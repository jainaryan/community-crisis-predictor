# Case Study: Crisis Week 2024-W44
**Week starting:** 2024-10-28
**Distress score:** 1.371

## What Happened
The community distress score spiked to 1.371, exceeding the crisis threshold.

## Early Warning Signals

### 2024-W41 (not flagged, probability: 0.23)
- **hopelessness_density**: 0.0067 (24.8% below average)
- **first_person_singular_ratio**: 0.0786 (4.6% above average)
- **pct_negative_roll2w**: 0.0614 (3.2% below average)
- **pct_very_negative_delta**: -0.3053 (12283.2% below average)
- **avg_neutral_delta**: 0.0458 (9994.2% above average)

### 2024-W42 (not flagged, probability: 0.16)
- **hopelessness_density**: 0.0071 (20.9% below average)
- **first_person_singular_ratio**: 0.0734 (2.4% below average)
- **pct_negative_roll2w**: 0.0395 (37.8% below average)
- **pct_very_negative_delta**: -0.0301 (1300.1% below average)
- **avg_neutral_delta**: 0.0098 (2211.8% above average)

### 2024-W43 (FLAGGED, probability: 0.89)
- **hopelessness_density**: 0.0151 (68.5% above average)
- **first_person_singular_ratio**: 0.0834 (10.9% above average)
- **pct_negative_roll2w**: 0.0716 (12.8% above average)
- **pct_very_negative_delta**: 0.2049 (8077.0% above average)
- **avg_neutral_delta**: -0.0223 (4723.3% below average)

## Top Contributing Features (SHAP)

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | hopelessness_density | 1.8401 |
| 2 | first_person_singular_ratio | 1.0309 |
| 3 | pct_negative_roll2w | 0.5802 |
| 4 | pct_very_negative_delta | 0.5750 |
| 5 | avg_neutral_delta | 0.4919 |
| 6 | avg_positive_delta | 0.4412 |
| 7 | avg_compound | 0.2582 |
| 8 | avg_negative_roll4w | 0.2396 |
| 9 | avg_positive_roll4w | 0.2212 |
| 10 | avg_comments_roll2w | 0.1863 |

## Summary

The early warning system detected precursor signals 3 weeks before this crisis event. Key indicators included changes in hopelessness_density, first_person_singular_ratio, pct_negative_roll2w.