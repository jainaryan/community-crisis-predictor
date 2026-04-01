# Case Study: High-Distress Signal Week 2019-W07
**Week starting:** 2019-02-11
**Distress score:** 0.202

## What Happened
The community distress score spiked to 0.202, 
exceeding the severe community distress threshold.

## Early Warning Signals

### 2019-W04 (FLAGGED, probability: 0.24)
- **help_seeking_density**: 0.0028 (10.5% below average)
- **pct_neutral**: 0.0204 (12.7% below average)
- **pct_negative_roll2w**: 0.0886 (3.3% above average)
- **avg_negative_delta**: -0.0024 (17655.9% below average)
- **distress_density_roll2w**: 0.0083 (0.9% above average)

### 2019-W05 (not flagged, probability: 0.44)
- **help_seeking_density**: 0.0042 (34.9% above average)
- **pct_neutral**: 0.0151 (35.4% below average)
- **pct_negative_roll2w**: 0.0908 (5.8% above average)
- **avg_negative_delta**: 0.0070 (52301.8% above average)
- **distress_density_roll2w**: 0.0082 (0.3% below average)

### 2019-W06 (FLAGGED, probability: 0.35)
- **help_seeking_density**: 0.0038 (20.2% above average)
- **pct_neutral**: 0.0229 (2.0% below average)
- **pct_negative_roll2w**: 0.0934 (8.9% above average)
- **avg_negative_delta**: 0.0002 (1022.0% above average)
- **distress_density_roll2w**: 0.0083 (1.0% above average)

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