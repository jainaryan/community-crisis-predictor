# Case Study: High-Distress Signal Week 2019-W29
**Week starting:** 2019-07-15
**Distress score:** 0.251

## What Happened
The community distress score spiked to 0.251, 
exceeding the severe community distress threshold.

## Early Warning Signals

### 2019-W26 (FLAGGED, probability: 0.29)
- **new_poster_ratio_roll2w**: 0.9597 (15.6% above average)
- **first_person_singular_ratio_roll2w**: 0.0854 (1.8% above average)
- **distress_density_delta**: 0.0026 (30959.8% above average)
- **avg_compound_delta**: -0.1199 (12535.3% below average)
- **avg_type_token_ratio**: 0.7258 (0.6% below average)

### 2019-W27 (FLAGGED, probability: 0.35)
- **new_poster_ratio_roll2w**: 0.9579 (15.4% above average)
- **first_person_singular_ratio_roll2w**: 0.0849 (1.2% above average)
- **distress_density_delta**: -0.0013 (14760.8% below average)
- **avg_compound_delta**: -0.0111 (1251.0% below average)
- **avg_type_token_ratio**: 0.7288 (0.2% below average)

### 2019-W28 (FLAGGED, probability: 0.36)
- **new_poster_ratio_roll2w**: 0.9571 (15.3% above average)
- **first_person_singular_ratio_roll2w**: 0.0827 (1.5% below average)
- **distress_density_delta**: 0.0004 (5417.0% above average)
- **avg_compound_delta**: 0.0337 (3394.0% above average)
- **avg_type_token_ratio**: 0.7372 (0.9% above average)

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