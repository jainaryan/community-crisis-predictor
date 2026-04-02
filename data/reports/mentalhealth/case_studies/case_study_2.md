# Case Study: High-Distress Signal Week 2025-W04
**Week starting:** 2025-01-20
**Distress score:** -1.034

## What Happened
The community distress score spiked to -1.034, 
exceeding the severe community distress threshold.

## Early Warning Signals

### 2025-W01 (FLAGGED, probability: 0.45)
- **avg_word_count**: 51.1955 (8.5% above average)
- **avg_flesch_kincaid_roll2w**: 4.4097 (5.8% below average)
- **first_person_singular_ratio**: 0.0824 (10.7% above average)
- **pct_negative_roll4w**: 0.0813 (21.8% above average)
- **hopelessness_density_delta**: 0.0041 (36780.6% above average)

### 2025-W02 (FLAGGED, probability: 0.43)
- **avg_word_count**: 46.9876 (0.4% below average)
- **avg_flesch_kincaid_roll2w**: 4.4469 (5.0% below average)
- **first_person_singular_ratio**: 0.0694 (6.8% below average)
- **pct_negative_roll4w**: 0.0838 (25.6% above average)
- **hopelessness_density_delta**: -0.0124 (111089.7% below average)

### 2025-W03 (FLAGGED, probability: 0.45)
- **avg_word_count**: 46.5658 (1.3% below average)
- **avg_flesch_kincaid_roll2w**: 4.6519 (0.6% below average)
- **first_person_singular_ratio**: 0.0705 (5.3% below average)
- **pct_negative_roll4w**: 0.0764 (14.5% above average)
- **hopelessness_density_delta**: -0.0016 (13806.0% below average)

## Top Contributing Features (SHAP)

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | avg_word_count | 1.2818 |
| 2 | avg_flesch_kincaid_roll2w | 1.0886 |
| 3 | first_person_singular_ratio | 0.9594 |
| 4 | pct_negative_roll4w | 0.6057 |
| 5 | hopelessness_density_delta | 0.5454 |
| 6 | post_volume_delta | 0.4138 |
| 7 | posting_time_entropy | 0.2801 |
| 8 | posting_time_entropy_roll4w | 0.2252 |
| 9 | pct_neutral_roll2w | 0.2043 |
| 10 | posting_time_entropy_delta | 0.2031 |

## Summary

The early warning system detected precursor signals 3 weeks before this high-distress event. Key indicators included changes in avg_word_count, avg_flesch_kincaid_roll2w, first_person_singular_ratio.