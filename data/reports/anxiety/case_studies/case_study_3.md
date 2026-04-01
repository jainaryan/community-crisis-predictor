# Case Study: High-Distress Signal Week 2019-W34
**Week starting:** 2019-08-19
**Distress score:** 0.348

## What Happened
The community distress score spiked to 0.348, 
exceeding the severe community distress threshold.

## Early Warning Signals

### 2019-W31 (FLAGGED, probability: 0.08)
- **new_poster_ratio_roll4w**: 0.8821 (11.3% above average)
- **unique_posters_delta**: 181.0000 (11033.9% above average)
- **first_person_plural_ratio_roll4w**: 0.0016 (8.6% below average)
- **pct_negative_delta**: -0.0166 (25829.4% below average)
- **std_word_count_delta**: -32.4852 (7969.5% below average)

### 2019-W32 (not flagged, probability: 0.75)
- **new_poster_ratio_roll4w**: 0.8907 (12.4% above average)
- **unique_posters_delta**: -35.0000 (2014.3% below average)
- **first_person_plural_ratio_roll4w**: 0.0017 (2.6% below average)
- **pct_negative_delta**: 0.0128 (20146.2% above average)
- **std_word_count_delta**: 11.0631 (2580.0% above average)

### 2019-W33 (not flagged, probability: 0.66)
- **new_poster_ratio_roll4w**: 0.8989 (13.4% above average)
- **unique_posters_delta**: 94.0000 (5778.4% above average)
- **first_person_plural_ratio_roll4w**: 0.0018 (3.0% above average)
- **pct_negative_delta**: 0.0103 (16222.2% above average)
- **std_word_count_delta**: 15.6403 (3688.8% above average)

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