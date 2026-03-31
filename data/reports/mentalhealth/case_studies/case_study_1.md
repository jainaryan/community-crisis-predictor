# Case Study: High-Distress Signal Week 2019-W08
**Week starting:** 2019-02-18
**Distress score:** 0.337

## What Happened
The community distress score spiked to 0.337, 
exceeding the severe community distress threshold.

## Early Warning Signals

### 2019-W05 (FLAGGED, probability: 0.38)
- **posting_time_entropy**: 0.0000 (100.0% below average)
- **hopelessness_density**: 0.0009 (7.4% below average)
- **new_poster_ratio_roll4w**: 0.8368 (2.0% below average)
- **hopelessness_density_delta**: -0.0002 (8076994.9% below average)
- **topic_shift_jsd_4w**: 0.0104 (91.6% below average)

### 2019-W06 (not flagged, probability: 0.40)
- **posting_time_entropy**: 0.0000 (100.0% below average)
- **hopelessness_density**: 0.0008 (17.6% below average)
- **new_poster_ratio_roll4w**: 0.8446 (1.1% below average)
- **hopelessness_density_delta**: -0.0001 (4912391.7% below average)
- **topic_shift_jsd_4w**: 0.1181 (4.6% below average)

### 2019-W07 (not flagged, probability: 0.48)
- **posting_time_entropy**: 0.0000 (100.0% below average)
- **hopelessness_density**: 0.0010 (0.9% above average)
- **new_poster_ratio_roll4w**: 0.8441 (1.2% below average)
- **hopelessness_density_delta**: 0.0002 (8931933.9% above average)
- **topic_shift_jsd_4w**: 0.0855 (30.9% below average)

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