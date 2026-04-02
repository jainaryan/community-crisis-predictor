# Case Study: High-Distress Signal Week 2024-W37
**Week starting:** 2024-09-09
**Distress score:** -0.095

## What Happened
The community distress score spiked to -0.095, 
exceeding the severe community distress threshold.

## Early Warning Signals

### 2024-W34 (not flagged, probability: 0.00)
- **avg_word_count**: 43.9459 (6.8% below average)
- **avg_flesch_kincaid_roll2w**: 4.7920 (2.4% above average)
- **first_person_singular_ratio**: 0.0722 (3.0% below average)
- **pct_negative_roll4w**: 0.0782 (17.2% above average)
- **hopelessness_density_delta**: 0.0013 (11477.2% above average)

### 2024-W35 (FLAGGED, probability: 0.27)
- **avg_word_count**: 45.7328 (3.1% below average)
- **avg_flesch_kincaid_roll2w**: 4.7025 (0.5% above average)
- **first_person_singular_ratio**: 0.0736 (1.1% below average)
- **pct_negative_roll4w**: 0.0702 (5.3% above average)
- **hopelessness_density_delta**: -0.0044 (39250.3% below average)

### 2024-W36 (FLAGGED, probability: 0.28)
- **avg_word_count**: 46.8983 (0.6% below average)
- **avg_flesch_kincaid_roll2w**: 4.6741 (0.1% below average)
- **first_person_singular_ratio**: 0.0708 (4.8% below average)
- **pct_negative_roll4w**: 0.0779 (16.8% above average)
- **hopelessness_density_delta**: 0.0027 (24247.5% above average)

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