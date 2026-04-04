# Case Study: High-Distress Signal Week 2020-W13
**Week starting:** 2020-03-23
**Distress score:** 0.108

## What Happened
The community distress score spiked to 0.108, 
exceeding the severe community distress threshold.

## Early Warning Signals

### 2020-W10 (FLAGGED, probability: 0.33)
- **suicidality_density_roll2w**: 0.0394 (5.5% below average)
- **avg_type_token_ratio_roll4w**: 0.6949 (5.5% above average)
- **help_seeking_density_delta**: -0.0001 (495.4% below average)
- **avg_type_token_ratio_delta**: -0.0041 (3369.3% below average)
- **topic_shift_jsd_4w**: 0.0774 (33.2% below average)

### 2020-W11 (FLAGGED, probability: 0.34)
- **suicidality_density_roll2w**: 0.0393 (5.7% below average)
- **avg_type_token_ratio_roll4w**: 0.6971 (5.8% above average)
- **help_seeking_density_delta**: -0.0000 (259.8% below average)
- **avg_type_token_ratio_delta**: 0.0081 (6351.6% above average)
- **topic_shift_jsd_4w**: 0.1616 (39.6% above average)

### 2020-W12 (FLAGGED, probability: 0.32)
- **suicidality_density_roll2w**: 0.0417 (0.0% above average)
- **avg_type_token_ratio_roll4w**: 0.6977 (5.9% above average)
- **help_seeking_density_delta**: -0.0005 (3395.6% below average)
- **avg_type_token_ratio_delta**: -0.0033 (2754.9% below average)
- **topic_shift_jsd_4w**: 0.0969 (16.4% below average)

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