# Case Study: High-Distress Signal Week 2019-W12
**Week starting:** 2019-03-18
**Distress score:** 0.437

## What Happened
The community distress score spiked to 0.437, 
exceeding the severe community distress threshold.

## Early Warning Signals

### 2019-W09 (not flagged, probability: 0.14)
- **domestic_stress_density_delta**: -0.0005 (1280.0% below average)
- **avg_type_token_ratio_roll4w**: 0.6817 (16.5% above average)
- **pct_neutral_roll2w**: 0.0142 (17.0% below average)
- **avg_word_count_delta**: 3.6809 (5133.6% above average)
- **help_seeking_density_roll2w**: 0.0044 (30.5% above average)

### 2019-W10 (not flagged, probability: 0.15)
- **domestic_stress_density_delta**: -0.0021 (5461.8% below average)
- **avg_type_token_ratio_roll4w**: 0.6814 (16.5% above average)
- **pct_neutral_roll2w**: 0.0134 (21.7% below average)
- **avg_word_count_delta**: -8.2846 (11879.2% below average)
- **help_seeking_density_roll2w**: 0.0043 (27.0% above average)

### 2019-W11 (FLAGGED, probability: 0.43)
- **domestic_stress_density_delta**: 0.0033 (8347.0% above average)
- **avg_type_token_ratio_roll4w**: 0.6788 (16.0% above average)
- **pct_neutral_roll2w**: 0.0138 (19.5% below average)
- **avg_word_count_delta**: 4.9429 (6927.9% above average)
- **help_seeking_density_roll2w**: 0.0043 (27.7% above average)

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