# Case Study: High-Distress Signal Week 2019-W26
**Week starting:** 2019-06-25
**Distress score:** -0.374

## What Happened
The community distress score spiked to -0.374, 
exceeding the severe community distress threshold.

## Early Warning Signals

### 2019-W23 (FLAGGED, probability: 0.29)
- **new_poster_ratio_roll4w**: 0.8678 (9.5% above average)
- **first_person_plural_ratio_roll4w**: 0.0013 (24.3% below average)
- **unique_posters_delta**: 12.0000 (824.9% above average)
- **std_word_count_delta**: -1.5371 (472.4% below average)
- **posting_time_entropy**: 0.0000 (100.0% below average)

### 2019-W24 (FLAGGED, probability: 0.27)
- **new_poster_ratio_roll4w**: 0.8715 (9.9% above average)
- **first_person_plural_ratio_roll4w**: 0.0012 (27.5% below average)
- **unique_posters_delta**: -234.0000 (14035.5% below average)
- **std_word_count_delta**: -29.4596 (7236.5% below average)
- **posting_time_entropy**: 0.0000 (100.0% below average)

### 2019-W25 (FLAGGED, probability: 0.31)
- **new_poster_ratio_roll4w**: 0.8922 (12.6% above average)
- **first_person_plural_ratio_roll4w**: 0.0013 (26.4% below average)
- **unique_posters_delta**: 116.0000 (7107.3% above average)
- **std_word_count_delta**: 57.4319 (13812.8% above average)
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