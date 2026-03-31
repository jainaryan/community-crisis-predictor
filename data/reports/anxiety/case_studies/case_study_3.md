# Case Study: High-Distress Signal Week 2019-W38
**Week starting:** 2019-09-17
**Distress score:** 0.849

## What Happened
The community distress score spiked to 0.849, 
exceeding the severe community distress threshold.

## Early Warning Signals

### 2019-W35 (FLAGGED, probability: 0.10)
- **new_poster_ratio_roll4w**: 0.9013 (13.7% above average)
- **first_person_plural_ratio_roll4w**: 0.0017 (0.1% below average)
- **unique_posters_delta**: -124.0000 (7390.6% below average)
- **std_word_count_delta**: 9.3449 (2163.8% above average)
- **posting_time_entropy**: 0.0000 (100.0% below average)

### 2019-W36 (FLAGGED, probability: 0.03)
- **new_poster_ratio_roll4w**: 0.9076 (14.5% above average)
- **first_person_plural_ratio_roll4w**: 0.0016 (5.4% below average)
- **unique_posters_delta**: 37.0000 (2335.1% above average)
- **std_word_count_delta**: -24.7708 (6100.7% below average)
- **posting_time_entropy**: 0.0000 (100.0% below average)

### 2019-W37 (FLAGGED, probability: 0.05)
- **new_poster_ratio_roll4w**: 0.9189 (15.9% above average)
- **first_person_plural_ratio_roll4w**: 0.0017 (4.2% below average)
- **unique_posters_delta**: 190.0000 (11577.6% above average)
- **std_word_count_delta**: 34.8296 (8337.4% above average)
- **posting_time_entropy**: 0.0000 (100.0% below average)

## Top Contributing Features (SHAP)

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | new_poster_ratio_roll4w | 1.0200 |
| 2 | first_person_plural_ratio_roll4w | 0.5834 |
| 3 | unique_posters_delta | 0.5428 |
| 4 | std_word_count_delta | 0.4343 |
| 5 | posting_time_entropy | 0.4071 |
| 6 | pct_negative_delta | 0.3678 |
| 7 | topic_shift_jsd_4w_roll4w | 0.2695 |
| 8 | avg_word_count_roll2w | 0.2494 |
| 9 | pct_neutral | 0.2323 |
| 10 | avg_positive | 0.2099 |

## Summary

The early warning system detected precursor signals 3 weeks before this high-distress event. Key indicators included changes in new_poster_ratio_roll4w, first_person_plural_ratio_roll4w, unique_posters_delta.