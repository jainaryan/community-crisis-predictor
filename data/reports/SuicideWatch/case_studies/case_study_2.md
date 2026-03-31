# Case Study: High-Distress Signal Week 2019-W06
**Week starting:** 2019-02-04
**Distress score:** 0.341

## What Happened
The community distress score spiked to 0.341, 
exceeding the severe community distress threshold.

## Early Warning Signals

### 2019-W03 (not flagged, probability: 0.44)
- **pct_neutral**: 0.0085 (63.5% below average)
- **help_seeking_density**: 0.0040 (26.5% above average)
- **pct_negative_roll2w**: 0.0925 (7.8% above average)
- **avg_negative_delta**: 0.0020 (14463.9% above average)
- **distress_density_roll2w**: 0.0080 (2.6% below average)

### 2019-W04 (not flagged, probability: 0.42)
- **pct_neutral**: 0.0204 (12.7% below average)
- **help_seeking_density**: 0.0028 (10.5% below average)
- **pct_negative_roll2w**: 0.0886 (3.3% above average)
- **avg_negative_delta**: -0.0024 (17655.9% below average)
- **distress_density_roll2w**: 0.0083 (0.9% above average)

### 2019-W05 (not flagged, probability: 0.54)
- **pct_neutral**: 0.0151 (35.4% below average)
- **help_seeking_density**: 0.0042 (34.9% above average)
- **pct_negative_roll2w**: 0.0908 (5.8% above average)
- **avg_negative_delta**: 0.0070 (52301.8% above average)
- **distress_density_roll2w**: 0.0082 (0.3% below average)

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