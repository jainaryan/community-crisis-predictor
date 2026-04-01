# Case Study: High-Distress Signal Week 2019-W31
**Week starting:** 2019-08-01
**Distress score:** 0.300

## What Happened
The community distress score spiked to 0.300, 
exceeding the severe community distress threshold.

## Early Warning Signals

### 2019-W28 (FLAGGED, probability: 0.33)
- **new_poster_ratio_roll4w**: 0.8734 (10.2% above average)
- **unique_posters_delta**: -182.0000 (10894.3% below average)
- **first_person_plural_ratio_roll4w**: 0.0016 (6.5% below average)
- **pct_negative_delta**: 0.0090 (14235.7% above average)
- **std_word_count_delta**: -29.0929 (7147.7% below average)

### 2019-W29 (FLAGGED, probability: 0.08)
- **new_poster_ratio_roll4w**: 0.8608 (8.6% above average)
- **unique_posters_delta**: -235.0000 (14095.9% below average)
- **first_person_plural_ratio_roll4w**: 0.0015 (11.2% below average)
- **pct_negative_delta**: 0.0260 (40815.2% above average)
- **std_word_count_delta**: 4.8881 (1084.1% above average)

### 2019-W30 (not flagged, probability: 0.71)
- **new_poster_ratio_roll4w**: 0.8658 (9.2% above average)
- **unique_posters_delta**: -54.0000 (3162.0% below average)
- **first_person_plural_ratio_roll4w**: 0.0015 (14.5% below average)
- **pct_negative_delta**: -0.0310 (48433.7% below average)
- **std_word_count_delta**: 25.1630 (5995.7% above average)

## Top Contributing Features (SHAP)

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | new_poster_ratio_roll4w | 1.3090 |
| 2 | unique_posters_delta | 0.6189 |
| 3 | first_person_plural_ratio_roll4w | 0.6015 |
| 4 | pct_negative_delta | 0.5829 |
| 5 | std_word_count_delta | 0.4728 |
| 6 | avg_word_count_roll2w | 0.3977 |
| 7 | posting_time_entropy | 0.3633 |
| 8 | distress_density_roll2w | 0.2968 |
| 9 | avg_positive | 0.2821 |
| 10 | help_seeking_density_roll4w | 0.2151 |

## Summary

The early warning system detected precursor signals 3 weeks before this high-distress event. Key indicators included changes in new_poster_ratio_roll4w, unique_posters_delta, first_person_plural_ratio_roll4w.