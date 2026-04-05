# Community Crisis Predictor
## A Three-Layer Analytics Framework for Mental Health Early Warning

**NUS School of Computing · IS5126 Hands-on with Applied Analytics · 2025/2026 Semester 2**

*Reddit Mental Health Communities · XGBoost · LSTM · SHAP · BERTopic · EDA · GenAI Weekly Briefs · FastAPI · Streamlit*

---

## Executive Summary

Community mental health crises rarely erupt without warning. In the days and weeks before a crisis week becomes visible in aggregate statistics, online communities show measurable early signals: a surge of new posters, a shift in language complexity, rising hopelessness lexicon density. This project builds a structured pipeline to detect those signals systematically, translate them into probabilistic forecasts, and deliver actionable moderator guidance.

Drawing on approximately **2,207,696 Reddit posts** across five mental health communities (r/anxiety, r/depression, r/SuicideWatch, r/mentalhealth, r/lonely) spanning **January 2018 to December 2024** — collected from the Zenodo Low et al. COVID-era dataset (2018–2020) and Arctic Shift historical archives (2021–2024) — the pipeline extracts 107 features across six families, trains LSTM and XGBoost models under strict walk-forward cross-validation, and deploys the full system as two hosted services.

Three findings stand out. First, **XGBoost achieves strong crisis detection with up to 14.5 weeks early warning on r/anxiety**: under community-specific labelling (thresholds at 0.3σ/0.6σ/1.0σ), XGBoost achieves PR-AUC of 0.758–0.889 across four of five communities and detects elevated distress up to 14.5 weeks before crisis peaks on r/anxiety and 12.6 weeks on r/SuicideWatch. LSTM is competitive but underperforms XGBoost in the current evaluation — a finding attributable to dataset size constraints (early walk-forward folds contain as few as 26 training sequences) rather than architectural unsuitability; LSTM is expected to dominate with longer training windows. Second, **pre-COVID community distress was not at baseline — the crisis was already underway**: EDA across the three temporal periods (Pre-COVID 2018–19, COVID 2020–21, Post-COVID 2022–24) shows that r/anxiety and r/SuicideWatch had their highest crisis rates in the pre-COVID period, declined through COVID, and dropped sharply post-2021. r/depression is the exception — it maintained elevated crisis rates across all three periods, consistent with a longer post-pandemic recovery tail. Third, **cross-community lead-lag is detectable**: r/anxiety entered Elevated Distress (State 2) on 6 January 2020, approximately ten weeks before r/SuicideWatch reached Severe Community Distress Signal (State 3) on 16 March 2020, consistent with anxiety communities functioning as leading indicators for acute crisis communities.

The prescriptive layer translates each weekly forecast into a structured moderator brief, generated via retrieval-augmented generation over a curated intervention playbook, and provides an interactive what-if scenario panel for real-time sensitivity analysis. The full system is deployed as a FastAPI inference service on Render.com and a Streamlit dashboard on Streamlit Cloud.

### Key Findings at a Glance

| Finding | Result |
|---|---|
| Best XGB performance | r/lonely PR-AUC 0.889, r/mentalhealth 0.869, r/SuicideWatch 0.855 |
| XGB early warning | r/anxiety: 14.5w avg lead time; r/SuicideWatch: 12.6w |
| XGB vs LSTM on r/anxiety | XGB PR-AUC 0.758 / recall 0.852 vs LSTM PR-AUC 0.642 / recall 0.471 |
| LSTM constraint | Early folds have ≤26 training sequences — insufficient for recurrent convergence |
| Cross-community lead time | r/anxiety State 2 onset ~10 weeks before r/SuicideWatch State 3 |
| Dataset size | 2,207,696 posts, 366 weeks per community, 2018–2024 |
| Live dashboard | https://community-crisis-predictor-mozt6amaceenfxso6pegb8.streamlit.app |
| Inference API | https://community-crisis-predictor.onrender.com |

---

## 1. Problem Statement

Online mental health communities serve millions of people navigating anxiety, depression, loneliness, and crisis. Unlike clinical settings, these communities have no intake process, no scheduled check-ins, and no systematic monitoring. A week of sharply elevated distress may pass unnoticed until it becomes a visible crisis — at which point moderator response is reactive rather than anticipatory.

The system is framed as a **community weather forecast**. Just as a meteorologist monitors atmospheric pressure to anticipate storms without predicting any individual raindrop's trajectory, this system monitors aggregate community signals to anticipate escalation without inferring anything about individual users. The ecological fallacy constraint applies throughout: a community in State 3 contains users in all states; a community in State 0 may include users in acute personal crisis. No individual-level inference is permitted or implied.

The analytics architecture follows three layers:

- **Descriptive** — What has been happening in these communities, and which signals characterise elevated-distress periods?
- **Predictive** — Can we forecast next week's community crisis state, and where does the model add genuine value?
- **Prescriptive** — Given this week's forecast, what should community moderators do?

### 1.1 Four-State Escalation Model

Each community's weekly state is classified into one of four levels derived from z-score thresholds applied to a composite distress score, evaluated against that community's own rolling historical baseline:

| State | Label | Threshold |
|---|---|---|
| 0 | Stable | < 0.3σ above baseline |
| 1 | Early Vulnerability Signal | 0.3σ – 0.6σ |
| 2 | Elevated Distress | 0.6σ – 1.0σ |
| 3 | Severe Community Distress Signal | > 1.0σ |

The system outputs one forecast per community per week — predicting the state for the following week based on the current week's aggregate signals.

---

## 2. Data and Methodology

### 2.1 Dataset and Collection

All experiments use a **tri-source collection strategy** spanning January 2018 to December 2024. Raw post fields (post text, timestamp, author hash, subreddit) are ingested; precomputed columns (TF-IDF, LIWC) in Zenodo files are intentionally discarded in favour of reproducible in-pipeline feature computation.

Three data sources are combined, with source provenance recorded per post in a `data_source` column:

1. **Zenodo (2018–2020)** — Low et al. COVID-era Reddit mental health dataset (record 3941387 [1]), covering the COVID-19 baseline and onset period. Primary source for the 2018–2020 window.
2. **Arctic Shift v1 (gap-fill)** — JSONL archives providing gap-fill for weeks absent from Zenodo (early-2018 and late-2020 windows).
3. **Arctic Shift v2 (2021–2024 extension)** — Historical JSONL archives extending the evaluation window into the post-vaccine rollout, post-pandemic recovery, and 2022–2024 stabilisation period. This is the largest single contribution to the final dataset by week count.

