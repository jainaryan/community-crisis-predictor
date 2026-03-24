import argparse
import hashlib
import json
import sys
import time
from pathlib import Path

from src.config import load_config
from src.collector.storage import load_all_raw, save_processed
from src.processing.text_cleaner import process_posts
from src.processing.weekly_aggregator import WeeklyAggregator
from src.features.pipeline import FeaturePipeline


def main():
    parser = argparse.ArgumentParser(description="Extract features from collected data")
    parser.add_argument("--config", default="config/default.yaml")
    parser.add_argument("--skip-topics", action="store_true",
                        help="Skip BERTopic feature extraction (faster)")
    parser.add_argument(
        "--skip-if-up-to-date",
        action="store_true",
        help="Skip feature extraction when raw inputs/config are unchanged",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force rerun even when cache metadata indicates no upstream changes",
    )
    args = parser.parse_args()

    config = load_config(args.config)
    stage_start = time.perf_counter()
    cache_meta_path = Path(config["paths"]["features"]) / "feature_build_meta.json"
    current_fingerprint = _compute_feature_fingerprint(config, args.config, args.skip_topics)
    if args.skip_if_up_to_date and not args.force and _is_feature_cache_valid(cache_meta_path, current_fingerprint):
        print("Feature extraction skipped: upstream data/config unchanged.")
        print(f"  Cache metadata: {cache_meta_path}")
        return

    print("Loading raw data...")
    df = load_all_raw(config["paths"]["raw_data"], config["reddit"]["subreddits"])
    print(f"  {len(df)} total posts loaded")
    _print_counts_by_subreddit(df, label="posts loaded")

    print("Cleaning text...")
    min_len = config["processing"].get("min_post_length_chars", 20)
    df = process_posts(df, min_length=min_len)
    print(f"  {len(df)} posts after cleaning")
    _print_counts_by_subreddit(df, label="posts after cleaning")
    min_posts_after_cleaning = config.get("processing", {}).get("min_posts_after_cleaning", 50)
    if len(df) < min_posts_after_cleaning:
        print(
            "ERROR: Too few posts after cleaning "
            f"({len(df)} < required {min_posts_after_cleaning})."
        )
        print("Hint: rerun collection (`python -m src.pipeline.run_collect`) or lower cleaning thresholds.")
        sys.exit(1)

    print("Aggregating by week...")
    aggregator = WeeklyAggregator()
    weekly_df = aggregator.aggregate(df)
    print(f"  {len(weekly_df)} weeks")
    _print_counts_by_subreddit(weekly_df, label="weeks aggregated")
    wf_cfg = config.get("modeling", {}).get("walk_forward", {})
    min_train_weeks = int(wf_cfg.get("min_train_weeks", 26))
    gap_weeks = int(wf_cfg.get("gap_weeks", 1))
    seq_len = int(config.get("modeling", {}).get("lstm", {}).get("sequence_length", 8))
    min_weeks_required = min_train_weeks + gap_weeks + seq_len
    if len(weekly_df) < min_weeks_required:
        print(
            "ERROR: Weekly history too short for modeling "
            f"({len(weekly_df)} < required {min_weeks_required})."
        )
        print(
            "Hint: extend collection date range or use synthetic mode "
            "(`python -m src.pipeline.run_all --synthetic`)."
        )
        sys.exit(1)

    # Save processed weekly data
    save_processed(weekly_df, config["paths"]["processed_data"], "weekly")

    print("Extracting features...")
    pipeline = FeaturePipeline(config)
    feature_df = pipeline.run(weekly_df, skip_topics=args.skip_topics)

    save_processed(feature_df, config["paths"]["features"], "features")
    print(f"Feature matrix saved: {feature_df.shape}")
    _append_profile(
        config,
        {
            "stage": "features",
            "elapsed_seconds": round(time.perf_counter() - stage_start, 3),
            "rows_processed": int(len(df)),
            "weeks_generated": int(len(weekly_df)),
            "feature_rows": int(feature_df.shape[0]),
            "feature_cols": int(feature_df.shape[1]),
        },
    )
    _save_feature_cache_meta(cache_meta_path, current_fingerprint)
    print("Feature extraction complete.")


def _append_profile(config: dict, entry: dict) -> None:
    reports_root = Path(config["paths"]["reports"])
    reports_root.mkdir(parents=True, exist_ok=True)
    profile_path = reports_root / "pipeline_profile.json"
    payload = []
    if profile_path.exists():
        with open(profile_path, encoding="utf-8") as f:
            payload = json.load(f)
            if not isinstance(payload, list):
                payload = [payload]
    payload.append(entry)
    with open(profile_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)


def _print_counts_by_subreddit(df, label: str) -> None:
    if "subreddit" not in df.columns or df.empty:
        print(f"  No subreddit breakdown available for {label}.")
        return
    counts = (
        df.groupby("subreddit")
        .size()
        .sort_values(ascending=False)
    )
    print(f"  Per-subreddit {label}:")
    for sub, count in counts.items():
        print(f"    r/{sub}: {int(count)}")


def _compute_feature_fingerprint(config: dict, config_path: str, skip_topics: bool) -> dict:
    raw_root = Path(config["paths"]["raw_data"])
    subreddits = list(config["reddit"]["subreddits"])
    raw_files = []
    for sub in subreddits:
        p = raw_root / sub / "posts.parquet"
        if p.exists():
            st = p.stat()
            raw_files.append(
                {
                    "path": str(p),
                    "size": int(st.st_size),
                    "mtime_ns": int(st.st_mtime_ns),
                }
            )
    cfg_path = Path(config_path)
    cfg_sig = ""
    if cfg_path.exists():
        st = cfg_path.stat()
        cfg_sig = f"{st.st_size}:{st.st_mtime_ns}"

    base = {
        "subreddits": subreddits,
        "skip_topics": bool(skip_topics),
        "raw_files": raw_files,
        "config_sig": cfg_sig,
    }
    digest = hashlib.sha256(
        json.dumps(base, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    return {"version": 1, "fingerprint": digest, "base": base}


def _is_feature_cache_valid(meta_path: Path, current: dict) -> bool:
    if not meta_path.exists():
        return False
    try:
        with open(meta_path, encoding="utf-8") as f:
            saved = json.load(f)
    except (json.JSONDecodeError, OSError):
        return False
    return (
        isinstance(saved, dict)
        and saved.get("version") == current.get("version")
        and saved.get("fingerprint") == current.get("fingerprint")
    )


def _save_feature_cache_meta(meta_path: Path, payload: dict) -> None:
    meta_path.parent.mkdir(parents=True, exist_ok=True)
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)


if __name__ == "__main__":
    main()
