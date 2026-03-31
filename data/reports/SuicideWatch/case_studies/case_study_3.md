# Case Study: High-Distress Signal Week 2019-W11
**Week starting:** 2019-03-11
**Distress score:** -0.357

## What Happened
The community distress score spiked to -0.357, 
exceeding the severe community distress threshold.

## Early Warning Signals

### 2019-W08 (FLAGGED, probability: 0.43)
- **pct_neutral**: 0.0107 (54.3% below average)
- **help_seeking_density**: 0.0033 (5.9% above average)
- **pct_negative_roll2w**: 0.0823 (4.1% below average)
- **avg_negative_delta**: 0.0008 (6003.8% above average)
- **distress_density_roll2w**: 0.0081 (2.1% below average)

### 2019-W09 (not flagged, probability: 0.42)
- **pct_neutral**: 0.0222 (5.2% below average)
- **help_seeking_density**: 0.0037 (18.9% above average)
- **pct_negative_roll2w**: 0.0856 (0.3% below average)
- **avg_negative_delta**: 0.0010 (7072.4% above average)
- **distress_density_roll2w**: 0.0079 (4.0% below average)

### 2019-W10 (FLAGGED, probability: 0.22)
- **pct_neutral**: 0.0187 (20.2% below average)
- **help_seeking_density**: 0.0035 (11.1% above average)
- **pct_negative_roll2w**: 0.0870 (1.4% above average)
- **avg_negative_delta**: -0.0030 (22757.4% below average)
- **distress_density_roll2w**: 0.0084 (1.6% above average)

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