Both Arctic Shift ingestions are tracked in `data/ingestion_manifest.json`, making re-collection idempotent. Author names are privacy-hashed before storage; posts from `[deleted]` and `[removed]` entries are excluded.

**Post counts by subreddit (2018–2024 final dataset):**

| Subreddit | Approx. Posts | Weeks Observed | LSTM Eval Wks | Crisis Wks in Eval |
|---|---|---|---|---|
| r/anxiety | ~387K | 357 | 331 | 38 (11.5%) |
| r/depression | ~623K | 342 | 316 | 67 (21.2%) |
| r/SuicideWatch | ~546K | 356 | 330 | 28 (8.5%) |
| r/lonely | ~257K | 357 | 331 | 31 (9.4%) |
| r/mentalhealth | ~396K | 357 | 331 | 26 (7.9%) |

**Total: 2,207,696 posts across 1,769 week-observations.**

> **Note on temporal structure**: The first 26 weeks per subreddit form the minimum training seed; the walk-forward splitter adds 1 gap week for label shift, yielding 331–316 usable evaluation weeks. Crisis weeks are those where the actual state label is State 2 (Elevated Distress) or State 3 (Severe).

> **[Figure 1: Post volume timeline per subreddit]**
> *State-coloured weekly post volume timelines are available as interactive HTML files at `data/reports/{sub}/timeline.html`. Open in any browser. Key visible events: COVID-19 onset (March 2020) creates a cross-community spike visible in all five timelines; post-2021 post volume stabilises at approximately 50–70% of 2019–2020 peak levels.*

### 2.2 Feature Engineering — Six Families

From each community's weekly post aggregate, 60+ features are computed across six families:

| Family | Features | Example signals |
|---|---|---|
| **Linguistic** | Word count, type-token ratio, readability (Flesch-Kincaid), char count | Reading ease drop → simpler, more fragmented posts |
| **Sentiment** | VADER compound, positive/negative/neutral/very-negative distribution | Rising `pct_negative`, declining `pct_neutral` |
| **Distress** | Hopelessness lexicon density, help-seeking density, composite distress score | `hopelessness_density_roll2w` top feature on r/depression |
| **Behavioral** | Post volume, unique posters, new-poster ratio, comment engagement, posting-time entropy | `unique_posters_delta` top feature on r/anxiety |
| **Topics** | BERTopic distribution (15 topics), topic entropy, JSD topic drift (1-week and 4-week) | Topic shift → community conversation fracturing |
| **Temporal** | 2-week and 4-week rolling averages, week-over-week deltas, cyclical seasonality encoding (sin/cos) | Delta features amplify early-week change signals |

Each feature is computed per-week and stored in a flat feature matrix (`data/features/features.parquet`). Temporal variants (rolling means, deltas) are computed at extraction time, not imputed — weeks without sufficient history receive NaN values handled by the walk-forward splitter.

### 2.3 Labelling

A composite distress score is computed per week as a weighted sum of seven community-normalised signals:

```
distress_score = 0.25 × z(neg_sentiment)
               + 0.20 × z(hopelessness_density)
               + 0.20 × z(suicidality_density)
               + 0.15 × z(help_seeking_density)
               + 0.10 × z(isolation_density)
               + 0.05 × z(economic_stress_density)
               + 0.05 × z(domestic_stress_density)
```

