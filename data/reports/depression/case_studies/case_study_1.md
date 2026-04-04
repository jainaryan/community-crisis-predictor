# Case Study: High-Distress Signal Week 2019-W08
**Week starting:** 2019-02-18
**Distress score:** 0.390

## What Happened
The community distress score spiked to 0.390, 
exceeding the severe community distress threshold.

## Early Warning Signals

### 2019-W05 (not flagged, probability: 0.18)
- **domestic_stress_density_delta**: -0.0026 (6721.1% below average)
- **avg_type_token_ratio_roll4w**: 0.6865 (17.4% above average)
- **pct_neutral_roll2w**: 0.0150 (12.5% below average)
- **avg_word_count_delta**: 4.5308 (6341.9% above average)
- **help_seeking_density_roll2w**: 0.0047 (40.3% above average)

### 2019-W06 (not flagged, probability: 0.18)
- **domestic_stress_density_delta**: 0.0003 (772.1% above average)
- **avg_type_token_ratio_roll4w**: 0.6853 (17.1% above average)
- **pct_neutral_roll2w**: 0.0148 (13.9% below average)
- **avg_word_count_delta**: -2.4167 (3536.1% below average)
- **help_seeking_density_roll2w**: 0.0046 (38.0% above average)

### 2019-W07 (not flagged, probability: 0.18)
- **domestic_stress_density_delta**: -0.0031 (8190.3% below average)
- **avg_type_token_ratio_roll4w**: 0.6847 (17.0% above average)
- **pct_neutral_roll2w**: 0.0161 (6.3% below average)
- **avg_word_count_delta**: -1.7389 (2572.4% below average)
- **help_seeking_density_roll2w**: 0.0044 (31.7% above average)

## Top Contributing Features (SHAP)

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | domestic_stress_density_delta | 1.0312 |
| 2 | avg_type_token_ratio_roll4w | 0.6527 |
| 3 | pct_neutral_roll2w | 0.6401 |
| 4 | avg_word_count_delta | 0.5892 |
| 5 | help_seeking_density_roll2w | 0.4807 |
| 6 | topic_shift_jsd_roll2w | 0.3980 |
| 7 | week_sin | 0.3709 |
| 8 | topic_shift_jsd_4w | 0.3497 |
| 9 | domestic_stress_density_roll2w | 0.3072 |
| 10 | domestic_stress_density_roll4w | 0.2903 |

## Summary

The early warning system detected precursor signals 3 weeks before this high-distress event. Key indicators included changes in domestic_stress_density_delta, avg_type_token_ratio_roll4w, pct_neutral_roll2w.