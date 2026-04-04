# Case Study: High-Distress Signal Week 2019-W33
**Week starting:** 2019-08-12
**Distress score:** 0.487

## What Happened
The community distress score spiked to 0.487, 
exceeding the severe community distress threshold.

## Early Warning Signals

### 2019-W30 (not flagged, probability: 0.42)
- **help_seeking_density_roll4w**: 0.0064 (15.8% above average)
- **distress_density_roll2w**: 0.0104 (6.6% above average)
- **avg_positive_delta**: 0.0047 (116958.9% above average)
- **topic_shift_jsd**: 0.2059 (68.0% above average)
- **topic_entropy_roll4w**: 0.5827 (3.5% above average)

### 2019-W31 (not flagged, probability: 0.20)
- **help_seeking_density_roll4w**: 0.0066 (19.1% above average)
- **distress_density_roll2w**: 0.0104 (6.6% above average)
- **avg_positive_delta**: -0.0040 (99249.5% below average)
- **topic_shift_jsd**: 0.1384 (13.0% above average)
- **topic_entropy_roll4w**: 0.5835 (3.7% above average)

### 2019-W32 (not flagged, probability: 0.15)
- **help_seeking_density_roll4w**: 0.0064 (15.3% above average)
- **distress_density_roll2w**: 0.0105 (7.8% above average)
- **avg_positive_delta**: -0.0026 (64869.1% below average)
- **topic_shift_jsd**: 0.0914 (25.4% below average)
- **topic_entropy_roll4w**: 0.5906 (5.0% above average)

## Top Contributing Features (SHAP)

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | help_seeking_density_roll4w | 1.4533 |
| 2 | distress_density_roll2w | 1.3232 |
| 3 | avg_positive_delta | 0.6226 |
| 4 | topic_shift_jsd | 0.5297 |
| 5 | topic_entropy_roll4w | 0.3558 |
| 6 | help_seeking_density_roll2w | 0.3258 |
| 7 | new_poster_ratio_delta | 0.2932 |
| 8 | suicidality_density_delta | 0.2805 |
| 9 | avg_neutral | 0.2565 |
| 10 | isolation_density_roll2w | 0.2182 |

## Summary

The early warning system detected precursor signals 3 weeks before this high-distress event. Key indicators included changes in help_seeking_density_roll4w, distress_density_roll2w, avg_positive_delta.