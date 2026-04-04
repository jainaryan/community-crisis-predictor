# Case Study: High-Distress Signal Week 2018-W48
**Week starting:** 2018-11-26
**Distress score:** 0.194

## What Happened
The community distress score spiked to 0.194, 
exceeding the severe community distress threshold.

## Early Warning Signals

### 2018-W45 (not flagged, probability: 0.45)
- **isolation_density_delta**: 0.3075 (13158.0% above average)
- **avg_type_token_ratio_roll2w**: 0.7149 (3.8% above average)
- **avg_positive_roll2w**: 0.1418 (4.3% above average)
- **hopelessness_density_delta**: 0.0013 (67499.9% above average)
- **avg_neutral_delta**: -0.0189 (58218.3% below average)

### 2018-W46 (not flagged, probability: 0.50)
- **isolation_density_delta**: -0.0696 (2853.8% below average)
- **avg_type_token_ratio_roll2w**: 0.7190 (4.4% above average)
- **avg_positive_roll2w**: 0.1507 (10.8% above average)
- **hopelessness_density_delta**: 0.0002 (8696.3% above average)
- **avg_neutral_delta**: 0.0087 (26754.7% above average)

### 2018-W47 (not flagged, probability: 0.16)
- **isolation_density_delta**: 0.1064 (4618.2% above average)
- **avg_type_token_ratio_roll2w**: 0.7175 (4.2% above average)
- **avg_positive_roll2w**: 0.1539 (13.2% above average)
- **hopelessness_density_delta**: -0.0008 (45148.8% below average)
- **avg_neutral_delta**: -0.0230 (70760.9% below average)

## Top Contributing Features (SHAP)

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | isolation_density_delta | 0.7773 |
| 2 | avg_type_token_ratio_roll2w | 0.6429 |
| 3 | avg_positive_roll2w | 0.5438 |
| 4 | hopelessness_density_delta | 0.4854 |
| 5 | avg_neutral_delta | 0.4424 |
| 6 | avg_type_token_ratio_delta | 0.3638 |
| 7 | economic_stress_density | 0.3131 |
| 8 | week_sin | 0.2910 |
| 9 | first_person_singular_ratio_roll4w | 0.2899 |
| 10 | distress_density_delta | 0.2678 |

## Summary

The early warning system detected precursor signals 3 weeks before this high-distress event. Key indicators included changes in isolation_density_delta, avg_type_token_ratio_roll2w, avg_positive_roll2w.