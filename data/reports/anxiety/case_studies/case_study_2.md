# Case Study: High-Distress Signal Week 2020-W12
**Week starting:** 2020-03-16
**Distress score:** 0.221

## What Happened
The community distress score spiked to 0.221, 
exceeding the severe community distress threshold.

## Early Warning Signals

### 2020-W09 (FLAGGED, probability: 0.37)
- **suicidality_density_roll2w**: 0.0380 (9.0% below average)
- **avg_type_token_ratio_roll4w**: 0.6959 (5.7% above average)
- **help_seeking_density_delta**: -0.0004 (3025.3% below average)
- **avg_type_token_ratio_delta**: 0.0019 (1417.2% above average)
- **topic_shift_jsd_4w**: 0.1010 (12.8% below average)

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