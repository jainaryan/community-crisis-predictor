from collections import deque

import numpy as np
import pandas as pd
from scipy.spatial.distance import jensenshannon
from sklearn.cluster import MiniBatchKMeans
from sklearn.feature_extraction.text import HashingVectorizer

from src.features.progress_util import iter_groupby_subreddit, tqdm_index


class TopicFeatureExtractor:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2", n_topics: int = 15,
                 min_topic_size: int = 10, max_posts_per_week: int = 200):
        self.model_name = model_name
        self.n_topics = n_topics
        self.min_topic_size = min_topic_size
        self.max_posts_per_week = max_posts_per_week
        # Stateless feature hashing keeps the representation fixed while the
        # clusterer is updated only with historical weeks.
        self._vectorizer = HashingVectorizer(
            n_features=4096,
            alternate_sign=False,
            norm="l2",
            lowercase=True,
            stop_words="english",
        )

    def _sample_texts(self, texts: list[str]) -> list[str]:
        if len(texts) <= self.max_posts_per_week:
            return texts
        rng = np.random.RandomState(42)
        indices = rng.choice(len(texts), self.max_posts_per_week, replace=False)
        return [texts[i] for i in indices]

    def _clean_week_texts(self, texts: list[str] | object) -> list[str]:
        if not isinstance(texts, list):
            return []
        sampled = self._sample_texts(texts)
        return [t for t in sampled if t and len(t) > 10]

    def _empty_result(self, index: pd.Index) -> pd.DataFrame:
        return pd.DataFrame(
            {
                "dominant_topic": [0] * len(index),
                "topic_entropy": [0.0] * len(index),
                "topic_shift_jsd": [0.0] * len(index),
                "topic_shift_jsd_4w": [0.0] * len(index),
            },
            index=index,
        )

    def _vectorize(self, texts: list[str]):
        if not texts:
            return None
        return self._vectorizer.transform(texts)

    def _new_clusterer(self) -> MiniBatchKMeans:
        return MiniBatchKMeans(
            n_clusters=self.n_topics,
            random_state=42,
            batch_size=max(32, self.max_posts_per_week),
            n_init=10,
        )

    def fit_and_extract(self, weekly_df: pd.DataFrame) -> pd.DataFrame:
        if weekly_df.empty:
            return self._empty_result(weekly_df.index)

        if "subreddit" in weekly_df.columns:
            grouped = iter_groupby_subreddit(weekly_df, "subreddit", "  Topic")
        else:
            grouped = [("__all__", weekly_df)]

        min_ready_texts = max(self.min_topic_size * 2, self.n_topics)
        result_parts: list[pd.DataFrame] = []

        for _, sub_df in grouped:
            sub_df = sub_df.sort_values(["iso_year", "iso_week"]).reset_index()
            rows: list[dict] = []
            history_texts: list[str] = []
            clusterer: MiniBatchKMeans | None = None
            prev_dist: np.ndarray | None = None
            dist_history: deque[np.ndarray] = deque(maxlen=4)

            for pos in tqdm_index(sub_df.index, total=len(sub_df), desc="  Topic: per-week stats"):
                week_row = sub_df.iloc[pos]
                row_index = week_row["index"]
                texts = self._clean_week_texts(week_row.get("texts", []))

                if texts:
                    history_texts.extend(texts)

                if len(history_texts) < min_ready_texts:
                    rows.append(
                        {
                            "index": row_index,
                            "dominant_topic": 0,
                            "topic_entropy": 0.0,
                            "topic_shift_jsd": 0.0,
                            "topic_shift_jsd_4w": 0.0,
                        }
                    )
                    continue

                if clusterer is None:
                    clusterer = self._new_clusterer()
                    try:
                        clusterer.partial_fit(self._vectorize(history_texts))
                    except Exception:
                        rows.append(
                            {
                                "index": row_index,
                                "dominant_topic": 0,
                                "topic_entropy": 0.0,
                                "topic_shift_jsd": 0.0,
                                "topic_shift_jsd_4w": 0.0,
                            }
                        )
                        clusterer = None
                        continue
                elif texts:
                    try:
                        clusterer.partial_fit(self._vectorize(texts))
                    except Exception:
                        rows.append(
                            {
                                "index": row_index,
                                "dominant_topic": 0,
                                "topic_entropy": 0.0,
                                "topic_shift_jsd": 0.0,
                                "topic_shift_jsd_4w": 0.0,
                            }
                        )
                        continue

                if not texts:
                    rows.append(
                        {
                            "index": row_index,
                            "dominant_topic": 0,
                            "topic_entropy": 0.0,
                            "topic_shift_jsd": 0.0,
                            "topic_shift_jsd_4w": 0.0,
                        }
                    )
                    continue

                try:
                    topic_ids = clusterer.predict(self._vectorize(texts))
                except Exception:
                    rows.append(
                        {
                            "index": row_index,
                            "dominant_topic": 0,
                            "topic_entropy": 0.0,
                            "topic_shift_jsd": 0.0,
                            "topic_shift_jsd_4w": 0.0,
                        }
                    )
                    continue

                dist = np.bincount(topic_ids, minlength=self.n_topics).astype(float)
                total = float(dist.sum())
                if total > 0:
                    dist_norm = dist / total
                    dominant = int(np.argmax(dist_norm))
                    entropy = float(-np.sum(dist_norm[dist_norm > 0] * np.log2(dist_norm[dist_norm > 0])))
                else:
                    dist_norm = dist
                    dominant = 0
                    entropy = 0.0

                if prev_dist is not None and total > 0 and prev_dist.sum() > 0:
                    jsd = float(jensenshannon(prev_dist, dist_norm))
                    if np.isnan(jsd):
                        jsd = 0.0
                else:
                    jsd = 0.0

                if len(dist_history) == 4 and total > 0 and dist_history[0].sum() > 0:
                    jsd_4w = float(jensenshannon(dist_history[0], dist_norm))
                    if np.isnan(jsd_4w):
                        jsd_4w = 0.0
                else:
                    jsd_4w = 0.0

                rows.append(
                    {
                        "index": row_index,
                        "dominant_topic": dominant,
                        "topic_entropy": entropy,
                        "topic_shift_jsd": jsd,
                        "topic_shift_jsd_4w": jsd_4w,
                    }
                )
                prev_dist = dist_norm if total > 0 else prev_dist
                if total > 0:
                    dist_history.append(dist_norm)

            result_parts.append(pd.DataFrame(rows).set_index("index"))

        if not result_parts:
            return self._empty_result(weekly_df.index)

        result = pd.concat(result_parts, axis=0).sort_index()
        result = result.reindex(weekly_df.index)
        return result
