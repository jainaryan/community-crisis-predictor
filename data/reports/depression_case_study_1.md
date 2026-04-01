# Case Study: Crisis Week 2024-W32
**Week starting:** 2024-08-05
**Distress score:** 0.570

## What Happened
The community distress score spiked to 0.570, exceeding the crisis threshold.

## Early Warning Signals

### 2024-W29 (not flagged, probability: 0.06)
- **pct_positive**: 0.3739 (24.0% below average)
- **first_person_singular_ratio**: 0.0801 (4.9% above average)
- **unique_posters_delta**: -44.0000 (6894.1% below average)
- **hopelessness_density**: 0.0135 (35.7% above average)
- **avg_flesch_kincaid**: 4.5358 (1.6% below average)

### 2024-W30 (FLAGGED, probability: 0.68)
- **pct_positive**: 0.2211 (55.1% below average)
- **first_person_singular_ratio**: 0.0891 (16.7% above average)
- **unique_posters_delta**: -21.0000 (3342.6% below average)
- **hopelessness_density**: 0.0184 (84.5% above average)
- **avg_flesch_kincaid**: 4.4956 (2.5% below average)

### 2024-W31 (not flagged, probability: 0.04)
- **pct_positive**: 0.4500 (8.5% below average)
- **first_person_singular_ratio**: 0.0750 (1.7% below average)
- **unique_posters_delta**: 8.0000 (1135.3% above average)
- **hopelessness_density**: 0.0055 (45.1% below average)
- **avg_flesch_kincaid**: 4.8128 (4.4% above average)

## Top Contributing Features (SHAP)

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | pct_positive | 1.1015 |
| 2 | first_person_singular_ratio | 0.8112 |
| 3 | unique_posters_delta | 0.7443 |
| 4 | hopelessness_density | 0.6996 |
| 5 | avg_flesch_kincaid | 0.4713 |
| 6 | avg_flesch_kincaid_roll2w | 0.3051 |
| 7 | distress_density_roll4w | 0.2902 |
| 8 | avg_compound_delta | 0.2825 |
| 9 | first_person_singular_ratio_delta | 0.2738 |
| 10 | avg_negative_delta | 0.2736 |

## Summary

The early warning system detected precursor signals 3 weeks before this crisis event. Key indicators included changes in pct_positive, first_person_singular_ratio, unique_posters_delta.