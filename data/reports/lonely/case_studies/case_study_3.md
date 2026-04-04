# Case Study: High-Distress Signal Week 2020-W34
**Week starting:** 2020-08-17
**Distress score:** 0.037

## What Happened
The community distress score spiked to 0.037, 
exceeding the severe community distress threshold.

## Early Warning Signals

### 2020-W31 (FLAGGED, probability: 0.74)
- **post_volume**: 500.0000 (84.8% above average)
- **post_volume_roll4w**: 477.2500 (78.0% above average)
- **week_sin**: -0.5681 (74090.9% below average)
- **hopelessness_density_roll4w**: 0.0012 (20.1% above average)
- **isolation_total_roll4w**: 443.5000 (37.0% above average)

### 2020-W32 (FLAGGED, probability: 0.74)
- **post_volume**: 498.0000 (84.1% above average)
- **post_volume_roll4w**: 495.0000 (84.6% above average)
- **week_sin**: -0.6631 (86472.3% below average)
- **hopelessness_density_roll4w**: 0.0012 (22.8% above average)
- **isolation_total_roll4w**: 461.7500 (42.6% above average)

### 2020-W33 (FLAGGED, probability: 0.74)
- **post_volume**: 534.0000 (97.4% above average)
- **post_volume_roll4w**: 507.0000 (89.1% above average)
- **week_sin**: -0.7485 (97594.1% below average)
- **hopelessness_density_roll4w**: 0.0010 (7.8% above average)
- **isolation_total_roll4w**: 462.7500 (42.9% above average)

## Top Contributing Features (SHAP)

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | post_volume | 1.4440 |
| 2 | post_volume_roll4w | 0.5400 |
| 3 | week_sin | 0.5188 |
| 4 | hopelessness_density_roll4w | 0.3442 |
| 5 | isolation_total_roll4w | 0.3270 |
| 6 | economic_stress_total_delta | 0.3164 |
| 7 | avg_positive_roll4w | 0.2909 |
| 8 | distress_density_roll2w | 0.2448 |
| 9 | pct_very_negative | 0.2422 |
| 10 | domestic_stress_total_roll2w | 0.2341 |

## Summary

The early warning system detected precursor signals 3 weeks before this high-distress event. Key indicators included changes in post_volume, post_volume_roll4w, week_sin.