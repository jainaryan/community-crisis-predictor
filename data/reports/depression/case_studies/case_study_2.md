# Case Study: High-Distress Signal Week 2020-W31
**Week starting:** 2020-07-27
**Distress score:** -0.289

## What Happened
The community distress score spiked to -0.289, 
exceeding the severe community distress threshold.

## Early Warning Signals

### 2020-W28 (not flagged, probability: 0.37)
- **avg_char_count**: 940.7171 (1.3% below average)
- **hopelessness_density_roll2w**: 0.0021 (3.4% below average)
- **avg_neutral_delta**: 0.0028 (5760.9% above average)
- **std_word_count_roll2w**: 198.2973 (4.2% below average)
- **avg_flesch_kincaid**: 7.8405 (0.0% below average)

### 2020-W29 (not flagged, probability: 0.43)
- **avg_char_count**: 908.1683 (4.7% below average)
- **hopelessness_density_roll2w**: 0.0022 (2.8% above average)
- **avg_neutral_delta**: -0.0023 (4813.0% below average)
- **std_word_count_roll2w**: 198.5018 (4.1% below average)
- **avg_flesch_kincaid**: 8.1728 (4.2% above average)

### 2020-W30 (not flagged, probability: 0.31)
- **avg_char_count**: 941.1877 (1.3% below average)
- **hopelessness_density_roll2w**: 0.0022 (2.1% above average)
- **avg_neutral_delta**: 0.0038 (7932.3% above average)
- **std_word_count_roll2w**: 222.2437 (7.3% above average)
- **avg_flesch_kincaid**: 8.4852 (8.2% above average)

## Top Contributing Features (SHAP)

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | avg_char_count | 0.6284 |
| 2 | hopelessness_density_roll2w | 0.5757 |
| 3 | avg_neutral_delta | 0.5075 |
| 4 | std_word_count_roll2w | 0.4915 |
| 5 | avg_flesch_kincaid | 0.3778 |
| 6 | unique_posters_delta | 0.3665 |
| 7 | pct_neutral_delta | 0.3584 |
| 8 | avg_neutral | 0.3247 |
| 9 | first_person_plural_ratio | 0.2523 |
| 10 | topic_shift_jsd_4w_roll2w | 0.2386 |

## Summary

The early warning system detected precursor signals 3 weeks before this high-distress event. Key indicators included changes in avg_char_count, hopelessness_density_roll2w, avg_neutral_delta.