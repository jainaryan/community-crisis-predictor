# Case Study: High-Distress Signal Week 2019-W04
**Week starting:** 2019-01-21
**Distress score:** -0.155

## What Happened
The community distress score spiked to -0.155, 
exceeding the severe community distress threshold.

## Early Warning Signals

### 2019-W01 (FLAGGED, probability: 0.08)
- **posting_time_entropy**: 0.0000 (100.0% below average)
- **new_poster_ratio_roll4w**: 0.8776 (2.8% above average)
- **hopelessness_density**: 0.0011 (8.1% above average)
- **hopelessness_density_delta**: 0.0002 (9606792.8% above average)
- **new_poster_ratio_delta**: -0.0607 (2637.6% below average)

### 2019-W02 (FLAGGED, probability: 0.15)
- **posting_time_entropy**: 0.0000 (100.0% below average)
- **new_poster_ratio_roll4w**: 0.8597 (0.7% above average)
- **hopelessness_density**: 0.0012 (21.2% above average)
- **hopelessness_density_delta**: 0.0001 (6338118.9% above average)
- **new_poster_ratio_delta**: 0.0088 (497.3% above average)

### 2019-W03 (FLAGGED, probability: 0.06)
- **posting_time_entropy**: 0.0000 (100.0% below average)
- **new_poster_ratio_roll4w**: 0.8570 (0.3% above average)
- **hopelessness_density**: 0.0009 (5.4% below average)
- **hopelessness_density_delta**: -0.0003 (12864082.6% below average)
- **new_poster_ratio_delta**: 0.0064 (389.1% above average)

## Top Contributing Features (SHAP)

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | posting_time_entropy | 0.8130 |
| 2 | new_poster_ratio_roll4w | 0.7487 |
| 3 | hopelessness_density | 0.7351 |
| 4 | hopelessness_density_delta | 0.5637 |
| 5 | new_poster_ratio_delta | 0.4455 |
| 6 | avg_type_token_ratio_roll2w | 0.4444 |
| 7 | distress_density_roll2w | 0.3597 |
| 8 | avg_positive_roll4w | 0.3277 |
| 9 | pct_negative | 0.2692 |
| 10 | pct_very_negative_roll2w | 0.2427 |

## Summary

The early warning system detected precursor signals 3 weeks before this high-distress event. Key indicators included changes in posting_time_entropy, new_poster_ratio_roll4w, hopelessness_density.