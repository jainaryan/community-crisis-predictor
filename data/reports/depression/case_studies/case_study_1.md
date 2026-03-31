# Case Study: High-Distress Signal Week 2019-W41
**Week starting:** 2019-10-08
**Distress score:** 0.465

## What Happened
The community distress score spiked to 0.465, 
exceeding the severe community distress threshold.

## Early Warning Signals

### 2019-W34 (not flagged, probability: 0.65)
- **avg_char_count**: 865.6320 (9.2% below average)
- **hopelessness_density_roll2w**: 0.0023 (7.1% above average)
- **avg_neutral_delta**: -0.0055 (11623.3% below average)
- **std_word_count_roll2w**: 153.3785 (25.9% below average)
- **avg_flesch_kincaid**: 8.0064 (2.1% above average)

### 2019-W35 (not flagged, probability: 0.69)
- **avg_char_count**: 870.3349 (8.7% below average)
- **hopelessness_density_roll2w**: 0.0022 (1.5% above average)
- **avg_neutral_delta**: 0.0053 (11006.3% above average)
- **std_word_count_roll2w**: 161.6994 (21.9% below average)
- **avg_flesch_kincaid**: 7.8190 (0.3% below average)

### 2019-W38 (not flagged, probability: 0.55)
- **avg_char_count**: 947.1669 (0.6% below average)
- **hopelessness_density_roll2w**: 0.0020 (4.4% below average)
- **avg_neutral_delta**: 0.0021 (4276.5% above average)
- **std_word_count_roll2w**: 245.7359 (18.7% above average)
- **avg_flesch_kincaid**: 11.5230 (46.9% above average)

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