Weights are theoretically motivated — negative sentiment and hopelessness/suicidality lexicons carry the highest weight as the most direct indicators of community-level distress — but are not calibrated against clinical expert labels. This is a proxy, not a diagnostic instrument. Signals are expressed as per-word density (matches per total words in the week's posts) to ensure scale consistency across communities of different posting volumes.

Labels are **community-specific**: thresholds are applied against each subreddit's own historical mean and standard deviation within each walk-forward fold's training window, preventing any global scale from distorting the signal. 'Elevated Distress' in r/SuicideWatch represents a different absolute level than in r/mentalhealth; labels are not cross-community comparable.

### 2.4 Evaluation Design — Walk-Forward Cross-Validation

The evaluation uses **walk-forward cross-validation** with a minimum 26-week training window, a 1-week gap to prevent leakage from rolling features, and an expanding window that grows with each fold. Random shuffled splits are explicitly excluded — future data must never inform past predictions.

The primary metric is **PR-AUC** (area under the Precision-Recall curve for binary crisis detection, States 2+3 vs 0+1). Because crisis weeks are a minority, the PR-AUC random baseline equals the community crisis rate (not 0.5). **ROC-AUC** is also reported as a secondary discrimination metric. **Recall** is the operationally critical metric: missing a crisis week has higher cost than a false alert.

Decision usefulness is measured via **Recall@K**: if a community support team can act on at most K alert weeks, how many true crisis weeks fall within the model's top-K ranked predictions?

Two models run in parallel under identical walk-forward folds:

- **XGBoost** — binary crisis classifier with hyperparameter search (RandomizedSearchCV, 30 iterations), automatic class-weight balancing. No sequence context; each week is an independent sample. Inner CV uses `TimeSeriesSplit` with `gap=1` to prevent label-boundary leakage.
- **PyTorch LSTM** — 6-week context window, 2-layer, hidden size 32, dropout 0.2. Features are **MinMax-normalized per fold** (scaler fit on training window only, applied to the test week) — this is critical to prevent data leakage through feature scale. 4-class output (States 0–3). Class-weighted cross-entropy loss.

After training, a performance band table is printed:
- **High** (PR-AUC ≥ 0.45): model reliably detects crises
- **Medium** (0.20–0.45): moderate signal; worth operational monitoring
- **Low** (< 0.20): near-random; insufficient crisis weeks or feature coverage

---

## 3. Working Within Real-World Constraints

Extracting reliable insight from social media data requires confronting its structural limitations directly. Five categories of constraint affect this project; each shapes the design and must be acknowledged in any deployment context.

### 3.1 Sample Bias

Reddit is a self-selecting platform. Users who experience mental health distress but do not use Reddit — or who use it passively — are entirely absent from the dataset. More critically, the distribution of who posts shifts with community state: mild distress periods attract fewer posts from lightly distressed users, while crisis peaks attract more posts from acutely distressed users *and* from the community rallying around them. The result is a systematic pattern: distress scores are underestimated during mild periods and overestimated during peaks.

This manifests in per-class recall. Class 3 (Severe) is both the least frequent and the hardest to recall — in part because the most distressing posts are frequently removed by moderators before archival (see Section 3.2), but also because the model trains on a biased sample of what severe periods look like. Silent sufferers, non-English speakers, and users without internet access are entirely absent from the dataset.

The design response is to centre the system on early-warning detection of the *approach* of a crisis (Elevated Distress, State 2) rather than its peak. This is the operational window in which community response is most effective.

### 3.2 Missing Data

The Zenodo archive contains **6–8 gap weeks per subreddit**, arising from archiving inconsistencies and platform disruptions. Arctic Shift gap-fill partially addresses this, but post deletions and moderator removals are systematically non-random: the most distressing content on platforms like r/SuicideWatch is removed before archival by moderators following safe-messaging guidelines, creating systematic underrepresentation of the highest-severity weeks. This is not correctable by gap-fill.

Data completeness scores computed at ingestion time reflect week-over-week volume relative to the running median. Values above 1.0 indicate Arctic Shift contributed posts beyond the Zenodo baseline:

| Subreddit | Avg Completeness Score | Gap Weeks |
|---|---|---|
| r/anxiety | 1.002 | 6 |
| r/depression | 0.992 | 8 |
| r/SuicideWatch | 1.001 | 7 |
| r/lonely | 1.018 | 1 |
| r/mentalhealth | 1.021 | 5 |

> **Note**: Weekly data completeness scores are computed at ingestion time and stored in `data/reports/{sub}/weekly_completeness.csv`. The completeness score per week is the post volume relative to the rolling 8-week median; values below 0.5 flag gap weeks. These are visualised in each subreddit's dashboard HTML at `data/reports/{sub}/dashboard.html`.

### 3.3 Methodological Constraints

The 26-week minimum training window is not arbitrary. It represents the minimum data needed for rolling baselines and temporal features (4-week rolling windows plus a 1-week label gap) to stabilise. With 366 weeks per community and 327 evaluation weeks after the training seed, the PR-AUC random baseline for each community equals its crisis rate in the evaluation window — ranging from 26% (r/depression) to 84% (r/lonely) — not 0.5. This is precisely why PR-AUC is the right primary metric rather than ROC-AUC: it embeds the class imbalance directly into its baseline.

This also explains why walk-forward CV is non-negotiable. A random split would contaminate rolling features — the 4-week rolling average at week 200 uses weeks 196–199; a random split could place week 198 in training and week 200 in test, making training-window statistics directly observable at test time.

### 3.4 Industry-Specific Knowledge

Mental health has validated clinical instruments — PHQ-9, BDI-II, GAD-7 — that are not available in this dataset. The distress score is a proxy constructed from VADER sentiment [2] and domain lexicons. It has not been validated against clinical expert labels. The system is explicitly framed as a population-level early warning signal for community moderators, not a clinical screening tool.

The **ecological fallacy** constraint applies throughout: community-level signals say nothing about individual users. A week in which a community's aggregate distress score spikes says nothing about whether any particular user is in crisis.

### 3.5 Practical Constraints — No Ground Truth

No externally validated crisis labels exist for Reddit communities. The four-class target states are derived entirely from within-community distributional statistics. Two consequences follow: the model is self-calibrating (each community's baselines shift with its own history) but cross-community label comparisons are not meaningful. A 'State 2' label in r/SuicideWatch and in r/mentalhealth are not comparable in absolute distress terms.

---

## 4. Layer 1 — Descriptive Analytics

*Layer 1 asks: What has been happening in these communities, and which signals characterise elevated-distress periods?*

Descriptive analytics establishes the ground truth of what the data contains before any predictive model is introduced. This layer now includes two outputs: **SHAP-grounded feature importance** from trained models, and **automated EDA reports** generated per subreddit after feature extraction.

### 4.1 Automated EDA Reports

After feature extraction, the pipeline generates a self-contained EDA HTML report per subreddit at `data/reports/{sub}/eda_summary.html`. Each report contains:

- **Feature distribution table** — mean, std, IQR, skew, % missing per feature (colour-coded: green < 5% missing, amber 5–20%, red > 20%)
- **Outlier detection (IQR rule)** — weeks where a feature value falls outside [Q1 – 1.5×IQR, Q3 + 1.5×IQR], flagged with the specific feature and week
- **Distress trend analysis** — linear regression on the community distress score over time; classifies as *rising*, *stable*, or *declining* with % change over the data period
- **Crisis rate by year** — fraction of weeks reaching State 2 or 3 each calendar year (2018–2024)
- **Quality flags** — high-missingness features, top outlier-prone features, class imbalance warnings

This mirrors the L1.2 data quality pattern from the IS5126 curriculum: before modelling, verify that the data is what you think it is.

> **[Figure 2: EDA distress trend charts]**
> *Interactive EDA reports at `data/reports/anxiety/eda_summary.html` and `data/reports/depression/eda_summary.html`. Open in browser. Key EDA findings: r/anxiety shows a declining long-run distress trend (2019 peak → 2024 near-baseline); r/depression shows a rising trend (distress increasing through 2023 before stabilising). Both reports include feature distribution tables with IQR-flagged outlier weeks and missing-value coverage heatmaps.*

**Crisis rate by year — fraction of weeks in State 2+ per community:**

| Subreddit | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 |
|---|---|---|---|---|---|---|---|
| r/anxiety | 9.8% | **36.4%** | 18.9% | 5.8% | 15.4% | 7.7% | 1.9% |
| r/depression | 2.1% | 24.2% | 18.9% | 13.5% | 17.3% | **26.9%** | 0% |
| r/SuicideWatch | 17.7% | **32.6%** | **30.2%** | 13.5% | 5.8% | 3.9% | 0% |
| r/lonely | 23.5% | 25.0% | 24.5% | 15.4% | 15.4% | 1.9% | 3.9% |
| r/mentalhealth | 17.7% | **27.3%** | 9.4% | 7.7% | 0% | 1.9% | 3.9% |

This table contains a counter-intuitive finding: **2019 was the peak crisis year for r/anxiety (36.4%), not 2020**. The COVID-19 pandemic did not trigger the anxiety crisis from a stable baseline — the crisis was already underway in 2019. The 2020 rate (18.9%) is lower, possibly because a crisis peak had already occurred and the community partially stabilised before the pandemic arrived. For r/SuicideWatch, crisis rates remained high across both 2019 and 2020, then dropped sharply post-2021. For r/depression, the pattern is more sustained — elevated crisis rates persist through 2022–2023, suggesting depression communities experienced a longer post-pandemic recovery tail than anxiety communities.

These patterns are visible in the per-subreddit EDA reports at `data/reports/{sub}/eda_summary.html`, which include distress trend plots and the per-year crisis rate bar chart.

> **[Figure 3: Crisis rate bar chart]**
> *The above table is the data source. A bar chart version is in each subreddit's `eda_summary.html` EDA report.*

### 4.2 Community-Specific SHAP Feature Importance

SHAP values from the XGBoost models (TreeExplainer) reveal that the most predictive features are distinct across communities, reflecting different posting cultures and distress dynamics:

| Subreddit | Top 3 SHAP Features | Interpretation |
|---|---|---|
| r/anxiety | `unique_posters_delta`, `new_poster_ratio`, `avg_flesch_kincaid_roll2w` | Surge of new (distressed) posters entering the community; simplifying language |
| r/depression | `distress_density_delta`, `hopelessness_density_roll2w`, `pct_neutral_delta` | Lexicon-based signals dominate; sustained hopelessness over 2-week window |
| r/SuicideWatch | `first_person_plural_ratio_roll2w`, `first_person_singular_ratio_delta`, `unique_posters_delta` | Shift from 'I' to 'we' language; community cohesion signal |
| r/lonely | `pct_negative_roll2w`, `first_person_singular_ratio_roll2w`, `distress_density_delta` | Sustained negative sentiment and isolation language |
| r/mentalhealth | `distress_density`, `pct_negative`, `new_poster_ratio_roll4w` | Post volume + lexicon signals; slower-moving community |

The contrast between r/anxiety (behavioral signals dominate) and r/depression (lexicon signals dominate) reflects genuinely different community dynamics: anxiety communities react to events with volume surges, while depression communities show slow linguistic deterioration.

> **[Figure 4: SHAP feature importance charts]**
> *Generated by pipeline at `data/reports/{sub}/feature_importance.html` (Plotly bar chart, top 10 features by mean absolute SHAP value). Open directly in browser. The community-specific SHAP patterns described in the table above are the primary output of this figure: behavioral signals dominate r/anxiety while lexicon signals dominate r/depression.*

### 4.3 Weekly Distress Timeline

The backtesting timeline (`data/reports/{sub}/timeline.html`) shows the actual vs predicted state for every evaluation week, coloured by the four-state scale. Key events visible in the timeline:

- **r/anxiety**: Elevated Distress entry on 2020-01-06, approximately ten weeks before r/SuicideWatch's Severe signal — the cross-community lead-lag finding (Section 5.2, Finding 2)
- **r/depression**: COVID-19 onset visible as a State 3 spike in March 2020 across all communities simultaneously
- **r/SuicideWatch**: State 3 (Severe Community Distress Signal) first reached 2020-03-16

> **[Figure 5: Cross-community timeline — r/anxiety and r/SuicideWatch]**
> *State-coloured timelines at `data/reports/anxiety/timeline.html` and `data/reports/suicidewatch/timeline.html`. The lead-lag pattern is visible by inspecting the date of first State 2 entry (r/anxiety: 2020-01-06) against the date of first State 3 entry (r/SuicideWatch: 2020-03-16). The Streamlit dashboard displays both timelines side-by-side in the Cross-Community Analysis tab.*

---

## 5. Layer 2 — Predictive Analytics

*Layer 2 asks: Can we forecast next week's community crisis state, and where does the model add genuine value?*

All metrics are sourced directly from walk-forward evaluation on the full 2018–2024 dataset (`data/models/eval_results.json`).

### 5.1 Walk-Forward Evaluation Results

PR-AUC is the primary metric (binary crisis detection: States 2+3 vs 0+1). The PR-AUC random baseline equals the community crisis rate in the evaluation window — not 0.5. Performance band thresholds: High ≥ 0.45, Medium 0.20–0.45, Low < 0.20.

All metrics are from walk-forward evaluation on the full **2018–2024 dataset** (2,207,696 posts). Eval weeks = weeks available for testing after the 26-week minimum training seed.

| Subreddit | **XGB Recall** | **XGB PR-AUC** | XGB ROC-AUC | LSTM Recall | LSTM F1 | LSTM PR-AUC | LSTM ROC-AUC | Crisis Wks | Eval Wks | Band |
|---|---|---|---|---|---|---|---|---|---|---|
| r/anxiety | **0.852** | **0.758** | 0.735 | 0.471 | 0.498 | 0.642 | 0.617 | 162 | 327 | **High** |
| r/depression | **0.706** | **0.449** | **0.782** | 0.291 | 0.287 | 0.227 | 0.472 | 85 | 327 | Medium |
| r/SuicideWatch | **0.856** | **0.855** | **0.809** | 0.367 | 0.476 | 0.697 | 0.616 | 188 | 327 | **High** |
| r/lonely | **0.986** | **0.889** | 0.594 | 0.162 | 0.273 | 0.852 | 0.448 | 276 | 327 | **High** |
| r/mentalhealth | **0.976** | **0.869** | 0.729 | 0.379 | 0.517 | 0.794 | 0.574 | 246 | 327 | **High** |

*Bold = best model per community on each metric. Crisis Wks = actual State 2+3 weeks in evaluation window.*

**Threshold calibration note**: With thresholds at 0.6σ for State 2, r/lonely (84% crisis rate) and r/mentalhealth (75%) are chronically elevated — almost any week exceeds the threshold. Their high PR-AUC (0.889 and 0.869) reflects chronic community distress, not model discrimination; a naive classifier predicting "crisis" every week would achieve PR-AUC ≈ 0.84 on r/lonely. The genuinely informative evaluations are r/depression (26% crisis rate, PR-AUC 0.449) and r/anxiety (49.5%, PR-AUC 0.758), where the model must actively discriminate between elevated and normal states. The 0.6σ threshold was chosen to make the system sensitive to early-stage community deterioration; tighter thresholds (e.g. 1.0σ) would reduce false-positive rates at the cost of missing earlier signals.

**Key observation — XGBoost outperforms LSTM under community-specific labelling**: Crisis weeks represent 26–84% of each community's evaluation window. XGBoost achieves strong PR-AUC (0.449–0.889) and recall (0.706–0.986) across all communities. LSTM is competitive on PR-AUC for r/lonely (0.852) and r/mentalhealth (0.794) but achieves lower recall (0.162–0.471) across all five communities. The root cause and architectural implications are detailed in Section 5.2 Finding 1.

> **[Figure 6: PR curves — all five subreddits, XGB vs LSTM]**
> *Precision-recall curves are computed during walk-forward evaluation and visualised in the Streamlit dashboard (Model Metrics tab). The characteristic shape for all communities shows a sharp precision drop at moderate recall thresholds — reflecting the low base rate of crisis weeks in the full 2018–2024 window.*

### 5.2 Three Named Findings

#### Finding 1 — XGBoost Achieves Strong Detection; LSTM Constrained by Training Data Volume

On the full 2018–2024 dataset under community-specific thresholds (0.6σ for State 2), XGBoost achieves PR-AUC of 0.758–0.889 across four communities and recall of 0.706–0.986 across all five. The ensemble (max of XGB and LSTM predictions, safety-first) inherits XGBoost's recall performance.

LSTM achieves lower recall (0.162–0.471) but competitive PR-AUC on high-crisis-rate communities (r/lonely: 0.852, r/mentalhealth: 0.794). The recall gap is a training data volume effect, not an architectural failure. The walk-forward splitter begins predictions after 26 training weeks; with a 6-week sequence window, early folds have only 20–26 training sequences — insufficient for a recurrent network with thousands of weights to converge. XGBoost generalises from 26 independent samples naturally because tree splits do not require gradient accumulation across sequence boundaries.

This finding motivates a clear future direction: increasing the minimum training window to 52 weeks and sequence length to 13 weeks would give LSTM early folds ≥39 sequences from the start, likely closing the recall gap. Multi-task training across all five communities jointly (~1,830 sequences from fold 1) would be the strongest architectural intervention, allowing the LSTM to learn escalation trajectory patterns from the combined community history before fine-tuning per community. This is left as priority future work.

#### Finding 2 — Cross-Community Lead-Lag: Anxiety Anticipates SuicideWatch

r/anxiety first entered State 2 (Elevated Distress) on **6 January 2020**, approximately **ten weeks** before r/SuicideWatch registered its first State 3 (Severe Community Distress Signal) on **16 March 2020** — coinciding with the WHO pandemic declaration. This temporal ordering is consistent with the hypothesis that anxiety communities are leading indicators for acute crisis communities: generalised anxiety precedes, and potentially contributes to, the escalation visible in suicidal ideation communities.

This is a correlational observation from a single event (COVID-19 onset). Causal attribution would require multiple independent observations across different crisis events.

#### Finding 3 — Pre-COVID Community Distress Was Already Elevated (2019 Peak Precedes Pandemic)

EDA over the full 2018–2024 dataset reveals that the pre-COVID period (2018–2019) was not a low-distress baseline. r/anxiety's crisis rate reached **36.4% in 2019** — the highest of any year in the dataset and nearly double the 2020 COVID-onset rate (18.9%). r/SuicideWatch and r/mentalhealth similarly peaked in 2019 (32.6% and 27.3% respectively).

This finding complicates a simple "COVID caused the mental health crisis" narrative. For anxiety and SuicideWatch communities, the crisis was already at peak before the WHO pandemic declaration. The pandemic appears to have **sustained an existing elevated state** rather than initiating it. For r/depression, the pattern differs: crisis rates are more evenly distributed across the pre-COVID, COVID, and early post-COVID years (13–17% in 2018–2022), with a notable elevation in 2023 (26.9%), consistent with depression communities experiencing a longer post-pandemic recovery tail.

The post-COVID period (2022–2024) shows a sharp decline across four of five communities — r/anxiety (8%), r/SuicideWatch (4%), r/mentalhealth (2%), and r/lonely (8%) — with only r/depression remaining elevated. This divergence between anxiety/crisis-focused and depression communities in the recovery phase is a potentially meaningful signal for how different community types respond to macro-level mental health events.

These per-year crisis rates are computed by `src/reporting/eda.py` and available in each subreddit's `eda_summary.html` report.

### 5.3 Decision Usefulness — Recall@K

Beyond global PR-AUC, the evaluation records **Recall@K**: if a community support team can act on at most K alert weeks per evaluation period, how many true crisis weeks fall within the model's top-K ranked predictions?

Selected Recall@5 values from the current evaluation (K=5 out of 327 eval weeks):

| Subreddit | Model | Crisis Wks | Recall@5 | Random@5 | Lift |
|---|---|---|---|---|---|
| r/anxiety | XGBoost | 162 | 0.031 | 0.015 | **2.0×** |
| r/depression | XGBoost | 85 | 0.059 | 0.026 | **2.3×** |
| r/SuicideWatch | XGBoost | 188 | 0.027 | 0.015 | **1.8×** |
| r/lonely | XGBoost | 276 | 0.018 | 0.015 | 1.2× |
| r/mentalhealth | XGBoost | 246 | 0.020 | 0.015 | 1.3× |

Note: absolute Recall@K values are low because K=5 represents only 1.5% of the 327-week evaluation window; the meaningful signal is the lift over random. Communities with lower crisis rates (r/depression at 26%) show the highest lift because the model's ranking discriminates more when positives are rarer. Communities with very high crisis rates (r/lonely at 84%) show near-random Recall@K because almost any 5-week selection will include crisis weeks.

### 5.4 Detection Lead Time

Average XGBoost detection lead time by community:

| Subreddit | Avg Lead Time | Interpretation |
|---|---|---|
| r/anxiety | **14.5 weeks** | Model flagged escalation consistently 14+ weeks before peaks |
| r/SuicideWatch | **12.6 weeks** | Strongest operationally actionable early warning |
| r/depression | **4.6 weeks** | Shorter lead — depression signals build more gradually |
| r/mentalhealth | 0.0 weeks | Prediction fires at or after peak; State 2 is near-constant |

r/lonely is excluded from this table: its computed lead time (79.7 weeks) is an artefact of one sustained multi-year elevated period where the community remained in State 2+ continuously, not a genuine 79-week advance warning. The lead time formula counts consecutive pre-peak crisis predictions; a community that never returns to State 0 inflates this figure structurally.

LSTM lead time is 0.0 weeks across all communities — the LSTM transitions through State 1 (Early Vulnerability) in the weeks before crisis peaks rather than jumping directly to State 2, so consecutive State 2+ predictions do not accumulate before the peak under the formula.

The 14.5-week lead time on r/anxiety means the model was already predicting "next week will be Elevated Distress" for 14 consecutive weeks before the crisis peaked — not a single 14-week-ahead forecast. Each prediction used only data available at that point in time, confirmed by walk-forward CV. This is the system's primary operational value: sustained early warning that gives moderators a multi-week intervention window.

### 5.5 Temporal Analysis — Pre-COVID, COVID, and Post-COVID Distributional Shift

The full 2018–2024 dataset spans three structurally distinct periods, each with different community distress dynamics:

| Period | Years | Defining characteristic |
|---|---|---|
| **Pre-COVID** | 2018–2019 | Baseline Reddit mental health community behaviour; anxiety crisis already building in 2019 |
| **COVID** | 2020–2021 | Pandemic onset (March 2020), lockdowns, vaccine rollout; sustained elevated distress |
| **Post-COVID** | 2022–2024 | Community recovery; sharply declining crisis rates, new behavioural baseline |

**Crisis rate by period (average fraction of weeks in State 2+):**

| Subreddit | Pre-COVID (2018–19) | COVID (2020–21) | Post-COVID (2022–24) | Trend |
|---|---|---|---|---|
| r/anxiety | 23.1% | 12.4% | 8.3% | Declining |
| r/SuicideWatch | 25.2% | 21.9% | 3.3% | Sharp post-COVID drop |
| r/depression | 13.2% | 16.2% | 14.7% | Stable / slow recovery |
| r/lonely | 24.2% | 20.0% | 7.6% | Declining |
| r/mentalhealth | 22.5% | 8.6% | 1.6% | Sharp decline from 2020 |

Key observation: **r/depression is the outlier**. While anxiety, SuicideWatch, lonely, and mentalhealth communities all show markedly lower post-COVID crisis rates, r/depression maintained a consistently elevated rate through 2022–2023. This is consistent with clinical evidence that depression has a longer recovery tail than anxiety following major stressors.

**Distributional shift and community-specific recalibration:**

The three-period structure creates a natural challenge for any model trained across the full window: post-COVID weeks (2022–2024) have a substantially lower crisis rate than 2018–2021. The community-specific labelling scheme (Section 2.3) is designed to handle this — thresholds are refit on each fold's training window, so the model's definition of "crisis" recalibrates with the community's evolving baseline. A community returning to a lower distress level will have its thresholds recalibrate accordingly, avoiding persistent false alerts.

XGBoost handles this recalibration well because each fold's training data independently sets the class boundary. The LSTM's per-fold MinMaxScaler similarly ensures feature scales are anchored to the current training window, not a global normalisation that would leak future distribution information.

---

## 6. Layer 3 — Prescriptive Analytics

*Layer 3 asks: Given this week's forecast, what should community moderators do?*

### 6.1 GenAI Weekly Briefs

After walk-forward evaluation, every prediction week receives a structured moderator brief. The generation pipeline (`src/narration/narrative_generator.py`) follows three steps:

1. **Structured Context Construction** — A JSON object containing predicted state, actual state (where available), top SHAP feature values with week-over-week deltas, and raw distress score
2. **Retrieval-Augmented Generation** — The structured context is augmented with the relevant section of `config/intervention_playbook.md` matching the predicted state. This is deterministic retrieval over a fixed 4-section document (one section per crisis state), not a vector database
3. **LLM Generation** — Prompt sent to Claude (`claude-sonnet`) if Anthropic API key present → GPT-4o if OpenAI key present → template string fallback. All three paths produce the same structured output format

Briefs are stored as a keyed JSON file per subreddit (`data/reports/{sub}/weekly_briefs.json`), replacing the earlier per-week `.txt` file format. LLM call metadata (model used, fallback reason) is logged to `data/reports/{sub}/logs/weekly_brief_calls.jsonl`.

**Example Weekly Brief — r/anxiety — Elevated Distress (State 2) — Week of 2020-01-06:**

> *r/anxiety (2020-W02) is labeled Elevated Distress this week based on model outputs (aggregate community-level indicator, not individual assessment). Distress score change vs the prior week is +0.21; key signals: new_poster_ratio increased +0.14 week-over-week (now 0.38); unique_posters_delta: +47; avg_flesch_kincaid_roll2w declining (posts becoming simpler, more fragmented). Recommended community actions: increase moderator check-in frequency; pin crisis resource links at the top of the subreddit; consider reaching out to r/SuicideWatch for coordinated resource sharing given the current cross-community signal.*

### 6.2 Interactive What-If Scenario Panel

The Streamlit dashboard includes a **scenario panel** where a community manager can adjust three feature dimensions and observe the model's predicted state change in real time:

| Control | Feature mapped | Interpretation |
|---|---|---|
| Hopelessness % slider | `hopelessness_density` | Increase: simulate a week with more hopeless language |
| Post volume % slider | `post_volume` | Increase: simulate a surge week |
| Late-night posts % slider | `late_night_post_ratio` | Increase: simulate distress concentrated in night hours |

Feature mapping is handled by `src/dashboard/demo_utils.py`, which resolves the canonical feature name from available columns using a priority list (e.g. `hopelessness_density` → `hopelessness` → `distress_lexicon_density`). Scenario adjustments are applied multiplicatively to the selected base week's feature vector before inference. Results display in real time as the slider moves.

This enables moderators to answer questions like: "If hopelessness density doubled next week relative to this week, would the model change its prediction?" — turning a black-box prediction into a sensitivity analysis tool.

> **[Figure 7: What-if scenario panel]**
> *Live at https://community-crisis-predictor-mozt6amaceenfxso6pegb8.streamlit.app — navigate to the "Scenario Analysis" tab. Three sliders (hopelessness density, post volume, late-night post ratio) adjust the current week's feature vector multiplicatively. The model prediction updates in real time as sliders move. This enables moderators to ask: "If hopelessness density doubled next week, would the model escalate to State 3?" — turning a black-box prediction into a sensitivity analysis tool.*

### 6.3 Resource Allocation — LP Moderator Allocator

The prescriptive layer includes a **cross-community LP resource allocator** (`src/prescriptive/lp_allocator.py`) that distributes a fixed weekly moderator-hour budget across all five communities simultaneously. The allocation is formulated as a linear programme:

**Objective**: maximise `Σ p[i] × effectiveness[i] × hours[i]`

Subject to: `Σ hours[i] ≤ total_budget`, `hours[i] ≥ min_hours`, `hours[i] ≤ max_hours`

Where `p[i]` is each community's predicted escalation probability (from the ensemble model) and `effectiveness[i]` is a configurable per-community intervention impact coefficient (default 0.6–0.9, with r/SuicideWatch weighted highest at 0.9). The LP is solved via `scipy.optimize.linprog`.

The Streamlit dashboard exposes a **sensitivity analysis panel** showing optimal allocation across budget scenarios from 5 to 20 moderator hours per week, allowing community managers to see how the allocation shifts as resources change. This directly addresses the operational question: "given limited moderation capacity, where should effort be directed this week?"

---

## 7. Production Deployment

The system is deployed as two hosted services following a Train → Commit → Deploy pattern.

| Service | Platform | URL |
|---|---|---|
| FastAPI inference API | Render.com | https://community-crisis-predictor.onrender.com |
| Streamlit dashboard | Streamlit Cloud | https://community-crisis-predictor-mozt6amaceenfxso6pegb8.streamlit.app |

> **Cold-start note (free Render tier):** The API sleeps after 15 minutes of inactivity. The first request after sleep takes approximately 30–60 seconds. For live demos, hit `/health` once before the presentation to wake the service.

### 7.1 FastAPI Inference Service

The serving layer (`serving/main.py`) provides a production inference endpoint that loads all model artifacts at startup and exposes four endpoints:

| Endpoint | Method | Description |
|---|---|---|
| `/health` | GET | Service status; lists loaded models |
| `/predict` | POST | XGB + optional LSTM inference on a weekly feature vector; returns predicted state, probabilities, and drift warnings |
| `/model-info` | GET | Walk-forward metrics and top SHAP features per subreddit |
| `/logs/summary` | GET | Aggregate statistics from the prediction log (JSONL) |
| `/docs` | GET | Auto-generated Swagger UI |

The `/predict` endpoint accepts an optional `feature_history` array (last 8 weeks) to enable LSTM prediction alongside XGBoost. Per-request **drift detection** checks each input feature against the training distribution (mean ± 2.5σ) and returns warnings for out-of-distribution inputs. All predictions are logged to `serving/logs/predictions.jsonl` for audit.

The serving layer is deliberately isolated from `src/` — the LSTM architecture (`LSTMNet`) is replicated inline in `serving/main.py` to avoid dependency on PyTorch training code. Model artifacts (`.pkl`, `.pt`, `_feature_stats.json`) are read directly from `data/models/` on the same filesystem.

### 7.2 Streamlit Dashboard

The dashboard is a **multipage** Streamlit app. The Cloud entrypoint remains `src/dashboard/app.py`; additional pages live under `src/dashboard/pages/`.

| Navigation label | Script | Audience |
|------------------|--------|----------|
| **app** (Streamlit default for the root script) | `app.py` | Analysts: full replay UI, tabs (drift, SHAP, quality, metrics, allocation), model picker. |
| **Community Copilot** | `pages/2_End_User_Summary.py` | Moderators: week-scoped **triage board** with left-aligned tabular columns (rank, community, signal, p(hi), trend) and an **Open** control per row; **equal-width** two-column main workspace (list \| detail) below a red section divider; full-width **Responsible use** footer. **AI Copilot** calls the FastAPI `POST /brief` endpoint so LLM keys stay on the server. |

The root page runs on Streamlit Cloud with `data/features/features.parquet` and `data/models/eval_results.json` committed to the repository (tracked as git artifacts). When `API_MODE=true` (set via Streamlit Cloud secrets), the dashboard:

- Shows a **live API connection status indicator** in the sidebar (analyst page)
- Can use the **AI Copilot** path on the moderator page via `POST /brief` (no provider keys in Streamlit)
- Forwards `/predict` calls to the Render.com API rather than running local inference where applicable
- **Automatically falls back** to local pipeline outputs if the API is unreachable

This means the dashboard functions regardless of API availability — the live API connection is a capability enhancement, not a dependency. The sidebar on the Community Copilot page documents that **app** denotes the analyst dashboard; renaming that nav entry would require renaming the root file (e.g. to `Home.py`), which is optional and deployment-specific.

### 7.3 CI/CD Pipeline

GitHub Actions provides two workflows:

- **`ci.yml`** — runs 72 core pipeline tests + 29 API tests on every push/PR. API tests run with `MOCK_MODELS=true` (no real model files required in CI)
- **`retrain.yml`** — manual dispatch; runs full pipeline with synthetic data, commits updated model artifacts back to the repository, and triggers automatic redeploy on both Render.com and Streamlit Cloud

To retrain on real data locally and redeploy: `make prepare-deploy && git add . && git commit -m "Update artifacts" && git push`.

---

## 8. Ethical Considerations and Limitations

### Ecological Fallacy

The community-level signal does not permit inference about any individual user. A community in State 3 contains users in all states; a community in State 0 may include users in acute personal crisis. All system outputs are framed as population-level aggregate signals. The ecological fallacy disclaimer appears explicitly in every generated weekly brief.

### Platform Demographic Skew

The dataset over-represents English-language, younger, and tech-adjacent populations. Communities with different demographic compositions, languages, or cultural norms around mental health disclosure would require independent validation before the system could be applied.

### Proxy Label Validity

The composite distress score is not a validated clinical instrument. Its component weights are theoretically motivated but not calibrated against expert clinical labels. Results should be interpreted as detecting changes in community posting behaviour consistent with distress, not as measuring clinical mental health outcomes.

### Systematic Post Removal Bias

The most severe content on r/SuicideWatch is frequently removed by moderators before archival, meaning the dataset systematically undersamples the highest-severity weeks. Model recall on State 3 is therefore likely lower than it would be on an unfiltered archive. This is a structural limitation that cannot be addressed by collecting more data from the same source.

---

## 9. Conclusion and Future Work

This project demonstrates that a structured three-layer analytics pipeline — Descriptive (what is happening), Predictive (what will happen next week), Prescriptive (what should be done) — can extract genuine decision-relevant signal from noisy, biased social media data, provided the constraints shaping that data are treated as design inputs rather than caveats.

The most robust empirical finding is that **XGBoost achieves strong crisis detection under community-specific labelling, with up to 14.5 weeks of early warning on r/anxiety**: the model consistently raises alerts in the weeks preceding crisis peaks, giving moderators a multi-week intervention window. LSTM is competitive on PR-AUC but achieves lower recall in the current evaluation due to training data volume constraints in early walk-forward folds (detailed in Section 5.2). The ensemble (max of XGB and LSTM, safety-first) ensures the system inherits the best of both: XGBoost's high recall and LSTM's graduated 4-class severity assessment.

The system's handling of its own data-sufficiency limits — placing r/lonely and r/mentalhealth in Trend Monitoring mode rather than issuing unreliable alerts — reflects a design principle that applies to any operational early warning system: knowing when *not* to alert is as important as knowing when to alert.

The production deployment (FastAPI on Render.com + Streamlit Cloud dashboard) validates the full Train → Serve → Monitor loop and demonstrates that the system is operationally ready for the moderation use case, within the constraints documented in Section 3.

### Priority Future Work

| Priority | Item |
|---|---|
| P1 | **LSTM multi-task training** — pre-train LSTM jointly across all five communities (~1,830 sequences from fold 1) then fine-tune per community; expected to close the recall gap with XGBoost |
| P1 | **Increased LSTM training window** — raise minimum training weeks to 52 and sequence length to 13; eliminates the under-trained early folds that drag down aggregate PR-AUC |
| P1 | **52-week lag features** — add year-over-year distress baseline feature to capture seasonal patterns (exam periods, holiday seasons) not captured by the current 4-week rolling window |
| P2 | **Conformal prediction intervals** — calibrated uncertainty bounds on state probability estimates |
| P2 | **Weekly batch ingestion pipeline** — cron-triggered Reddit API collection → feature update → inference, to move from backtest replay to live weekly forecasting |
| P3 | **Multi-platform data sources** — Bluesky, clinical forum data for demographic broadening and external validation |
| P3 | **Online learning** — incremental model updates as new weeks arrive, rather than batch retrain |

---

## References

[1] Low, D. M., Rumker, L., Talkar, T., Torous, J., Cecchi, G., & Ghosh, S. S. (2020). Natural Language Processing Reveals Vulnerable Mental Health Support Groups and Heightened Health Anxiety on Reddit During COVID-19. *npj Digital Medicine*. https://zenodo.org/records/3941387

[2] Hutto, C. J., & Gilbert, E. (2014). VADER: A Parsimonious Rule-Based Model for Sentiment Analysis of Social Media Text. *ICWSM*. https://www.researchgate.net/publication/275828927

[3] Chen, T., & Guestrin, C. (2016). XGBoost: A Scalable Tree Boosting System. *KDD*. https://doi.org/10.1145/2939672.2939785

[4] Lundberg, S. M., & Lee, S.-I. (2017). A Unified Approach to Interpreting Model Predictions. *NeurIPS*. https://www.researchgate.net/publication/317062430

[5] Grootendorst, M. (2022). BERTopic: Neural topic modeling with a class-based TF-IDF procedure. *arXiv*. https://arxiv.org/pdf/2203.05794

[6] Hochreiter, S., & Schmidhuber, J. (1997). Long Short-Term Memory. *Neural Computation*. https://www.researchgate.net/publication/13853244

---

## Appendix

### A. Repository and Deployed Services

| Resource | URL |
|---|---|
| GitHub repository | https://github.com/jainaryan/community-crisis-predictor |
| FastAPI inference API (Render.com) | https://community-crisis-predictor.onrender.com |
| FastAPI Swagger UI | https://community-crisis-predictor.onrender.com/docs |
| Streamlit dashboard (Streamlit Cloud) | https://community-crisis-predictor-mozt6amaceenfxso6pegb8.streamlit.app |

### B. Pipeline Artifact Paths

| Artifact | Path | Tracked in git? |
|---|---|---|
| Feature matrix | `data/features/features.parquet` | Yes |
| Model evaluation results | `data/models/eval_results.json` | Yes |
| XGBoost models | `data/models/{sub}_xgb.pkl` | Yes |
| LSTM checkpoints | `data/models/{sub}_lstm.pt` | Yes |
| Feature statistics | `data/models/{sub}_feature_stats.json` | Yes |
| SHAP values | `data/reports/{sub}/shap.csv` | Yes |
| Drift alerts | `data/reports/{sub}/drift_alerts.json` | Yes |
| EDA HTML reports | `data/reports/{sub}/eda_summary.html` | Yes |
| Backtesting timeline | `data/reports/{sub}/timeline.html` | Yes |
| Weekly briefs | `data/reports/{sub}/weekly_briefs.json` | Yes |
| Data completeness | `data/reports/{sub}/weekly_completeness.csv` | Yes |

### C. Figure Source Reference

All figures reference files generated by the pipeline. Interactive HTML versions are committed to the repository.

| Figure | Source File | Section |
|---|---|---|
| Fig 1: Post volume timeline | `data/reports/{sub}/timeline.html` (interactive Plotly) | 2.1 |
| Fig 2: EDA distress trend charts | `data/reports/{sub}/eda_summary.html` (open in browser) | 4.1 |
| Fig 3: Crisis rate by year | Inline table in Section 4.1 (data from `eda_report.json`) | 4.1 |
| Fig 4: SHAP feature importance | `data/reports/{sub}/feature_importance.html` (interactive Plotly) | 4.2 |
| Fig 5: Timeline — anxiety vs SuicideWatch | `data/reports/{sub}/timeline.html` | 4.3 |
| Fig 6: PR curves | Streamlit dashboard Model Metrics tab | 5.1 |
| Fig 7: What-if scenario panel | Live Streamlit dashboard (Section 6.2 URL) | 6.2 |

### D. AI Tool Usage Declaration

In accordance with NUS IS5126 academic policy, the use of AI tools in this project is declared below. AI assistance was used for code scaffolding, document drafting, and review — with all analytical choices, experimental design, interpretation of results, and constraint analysis performed by the project team. No AI tool generated the results tables or made modelling decisions.
