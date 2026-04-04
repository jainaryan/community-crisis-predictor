# Case Study: High-Distress Signal Week 2019-W01
**Week starting:** 2018-12-31
**Distress score:** 0.237

## What Happened
The community distress score spiked to 0.237, 
exceeding the severe community distress threshold.

## Early Warning Signals

### 2018-W50 (not flagged, probability: 0.37)
- **suicidality_density_roll2w**: 0.0408 (2.2% below average)
- **avg_type_token_ratio_roll4w**: 0.6968 (5.8% above average)
- **help_seeking_density_delta**: 0.0000 (249.3% above average)
- **avg_type_token_ratio_delta**: -0.0001 (151.9% below average)
- **topic_shift_jsd_4w**: 0.0948 (18.1% below average)

### 2018-W51 (FLAGGED, probability: 0.36)
- **suicidality_density_roll2w**: 0.0352 (15.6% below average)
- **avg_type_token_ratio_roll4w**: 0.6954 (5.6% above average)
- **help_seeking_density_delta**: 0.0004 (3277.2% above average)
- **avg_type_token_ratio_delta**: -0.0050 (4113.8% below average)
- **topic_shift_jsd_4w**: 0.0612 (47.1% below average)

### 2018-W52 (not flagged, probability: 0.35)
- **suicidality_density_roll2w**: 0.0366 (12.2% below average)
- **avg_type_token_ratio_roll4w**: 0.6918 (5.0% above average)
- **help_seeking_density_delta**: 0.0000 (225.1% above average)
- **avg_type_token_ratio_delta**: -0.0091 (7365.8% below average)
- **topic_shift_jsd_4w**: 0.1188 (2.6% above average)

## Top Contributing Features (SHAP)

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | suicidality_density_roll2w | 1.4114 |
| 2 | avg_type_token_ratio_roll4w | 0.7217 |
| 3 | help_seeking_density_delta | 0.6307 |
| 4 | avg_type_token_ratio_delta | 0.5976 |
| 5 | topic_shift_jsd_4w | 0.5287 |
| 6 | domestic_stress_density_roll2w | 0.5020 |
| 7 | pct_neutral_roll4w | 0.4659 |
| 8 | distress_density_roll2w | 0.3540 |
| 9 | topic_shift_jsd_roll2w | 0.2650 |
| 10 | avg_type_token_ratio | 0.2185 |

## Summary

The early warning system detected precursor signals 3 weeks before this high-distress event. Key indicators included changes in suicidality_density_roll2w, avg_type_token_ratio_roll4w, help_seeking_density_delta.