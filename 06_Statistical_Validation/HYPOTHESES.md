Hypothesis 1 — Utilization accelerates battery degradation
Business question
Do heavily used vehicles degrade faster than lightly used vehicles, even when average battery level looks acceptable?
This question matters because:
High-utilization assets generate revenue


But they may silently accumulate long-term damage


Late detection leads to sudden downtime and revenue loss



Null hypothesis (H₀)
There is no statistically significant difference in battery health between high-utilization and low-utilization vehicles.

Alternative hypothesis (H₁)
High-utilization vehicles show significantly worse battery health compared to low-utilization vehicles, indicating accelerated degradation.

Data used
Asset-level aggregated table


Metrics:


battery_health_index (proxy for long-term health)


rides_today or utilization proxy


Raw event-level data is intentionally excluded to avoid noise and leakage.

Grouping strategy
Vehicles are segmented into:
High utilization group: top 25% by rides per day


Low utilization group: bottom 25% by rides per day


Quartiles are chosen to:
Reduce sensitivity to outliers


Create interpretable, stable cohorts



Statistical test selection
Mann–Whitney U test (non-parametric)
Reasoning:
Battery health distributions are not assumed to be normal


Operational data often contains skew and outliers


The test compares medians rather than means, aligning better with decision thresholds



Validation approach
To ensure robustness:
Effect size is evaluated alongside statistical significance


The test is repeated with alternative cutoffs (top/bottom 20%, 30%)


Directional consistency is required before acting on results


A statistically significant result without meaningful effect size does not trigger intervention.

Decision implication
If H₁ is supported:
High-utilization assets enter proactive inspection or rotation queues


Thresholds for “continue operation” are tightened for these assets


If H₀ is not rejected:
Utilization alone is insufficient as a degradation signal


Decisions rely more heavily on trend-based indicators



Known limitations
Battery health is a proxy, not a physical measurement


Ride aggressiveness and terrain are not explicitly modeled


Environmental factors may partially explain degradation


These limitations are explicitly acknowledged to avoid overconfidence.

