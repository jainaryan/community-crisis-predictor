# Case Study: High-Distress Signal Week 2019-W11
**Week starting:** 2019-03-11
**Distress score:** 0.975

## What Happened
The community distress score spiked to 0.975, 
exceeding the severe community distress threshold.

## Early Warning Signals

### 2019-W08 (FLAGGED, probability: 0.32)
- **posting_time_entropy**: 0.0000 (100.0% below average)
- **hopelessness_density**: 0.0010 (2.4% below average)
- **new_poster_ratio_roll4w**: 0.8475 (0.8% below average)
- **hopelessness_density_delta**: -0.0000 (1564445.1% below average)
- **topic_shift_jsd_4w**: 0.0947 (23.5% below average)

### 2019-W09 (FLAGGED, probability: 0.37)
- **posting_time_entropy**: 0.0000 (100.0% below average)
- **hopelessness_density**: 0.0012 (17.3% above average)
- **new_poster_ratio_roll4w**: 0.8591 (0.6% above average)
- **hopelessness_density_delta**: 0.0002 (9537302.4% above average)
- **topic_shift_jsd_4w**: 0.0764 (38.3% below average)

### 2019-W10 (FLAGGED, probability: 0.41)
- **posting_time_entropy**: 0.0000 (100.0% below average)
- **hopelessness_density**: 0.0012 (17.9% above average)
- **new_poster_ratio_roll4w**: 0.8430 (1.3% below average)
- **hopelessness_density_delta**: 0.0000 (286405.8% above average)
- **topic_shift_jsd_4w**: 0.1479 (19.4% above average)

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