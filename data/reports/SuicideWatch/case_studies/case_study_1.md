# Case Study: High-Distress Signal Week 2018-W52
**Week starting:** 2018-12-25
**Distress score:** 0.051

## What Happened
The community distress score spiked to 0.051, 
exceeding the severe community distress threshold.

## Early Warning Signals

### 2018-W49 (not flagged, probability: 0.42)
- **help_seeking_density**: 0.0025 (19.9% below average)
- **pct_neutral**: 0.0262 (12.0% above average)
- **pct_negative_roll2w**: 0.0954 (11.1% above average)
- **avg_negative_delta**: -0.0072 (53786.8% below average)
- **distress_density_roll2w**: 0.0077 (6.2% below average)

### 2018-W50 (FLAGGED, probability: 0.35)
- **help_seeking_density**: 0.0045 (43.5% above average)
- **pct_neutral**: 0.0284 (21.2% above average)
- **pct_negative_roll2w**: 0.1034 (20.5% above average)
- **avg_negative_delta**: 0.0067 (49482.2% above average)
- **distress_density_roll2w**: 0.0076 (8.2% below average)

### 2018-W51 (not flagged, probability: 0.33)
- **help_seeking_density**: 0.0029 (6.2% below average)
- **pct_neutral**: 0.0395 (69.0% above average)
- **pct_negative_roll2w**: 0.0910 (6.0% above average)
- **avg_negative_delta**: 0.0046 (34028.0% above average)
- **distress_density_roll2w**: 0.0070 (15.5% below average)

## Top Contributing Features (SHAP)

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | help_seeking_density | 0.7066 |
| 2 | pct_neutral | 0.5677 |
| 3 | pct_negative_roll2w | 0.5664 |
| 4 | avg_negative_delta | 0.4251 |
| 5 | distress_density_roll2w | 0.3882 |
| 6 | pct_positive_roll4w | 0.3652 |
| 7 | first_person_singular_ratio_roll2w | 0.3640 |
| 8 | pct_positive_roll2w | 0.3369 |
| 9 | avg_flesch_kincaid_delta | 0.3127 |
| 10 | avg_type_token_ratio_roll4w | 0.3007 |

## Summary

The early warning system detected precursor signals 3 weeks before this high-distress event. Key indicators included changes in help_seeking_density, pct_neutral, pct_negative_roll2w.