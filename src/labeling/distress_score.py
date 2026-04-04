import numpy as np
import pandas as pd


def compute_distress_score(
    feature_df: pd.DataFrame,
    weights: dict[str, float] = None,
    *,
    normalize: bool = True,
) -> pd.Series:
    if weights is None:
        weights = {
            "neg_sentiment": 0.25,
            "hopelessness": 0.20,
            "help_seeking": 0.15,
            "suicidality": 0.20,
            "isolation": 0.10,
            "economic_stress": 0.05,
            "domestic_stress": 0.05,
        }

    # Map weight keys to feature columns (all on per-word density scale).
    col_map = {
        "neg_sentiment": "avg_negative",
        "hopelessness": "hopelessness_density",
        "help_seeking": "help_seeking_density",
        "suicidality": "suicidality_density",
        "isolation": "isolation_density",
        "economic_stress": "economic_stress_density",
        "domestic_stress": "domestic_stress_density",
    }

    components = {}
    for key, col in col_map.items():
        if col in feature_df.columns:
            values = feature_df[col].values.astype(float)
            if normalize:
                mean = np.mean(values)
                std = np.std(values)
                if std > 0:
                    components[key] = (values - mean) / std
                else:
                    components[key] = np.zeros_like(values)
            else:
                components[key] = values

    # Renormalize active weights to sum to 1.0 so missing columns don't silently
    # deflate the score (e.g. if suicidality_total is absent, the 0.20 weight
    # disappears and the scale drops, making threshold comparisons inconsistent).
    active_weight_sum = sum(w for k, w in weights.items() if k in components)
    score = np.zeros(len(feature_df))
    for key, weight in weights.items():
        if key in components:
            effective_weight = weight / active_weight_sum if active_weight_sum > 0 else weight
            score += effective_weight * components[key]

    return pd.Series(score, index=feature_df.index, name="distress_score")
