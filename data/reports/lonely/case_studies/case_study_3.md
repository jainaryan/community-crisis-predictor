# Case Study: High-Distress Signal Week 2019-W38
**Week starting:** 2019-09-16
**Distress score:** 0.785

## What Happened
The community distress score spiked to 0.785, 
exceeding the severe community distress threshold.

## Early Warning Signals

### 2019-W35 (not flagged, probability: 0.37)
- **new_poster_ratio_roll2w**: 0.9826 (18.3% above average)
- **first_person_singular_ratio_roll2w**: 0.0866 (3.2% above average)
- **distress_density_delta**: -0.0006 (6633.1% below average)
- **avg_compound_delta**: 0.0341 (3432.0% above average)
- **avg_type_token_ratio**: 0.7285 (0.3% below average)

### 2019-W36 (FLAGGED, probability: 0.34)
- **new_poster_ratio_roll2w**: 0.9554 (15.1% above average)
- **first_person_singular_ratio_roll2w**: 0.0866 (3.2% above average)
- **distress_density_delta**: 0.0005 (6432.3% above average)
- **avg_compound_delta**: -0.0021 (322.9% below average)
- **avg_type_token_ratio**: 0.7074 (3.2% below average)

### 2019-W37 (FLAGGED, probability: 0.33)
- **new_poster_ratio_roll2w**: 0.9528 (14.8% above average)
- **first_person_singular_ratio_roll2w**: 0.0886 (5.6% above average)
- **distress_density_delta**: -0.0014 (16694.8% below average)
- **avg_compound_delta**: -0.0016 (263.7% below average)
- **avg_type_token_ratio**: 0.7136 (2.3% below average)

## Top Contributing Features (SHAP)

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | new_poster_ratio_roll2w | 0.6279 |
| 2 | first_person_singular_ratio_roll2w | 0.6241 |
| 3 | distress_density_delta | 0.5567 |
| 4 | avg_compound_delta | 0.4785 |
| 5 | avg_type_token_ratio | 0.4547 |
| 6 | avg_type_token_ratio_delta | 0.4410 |
| 7 | pct_negative_roll2w | 0.4379 |
| 8 | avg_positive | 0.2760 |
| 9 | pct_negative_roll4w | 0.2620 |
| 10 | hopelessness_density_roll2w | 0.2510 |

## Summary

The early warning system detected precursor signals 3 weeks before this high-distress event. Key indicators included changes in new_poster_ratio_roll2w, first_person_singular_ratio_roll2w, distress_density_delta.