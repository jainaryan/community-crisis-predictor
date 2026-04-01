# Case Study: High-Distress Signal Week 2018-W51
**Week starting:** 2018-12-17
**Distress score:** 0.234

## What Happened
The community distress score spiked to 0.234, 
exceeding the severe community distress threshold.

## Early Warning Signals

### 2018-W48 (not flagged, probability: 0.68)
- **posting_time_entropy**: 0.0000 (100.0% below average)
- **new_poster_ratio_roll4w**: 0.8786 (2.9% above average)
- **hopelessness_density**: 0.0008 (14.5% below average)
- **hopelessness_density_delta**: -0.0006 (31766417.9% below average)
- **new_poster_ratio_delta**: -0.0368 (1559.8% below average)

### 2018-W49 (not flagged, probability: 0.51)
- **posting_time_entropy**: 0.0000 (100.0% below average)
- **new_poster_ratio_roll4w**: 0.8941 (4.7% above average)
- **hopelessness_density**: 0.0010 (3.1% below average)
- **hopelessness_density_delta**: 0.0001 (5478873.1% above average)
- **new_poster_ratio_delta**: 0.0225 (1116.4% above average)

### 2018-W50 (not flagged, probability: 0.56)
- **posting_time_entropy**: 0.0000 (100.0% below average)
- **new_poster_ratio_roll4w**: 0.9104 (6.6% above average)
- **hopelessness_density**: 0.0006 (42.3% below average)
- **hopelessness_density_delta**: -0.0004 (18939611.1% below average)
- **new_poster_ratio_delta**: 0.0052 (336.3% above average)

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