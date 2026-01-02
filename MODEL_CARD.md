Model Card — Asset Intervention Risk Model
Model Objective
The purpose of this model is to estimate the probability that an operational asset will require preventive intervention within the next 7–14 days, in order to reduce avoidable downtime and revenue loss.
This model does not predict asset failure.
 It predicts intervention risk, enabling early, reversible action.

Prediction Target
Target variable: needs_intervention (binary)
1 → Asset required preventive operational action within the prediction window


0 → Asset continued normal operation


Intervention includes:
Battery service or inspection


Temporary removal from fleet


Maintenance-triggered downtime


Margin-negative operation indicating unsustainable usage


This framing avoids failure-only labeling and reflects real operational workflows.

Prediction Window
Horizon: 7–14 days


Rationale:


Actionable for operations teams


Long enough to capture early degradation signals


Short enough to prevent delayed response


At time T, the model only uses data available up to T to predict intervention risk in (T, T+14].
Strict temporal boundaries are enforced to prevent data leakage.

Model Type
Primary model:
Logistic Regression (baseline, interpretable)


Optional extension:
Gradient Boosted Trees (for non-linear interactions)


Why simple models were chosen
Interpretability is critical for operational trust


Decisions must be explainable to non-technical stakeholders


Simpler models degrade more gracefully under data shift


Model complexity is intentionally constrained.

Feature Set Overview
Features are grouped by decision relevance, not convenience.
Asset Health
battery_health_index


battery_level_avg_7d


battery_level_avg_30d


Purpose: Capture fundamental degradation state.

Usage Stress
rides_per_day_avg


distance_per_day_avg


utilization_percentile


Purpose: Measure stress accumulation that accelerates wear.

Temporal Momentum
battery_trend_7d_vs_30d


utilization_trend


health_decline_rate


Purpose: Detect early warning signals before thresholds are breached.

Environmental / Context Risk
zone_stress_index


deployment_density


zone_intervention_rate


Purpose: Modify risk based on operational intensity, not determine outcomes alone.
Spatial features are intentionally discretized to preserve explainability.

What the Model Does NOT Do
This model explicitly does not:
Optimize deployment locations


Predict routes or rider behavior


Perform long-term demand forecasting


Use raw GPS trajectories


These are future extensions, not current guarantees.

Validation Strategy
Time-aware train/validation split


Validation performed on forward windows only


No random shuffling across time


Metrics considered
Precision–recall balance (intervention efficiency)


Stability across thresholds


Consistency across time windows


Accuracy alone is not a sufficient success metric.

Uncertainty & Risk Management
Predictions are accompanied by confidence scores


Low-confidence predictions do not trigger irreversible actions


Conservative thresholds are used for automated recommendations


The model is designed to support human-in-the-loop decision-making.

Known Limitations
Battery health is a proxy, not a physical measurement


Environmental stress is approximated via zones


Rare failure modes may be underrepresented


All limitations are documented to prevent overconfidence.

Decision Integration
Model outputs feed into the Asset Decision Table, where:
Risk score


Confidence level


Operational recommendation


are combined to guide action.
The model assists judgment — it does not replace it.

Intended Use
This model is designed for:
Fleet operations teams


Asset reliability planning


Preventive maintenance prioritization


It is not intended for real-time control or automated enforcement.

Summary
This model demonstrates Applied Data Science in production context:
Business-first objective


Conservative modeling choices


Explicit uncertainty handling


Clear decision alignment


The focus is not predictive novelty, but operational reliability and trust.


