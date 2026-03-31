# Case Study: High-Distress Signal Week 2019-W12
**Week starting:** 2019-03-18
**Distress score:** 0.299

## What Happened
The community distress score spiked to 0.299, 
exceeding the severe community distress threshold.

## Early Warning Signals

### 2019-W09 (not flagged, probability: 0.26)
- **new_poster_ratio_roll2w**: 0.8408 (1.3% above average)
- **first_person_singular_ratio_roll2w**: 0.0824 (1.8% below average)
- **distress_density_delta**: 0.0011 (13029.5% above average)
- **avg_compound_delta**: 0.0220 (2184.9% above average)
- **avg_type_token_ratio**: 0.7212 (1.3% below average)

### 2019-W10 (FLAGGED, probability: 0.23)
- **new_poster_ratio_roll2w**: 0.8132 (2.1% below average)
- **first_person_singular_ratio_roll2w**: 0.0814 (3.0% below average)
- **distress_density_delta**: -0.0035 (41386.7% below average)
- **avg_compound_delta**: -0.0850 (8917.1% below average)
- **avg_type_token_ratio**: 0.7175 (1.8% below average)

### 2019-W11 (not flagged, probability: 0.30)
- **new_poster_ratio_roll2w**: 0.7904 (4.8% below average)
- **first_person_singular_ratio_roll2w**: 0.0857 (2.1% above average)
- **distress_density_delta**: 0.0019 (22417.9% above average)
- **avg_compound_delta**: 0.0288 (2888.0% above average)
- **avg_type_token_ratio**: 0.7091 (2.9% below average)

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