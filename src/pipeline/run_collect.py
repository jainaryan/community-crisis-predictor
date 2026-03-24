import argparse
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from src.config import load_config
from src.data_quality.completeness import (
    check_weekly_completeness,
    flag_missing_weeks,
    log_source_provenance,
)
from src.collector.manifest import (
    is_file_entry_valid,
    load_manifest,
    record_file_entry,
    record_subreddit_ingestion,
    save_manifest,
)
from src.collector.privacy import strip_pii
from src.collector.storage import save_raw
from src.collector.synthetic import generate_synthetic_data


def main():
    parser = argparse.ArgumentParser(description="Collect Reddit data")
    parser.add_argument("--config", default="config/default.yaml")
    parser.add_argument(
        "--synthetic",
        action="store_true",
        help="Generate synthetic data instead of using Reddit API",
    )
    args = parser.parse_args()

    config = load_config(args.config)
    source = config.get("collection", {}).get("source", "reddit_api")
    if args.synthetic:
        source = "synthetic"
    reports_root = Path(config["paths"]["reports"])
    reports_root.mkdir(parents=True, exist_ok=True)
    profile_path = reports_root / "pipeline_profile.json"
    stage_start = time.perf_counter()
    profile_entries: list[dict] = []

    print(f"Collection source: {source}")
    if source == "synthetic":
        print("Generating synthetic data...")
        datasets = generate_synthetic_data(config, seed=config.get("random_seed", 42))
        for subreddit, df in datasets.items():
            print(f"  {subreddit}: {len(df)} posts")
            df = strip_pii(df, config["collection"]["privacy_salt"])
            df["data_source"] = "synthetic"
            path = save_raw(df, config["paths"]["raw_data"], subreddit)
            print(f"  Saved to {path}")
            _run_data_quality_and_log(
                df=df,
                subreddit=subreddit,
                source="synthetic",
                date_range=config["reddit"]["date_range"],
                reports_root=reports_root,
                quality_db_path=config.get("paths", {}).get("quality_db", "data/quality.db"),
            )
    elif source == "zenodo_covid":
        from src.collector.zenodo_loader import ZenodoLoader

        zen = config["collection"].get("zenodo", {})
        date_range = zen.get("date_range", config["reddit"]["date_range"])
        loader = ZenodoLoader(
            dataset_url=zen["dataset_url"],
            archive_dir=zen.get(
                "local_archive_dir", config.get("paths", {}).get("external_zenodo", "data/external/zenodo")
            ),
            staging_dir=zen.get(
                "staging_dir", config.get("paths", {}).get("staging_zenodo", "data/staging/zenodo")
            ),
            record_id=int(zen.get("record_id", 3941387)),
            timeframes=zen.get("timeframes", ["2018", "2019", "pre", "post"]),
        )
        manifest_path = zen.get(
            "manifest_path",
            str(
                Path(config.get("paths", {}).get("staging_zenodo", "data/staging/zenodo")) / "manifest.json"
            ),
        )
        manifest = load_manifest(manifest_path)

        subreddits = zen.get("subreddits", config["reddit"]["subreddits"])
        for subreddit in subreddits:
            sub_start = time.perf_counter()
            raw_path = Path(config["paths"]["raw_data"]) / subreddit / "posts.parquet"
            if raw_path.exists() and manifest.get("subreddits", {}).get(subreddit, {}).get("status") == "ingested":
                files_ok = True
                for file_path in manifest.get("subreddits", {}).get(subreddit, {}).get("files", []):
                    if not is_file_entry_valid(manifest, file_path):
                        files_ok = False
                        break
                if files_ok:
                    print(f"Skipping r/{subreddit}: already ingested and manifest valid.")
                    elapsed = time.perf_counter() - sub_start
                    profile_entries.append(
                        {
                            "stage": "collect",
                            "subreddit": subreddit,
                            "elapsed_seconds": round(elapsed, 3),
                            "rows_processed": int(
                                manifest.get("subreddits", {}).get(subreddit, {}).get("rows", 0)
                            ),
                            "throughput_rows_per_sec": 0.0,
                            "source": "zenodo_covid",
                            "status": "skipped_manifest_valid",
                        }
                    )
                    continue

            print(f"Collecting r/{subreddit} via Zenodo dataset ...")
            print(f"  Date range filter: {date_range.get('start')} -> {date_range.get('end')}")
            downloaded_files = loader.ensure_subreddit_files(subreddit)
            print(f"  Files prepared for r/{subreddit}: {len(downloaded_files)}")
            for p in downloaded_files:
                record_file_entry(manifest, p)
            manifest.setdefault("subreddits", {}).setdefault(subreddit, {})["files"] = [
                str(p) for p in downloaded_files
            ]
            save_manifest(manifest_path, manifest)

            df = loader.load_subreddit_posts(
                subreddit=subreddit,
                start_date=date_range.get("start"),
                end_date=date_range.get("end"),
            )
            if df.empty:
                print(f"  No posts found for r/{subreddit} in Zenodo staging files")
                record_subreddit_ingestion(
                    manifest,
                    subreddit=subreddit,
                    rows=0,
                    min_created_utc=None,
                    max_created_utc=None,
                    status="empty",
                )
                save_manifest(manifest_path, manifest)
                continue

            df = strip_pii(df, config["collection"]["privacy_salt"])
            df["data_source"] = "zenodo_covid"
            path = save_raw(df, config["paths"]["raw_data"], subreddit)
            print(f"  Saved {len(df)} posts to {path}")

            min_ts = int(df["created_utc"].min()) if "created_utc" in df.columns else None
            max_ts = int(df["created_utc"].max()) if "created_utc" in df.columns else None
            record_subreddit_ingestion(
                manifest,
                subreddit=subreddit,
                rows=len(df),
                min_created_utc=min_ts,
                max_created_utc=max_ts,
                status="ingested",
            )
            save_manifest(manifest_path, manifest)

            _run_data_quality_and_log(
                df=df,
                subreddit=subreddit,
                source="zenodo_covid",
                date_range=date_range,
                reports_root=reports_root,
                quality_db_path=config.get("paths", {}).get("quality_db", "data/quality.db"),
            )
            elapsed = time.perf_counter() - sub_start
            print(f"  r/{subreddit} collection finished in {elapsed:.2f}s")
            profile_entries.append(
                {
                    "stage": "collect",
                    "subreddit": subreddit,
                    "elapsed_seconds": round(elapsed, 3),
                    "rows_processed": int(len(df)),
                    "throughput_rows_per_sec": round(len(df) / max(elapsed, 1e-9), 3),
                    "source": "zenodo_covid",
                }
            )

    else:
        # Real collection via PushshiftLoader (PullPush.io — free, no auth needed)
        from src.collector.historical_loader import PushshiftLoader

        date_range = config["reddit"]["date_range"]
        after_dt = datetime.fromisoformat(date_range["start"])
        before_dt = datetime.fromisoformat(date_range["end"])
        after_ts = int(after_dt.replace(tzinfo=timezone.utc).timestamp())
        before_ts = int(before_dt.replace(tzinfo=timezone.utc).timestamp())

        pushshift_url = config["collection"].get(
            "pushshift_base_url", "https://api.pullpush.io"
        )
        batch_size = config["collection"].get("batch_size", 500)
        rate_limit_rps = config["collection"].get("rate_limit_rps", 1.0)

        loader = PushshiftLoader(base_url=pushshift_url, rate_limit_rps=rate_limit_rps)

        for subreddit in config["reddit"]["subreddits"]:
            sub_start = time.perf_counter()
            print(f"Collecting r/{subreddit} via PullPush.io ...")
            print(f"  Date range: {date_range['start']} -> {date_range['end']}")
            print("  (This may take 20–40 min due to rate limiting — ~1 req/sec)")
            source = "pushshift"

            try:
                df, summary = loader.load_range(
                    subreddit=subreddit,
                    after=after_ts,
                    before=before_ts,
                    batch_size=batch_size,
                )
            except Exception as e:
                print(f"  PullPush failed: {e}")
                print("  Falling back to PRAW...")
                df = _collect_via_praw(config, subreddit, after_dt, before_dt)
                source = "praw"
                summary = None

            if df is None or df.empty:
                print(f"  No posts found for r/{subreddit}")
                elapsed = time.perf_counter() - sub_start
                profile_entries.append(
                    {
                        "stage": "collect",
                        "subreddit": subreddit,
                        "elapsed_seconds": round(elapsed, 3),
                        "rows_processed": 0,
                        "throughput_rows_per_sec": 0.0,
                        "source": source,
                    }
                )
                continue

            print(f"  {len(df)} posts collected")
            if summary is not None:
                print(
                    f"  Requests: {summary.request_count}, retries: {summary.retry_count}, "
                    f"truncated: {summary.truncated}"
                )
            df = strip_pii(df, config["collection"]["privacy_salt"])
            df["data_source"] = source
            path = save_raw(df, config["paths"]["raw_data"], subreddit)
            print(f"  Saved to {path}")
            _run_data_quality_and_log(
                df=df,
                subreddit=subreddit,
                source=source,
                date_range=config["reddit"]["date_range"],
                reports_root=reports_root,
                quality_db_path=config.get("paths", {}).get("quality_db", "data/quality.db"),
            )
            elapsed = time.perf_counter() - sub_start
            print(f"  r/{subreddit} collection finished in {elapsed:.2f}s")
            profile_entries.append(
                {
                    "stage": "collect",
                    "subreddit": subreddit,
                    "elapsed_seconds": round(elapsed, 3),
                    "rows_processed": int(len(df)),
                    "throughput_rows_per_sec": round(len(df) / max(elapsed, 1e-9), 3),
                    "source": source,
                    "retry_count": int(summary.retry_count) if summary is not None else 0,
                    "truncated": bool(summary.truncated) if summary is not None else False,
                }
            )

    total_elapsed = time.perf_counter() - stage_start
    _append_profile(
        profile_path,
        {
            "stage": "collect_total",
            "elapsed_seconds": round(total_elapsed, 3),
            "subreddit_runs": profile_entries,
        },
    )
    print("Collection complete.")


