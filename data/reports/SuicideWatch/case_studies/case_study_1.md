# Case Study: High-Distress Signal Week 2018-W52
**Week starting:** 2018-12-25
**Distress score:** 0.051

## What Happened
The community distress score spiked to 0.051, 
exceeding the severe community distress threshold.

## Early Warning Signals

### 2018-W49 (not flagged, probability: 0.40)
- **pct_neutral**: 0.0262 (12.0% above average)
- **help_seeking_density**: 0.0025 (19.9% below average)
- **pct_negative_roll2w**: 0.0954 (11.1% above average)
- **avg_negative_delta**: -0.0072 (53786.8% below average)
- **distress_density_roll2w**: 0.0077 (6.2% below average)

### 2018-W50 (FLAGGED, probability: 0.41)
- **pct_neutral**: 0.0284 (21.2% above average)
- **help_seeking_density**: 0.0045 (43.5% above average)
- **pct_negative_roll2w**: 0.1034 (20.5% above average)
- **avg_negative_delta**: 0.0067 (49482.2% above average)
- **distress_density_roll2w**: 0.0076 (8.2% below average)

### 2018-W51 (not flagged, probability: 0.36)
- **pct_neutral**: 0.0395 (69.0% above average)
- **help_seeking_density**: 0.0029 (6.2% below average)
- **pct_negative_roll2w**: 0.0910 (6.0% above average)
- **avg_negative_delta**: 0.0046 (34028.0% above average)
- **distress_density_roll2w**: 0.0070 (15.5% below average)

## Top Contributing Features (SHAP)

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | pct_neutral | 0.6362 |
| 2 | help_seeking_density | 0.6020 |
| 3 | pct_negative_roll2w | 0.4955 |
| 4 | avg_negative_delta | 0.4121 |
| 5 | distress_density_roll2w | 0.3892 |
| 6 | pct_positive_roll4w | 0.3044 |
| 7 | first_person_singular_ratio_roll2w | 0.2915 |
| 8 | pct_positive_roll2w | 0.2702 |
| 9 | new_poster_ratio_delta | 0.2504 |
| 10 | pct_negative_roll4w | 0.2306 |

## Summary

The early warning system detected precursor signals 3 weeks before this high-distress event. Key indicators included changes in pct_neutral, help_seeking_density, pct_negative_roll2w.