# Case Study: High-Distress Signal Week 2020-W25
**Week starting:** 2020-06-15
**Distress score:** 0.430

## What Happened
The community distress score spiked to 0.430, 
exceeding the severe community distress threshold.

## Early Warning Signals

### 2020-W22 (FLAGGED, probability: 0.76)
- **suicidality_total**: 190.0000 (29.9% above average)
- **unique_posters**: 858.0000 (66.2% above average)
- **economic_stress_total**: 78.0000 (70.7% above average)
- **avg_flesch_kincaid_roll4w**: 8.6759 (7.5% above average)
- **avg_flesch_kincaid_delta**: 0.1483 (2188.1% above average)

### 2020-W23 (FLAGGED, probability: 0.80)
- **suicidality_total**: 241.0000 (64.8% above average)
- **unique_posters**: 807.0000 (56.3% above average)
- **economic_stress_total**: 56.0000 (22.5% above average)
- **avg_flesch_kincaid_roll4w**: 8.6744 (7.5% above average)
- **avg_flesch_kincaid_delta**: -0.0098 (251.5% below average)

### 2020-W24 (FLAGGED, probability: 0.84)
- **suicidality_total**: 198.0000 (35.4% above average)
- **unique_posters**: 785.0000 (52.1% above average)
- **economic_stress_total**: 51.0000 (11.6% above average)
- **avg_flesch_kincaid_roll4w**: 8.6202 (6.8% above average)
- **avg_flesch_kincaid_delta**: -0.2013 (3207.0% below average)

## Top Contributing Features (SHAP)

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | suicidality_total | 1.5556 |
| 2 | unique_posters | 0.7846 |
| 3 | economic_stress_total | 0.4926 |
| 4 | avg_flesch_kincaid_roll4w | 0.4577 |
| 5 | avg_flesch_kincaid_delta | 0.3920 |
| 6 | domestic_stress_total_roll2w | 0.3128 |
| 7 | week_cos | 0.3027 |
| 8 | avg_char_count_roll4w | 0.2586 |
| 9 | topic_entropy_delta | 0.2374 |
| 10 | new_poster_ratio | 0.2133 |

## Summary

The early warning system detected precursor signals 3 weeks before this high-distress event. Key indicators included changes in suicidality_total, unique_posters, economic_stress_total.