def _collect_via_praw(config, subreddit, after, before):
    """PRAW fallback — only fetches recent posts (~1000 limit)."""
    try:
        from src.collector.reddit_client import RedditCollector
    except ImportError:
        print("PRAW not installed. Install praw or use --synthetic.", file=sys.stderr)
        return None

    collector = RedditCollector(config)
    return collector.collect_subreddit(subreddit, after, before)


def _run_data_quality_and_log(
    df,
    subreddit: str,
    source: str,
    date_range: dict,
    reports_root: Path,
    quality_db_path: str,
) -> None:
    completeness_df = check_weekly_completeness(df, subreddit)
    missing_weeks = flag_missing_weeks(
        completeness_df,
        subreddit=subreddit,
        start_date=date_range["start"],
        end_date=date_range["end"],
    )
    for wk in completeness_df["week_start"].astype(str).tolist():
        log_source_provenance(
            subreddit=subreddit,
            week=wk,
            source=source,
            db_path=quality_db_path,
        )

    sub_report_dir = reports_root / subreddit
    sub_report_dir.mkdir(parents=True, exist_ok=True)
    completeness_csv = sub_report_dir / "weekly_completeness.csv"
    completeness_df.to_csv(completeness_csv, index=False)

    report = {
        "subreddit": subreddit,
        "source": source,
        "total_weeks_observed": int(len(completeness_df)),
        "gap_weeks_below_50pct": int(completeness_df["is_gap"].sum()) if not completeness_df.empty else 0,
        "missing_week_count": len(missing_weeks),
        "missing_weeks": missing_weeks,
        "avg_completeness_score": float(completeness_df["completeness_score"].mean())
        if not completeness_df.empty
        else 0.0,
    }
    with open(sub_report_dir / "data_quality_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    print(
        f"  Data quality: {report['gap_weeks_below_50pct']} gap week(s), "
        f"{report['missing_week_count']} missing week(s)"
    )


def _append_profile(profile_path: Path, entry: dict) -> None:
    payload = []
    if profile_path.exists():
        with open(profile_path, encoding="utf-8") as f:
            payload = json.load(f)
            if not isinstance(payload, list):
                payload = [payload]
    payload.append(entry)
    with open(profile_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)


if __name__ == "__main__":
    main()
