# Case Study: High-Distress Signal Week 2019-W26
**Week starting:** 2019-06-25
**Distress score:** -0.374

## What Happened
The community distress score spiked to -0.374, 
exceeding the severe community distress threshold.

## Early Warning Signals

### 2019-W23 (FLAGGED, probability: 0.42)
- **new_poster_ratio_roll4w**: 0.8678 (9.5% above average)
- **unique_posters_delta**: 12.0000 (824.9% above average)
- **first_person_plural_ratio_roll4w**: 0.0013 (24.3% below average)
- **pct_negative_delta**: 0.0082 (12928.1% above average)
- **std_word_count_delta**: -1.5371 (472.4% below average)

### 2019-W24 (FLAGGED, probability: 0.24)
- **new_poster_ratio_roll4w**: 0.8715 (9.9% above average)
- **unique_posters_delta**: -234.0000 (14035.5% below average)
- **first_person_plural_ratio_roll4w**: 0.0012 (27.5% below average)
- **pct_negative_delta**: -0.0006 (903.0% below average)
- **std_word_count_delta**: -29.4596 (7236.5% below average)

### 2019-W25 (FLAGGED, probability: 0.40)
- **new_poster_ratio_roll4w**: 0.8922 (12.6% above average)
- **unique_posters_delta**: 116.0000 (7107.3% above average)
- **first_person_plural_ratio_roll4w**: 0.0013 (26.4% below average)
- **pct_negative_delta**: -0.0196 (30513.2% below average)
- **std_word_count_delta**: 57.4319 (13812.8% above average)

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