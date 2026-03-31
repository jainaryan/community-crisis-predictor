# Case Study: High-Distress Signal Week 2019-W33
**Week starting:** 2019-08-12
**Distress score:** 1.088

## What Happened
The community distress score spiked to 1.088, 
exceeding the severe community distress threshold.

## Early Warning Signals

### 2019-W30 (not flagged, probability: 0.51)
- **new_poster_ratio_roll4w**: 0.8658 (9.2% above average)
- **first_person_plural_ratio_roll4w**: 0.0015 (14.5% below average)
- **unique_posters_delta**: -54.0000 (3162.0% below average)
- **std_word_count_delta**: 25.1630 (5995.7% above average)
- **posting_time_entropy**: 0.0000 (100.0% below average)

### 2019-W31 (not flagged, probability: 0.44)
- **new_poster_ratio_roll4w**: 0.8821 (11.3% above average)
- **first_person_plural_ratio_roll4w**: 0.0016 (8.6% below average)
- **unique_posters_delta**: 181.0000 (11033.9% above average)
- **std_word_count_delta**: -32.4852 (7969.5% below average)
- **posting_time_entropy**: 0.0000 (100.0% below average)

### 2019-W32 (FLAGGED, probability: 0.31)
- **new_poster_ratio_roll4w**: 0.8907 (12.4% above average)
- **first_person_plural_ratio_roll4w**: 0.0017 (2.6% below average)
- **unique_posters_delta**: -35.0000 (2014.3% below average)
- **std_word_count_delta**: 11.0631 (2580.0% above average)
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