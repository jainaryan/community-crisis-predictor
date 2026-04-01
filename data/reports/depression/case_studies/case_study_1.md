# Case Study: High-Distress Signal Week 2020-W12
**Week starting:** 2020-03-16
**Distress score:** 0.820

## What Happened
The community distress score spiked to 0.820, 
exceeding the severe community distress threshold.

## Early Warning Signals

### 2020-W09 (not flagged, probability: 0.58)
- **avg_char_count**: 930.0462 (2.4% below average)
- **unique_posters_delta**: -188.0000 (1836.8% below average)
- **avg_neutral_delta**: 0.0017 (3505.3% above average)
- **std_word_count_roll2w**: 179.2295 (13.4% below average)
- **avg_flesch_kincaid**: 8.2400 (5.0% above average)

### 2020-W10 (not flagged, probability: 0.54)
- **avg_char_count**: 945.5040 (0.8% below average)
- **unique_posters_delta**: -21.0000 (116.3% below average)
- **avg_neutral_delta**: 0.0008 (1508.9% above average)
- **std_word_count_roll2w**: 170.1932 (17.8% below average)
- **avg_flesch_kincaid**: 7.8394 (0.1% below average)

### 2020-W11 (not flagged, probability: 0.49)
- **avg_char_count**: 956.7783 (0.4% above average)
- **unique_posters_delta**: -288.0000 (2867.0% below average)
- **avg_neutral_delta**: -0.0009 (1942.4% below average)
- **std_word_count_roll2w**: 187.7450 (9.3% below average)
- **avg_flesch_kincaid**: 8.0584 (2.7% above average)

## Top Contributing Features (SHAP)

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | avg_char_count | 0.6258 |
| 2 | unique_posters_delta | 0.5391 |
| 3 | avg_neutral_delta | 0.5360 |
| 4 | std_word_count_roll2w | 0.5251 |
| 5 | avg_flesch_kincaid | 0.5096 |
| 6 | pct_neutral_delta | 0.4630 |
| 7 | avg_neutral | 0.3197 |
| 8 | avg_word_count_delta | 0.2699 |
| 9 | avg_positive_delta | 0.2464 |
| 10 | hopelessness_density_roll2w | 0.2265 |

## Summary

The early warning system detected precursor signals 3 weeks before this high-distress event. Key indicators included changes in avg_char_count, unique_posters_delta, avg_neutral_delta.