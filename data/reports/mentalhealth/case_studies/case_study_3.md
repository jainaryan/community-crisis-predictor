# Case Study: High-Distress Signal Week 2019-W15
**Week starting:** 2019-04-08
**Distress score:** -0.706

## What Happened
The community distress score spiked to -0.706, 
exceeding the severe community distress threshold.

## Early Warning Signals

### 2019-W12 (FLAGGED, probability: 0.16)
- **posting_time_entropy**: 0.0000 (100.0% below average)
- **hopelessness_density**: 0.0009 (6.0% below average)
- **new_poster_ratio_roll4w**: 0.8482 (0.7% below average)
- **hopelessness_density_delta**: -0.0004 (20741825.6% below average)
- **topic_shift_jsd_4w**: 0.0302 (75.6% below average)

### 2019-W13 (not flagged, probability: 0.48)
- **posting_time_entropy**: 0.0000 (100.0% below average)
- **hopelessness_density**: 0.0010 (0.6% below average)
- **new_poster_ratio_roll4w**: 0.8347 (2.3% below average)
- **hopelessness_density_delta**: 0.0001 (2642117.5% above average)
- **topic_shift_jsd_4w**: 0.0944 (23.7% below average)

### 2019-W14 (FLAGGED, probability: 0.44)
- **posting_time_entropy**: 0.0000 (100.0% below average)
- **hopelessness_density**: 0.0013 (36.2% above average)
- **new_poster_ratio_roll4w**: 0.8508 (0.4% below average)
- **hopelessness_density_delta**: 0.0004 (17802954.8% above average)
- **topic_shift_jsd_4w**: 0.1634 (32.0% above average)

## Top Contributing Features (SHAP)

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | posting_time_entropy | 0.8438 |
| 2 | hopelessness_density | 0.7089 |
| 3 | new_poster_ratio_roll4w | 0.6236 |
| 4 | hopelessness_density_delta | 0.5255 |
| 5 | topic_shift_jsd_4w | 0.5073 |
| 6 | new_poster_ratio_delta | 0.3845 |
| 7 | avg_positive_roll4w | 0.3522 |
| 8 | avg_type_token_ratio_roll2w | 0.3239 |
| 9 | distress_density_roll2w | 0.2938 |
| 10 | topic_entropy_roll4w | 0.2120 |

## Summary

The early warning system detected precursor signals 3 weeks before this high-distress event. Key indicators included changes in posting_time_entropy, hopelessness_density, new_poster_ratio_roll4w.