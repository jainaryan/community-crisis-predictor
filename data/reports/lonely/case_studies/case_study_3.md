# Case Study: High-Distress Signal Week 2019-W09
**Week starting:** 2019-02-25
**Distress score:** -0.703

## What Happened
The community distress score spiked to -0.703, 
exceeding the severe community distress threshold.

## Early Warning Signals

### 2019-W06 (FLAGGED, probability: 0.16)
- **new_poster_ratio_roll2w**: 0.8082 (2.7% below average)
- **avg_type_token_ratio**: 0.7266 (0.5% below average)
- **first_person_singular_ratio_roll2w**: 0.0826 (1.6% below average)
- **distress_density_delta**: 0.0017 (20690.4% above average)
- **avg_type_token_ratio_delta**: -0.0062 (9199.9% below average)

### 2019-W07 (not flagged, probability: 0.16)
- **new_poster_ratio_roll2w**: 0.8517 (2.6% above average)
- **avg_type_token_ratio**: 0.7438 (1.8% above average)
- **first_person_singular_ratio_roll2w**: 0.0785 (6.5% below average)
- **distress_density_delta**: -0.0011 (12423.4% below average)
- **avg_type_token_ratio_delta**: 0.0172 (26039.8% above average)

### 2019-W08 (not flagged, probability: 0.24)
- **new_poster_ratio_roll2w**: 0.8164 (1.7% below average)
- **avg_type_token_ratio**: 0.7029 (3.8% below average)
- **first_person_singular_ratio_roll2w**: 0.0807 (3.8% below average)
- **distress_density_delta**: -0.0004 (4582.6% below average)
- **avg_type_token_ratio_delta**: -0.0410 (61664.4% below average)

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