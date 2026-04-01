# Case Study: High-Distress Signal Week 2019-W06
**Week starting:** 2019-02-04
**Distress score:** 0.051

## What Happened
The community distress score spiked to 0.051, 
exceeding the severe community distress threshold.

## Early Warning Signals

### 2019-W03 (FLAGGED, probability: 0.23)
- **new_poster_ratio_roll2w**: 0.8045 (3.1% below average)
- **avg_type_token_ratio**: 0.7235 (0.9% below average)
- **first_person_singular_ratio_roll2w**: 0.0825 (1.7% below average)
- **distress_density_delta**: -0.0011 (12762.5% below average)
- **avg_type_token_ratio_delta**: 0.0043 (6589.4% above average)

### 2019-W04 (FLAGGED, probability: 0.17)
- **new_poster_ratio_roll2w**: 0.8257 (0.6% below average)
- **avg_type_token_ratio**: 0.6964 (4.7% below average)
- **first_person_singular_ratio_roll2w**: 0.0845 (0.8% above average)
- **distress_density_delta**: 0.0006 (6627.7% above average)
- **avg_type_token_ratio_delta**: -0.0271 (40796.6% below average)

### 2019-W05 (not flagged, probability: 0.20)
- **new_poster_ratio_roll2w**: 0.7758 (6.6% below average)
- **avg_type_token_ratio**: 0.7328 (0.3% above average)
- **first_person_singular_ratio_roll2w**: 0.0844 (0.6% above average)
- **distress_density_delta**: 0.0014 (16451.1% above average)
- **avg_type_token_ratio_delta**: 0.0364 (54980.8% above average)

## Top Contributing Features (SHAP)

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | new_poster_ratio_roll2w | 0.6025 |
| 2 | avg_type_token_ratio | 0.5896 |
| 3 | first_person_singular_ratio_roll2w | 0.5513 |
| 4 | distress_density_delta | 0.5052 |
| 5 | avg_type_token_ratio_delta | 0.4690 |
| 6 | pct_negative_roll2w | 0.4061 |
| 7 | pct_negative_roll4w | 0.3414 |
| 8 | avg_compound_delta | 0.3257 |
| 9 | help_seeking_density | 0.2821 |
| 10 | avg_positive | 0.2667 |

## Summary

The early warning system detected precursor signals 3 weeks before this high-distress event. Key indicators included changes in new_poster_ratio_roll2w, avg_type_token_ratio, first_person_singular_ratio_roll2w.