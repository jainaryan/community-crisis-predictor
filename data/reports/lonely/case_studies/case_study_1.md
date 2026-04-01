# Case Study: High-Distress Signal Week 2018-W51
**Week starting:** 2018-12-17
**Distress score:** 0.320

## What Happened
The community distress score spiked to 0.320, 
exceeding the severe community distress threshold.

## Early Warning Signals

### 2018-W48 (not flagged, probability: 0.29)
- **new_poster_ratio_roll2w**: 0.8579 (3.3% above average)
- **avg_type_token_ratio**: 0.7127 (2.4% below average)
- **first_person_singular_ratio_roll2w**: 0.0850 (1.3% above average)
- **distress_density_delta**: -0.0003 (3066.7% below average)
- **avg_type_token_ratio_delta**: -0.0042 (6167.6% below average)

### 2018-W49 (FLAGGED, probability: 0.39)
- **new_poster_ratio_roll2w**: 0.8768 (5.6% above average)
- **avg_type_token_ratio**: 0.7300 (0.1% below average)
- **first_person_singular_ratio_roll2w**: 0.0848 (1.1% above average)
- **distress_density_delta**: 0.0019 (22087.6% above average)
- **avg_type_token_ratio_delta**: 0.0173 (26187.8% above average)

### 2018-W50 (not flagged, probability: 0.79)
- **new_poster_ratio_roll2w**: 0.8709 (4.9% above average)
- **avg_type_token_ratio**: 0.7327 (0.3% above average)
- **first_person_singular_ratio_roll2w**: 0.0831 (0.9% below average)
- **distress_density_delta**: -0.0009 (10812.2% below average)
- **avg_type_token_ratio_delta**: 0.0026 (4088.4% above average)

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