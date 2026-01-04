# Model Performance Comparison

This section compares the baseline machine learning models used to predict maintenance risk.  
The goal is not to chase complexity, but to understand how different models behave on the same business problem and what trade-offs they introduce.

| Model               | Accuracy     | Recall (Risk = 1) | ROC AUC | Strength                     |
|---------------------|--------------|-------------------|---------|------------------------------|
| Logistic Regression | ~0.96–0.97   | High (≈1.0)       | ~0.99   | Stable and consistent risk scoring |
| Decision Tree       | ~0.98        | Moderate (~0.71)  | ~0.86   | Clear rules and interpretability   |

---

## Interpretation (Why these results matter)

### Logistic Regression — Risk Scoring Model

Logistic Regression performs strongly when the objective is to **catch risky vehicles early**.  
Instead of producing hard yes/no decisions, it assigns probability scores, which makes it useful for ranking assets by risk level.

This behavior is especially valuable in maintenance scenarios where missing a true failure can lead to higher operational cost than investigating a false alert.

In this project, Logistic Regression consistently shows:
- High recall on risky vehicles
- Stable performance across samples
- Better ranking quality, reflected in ROC AUC

**Key takeaway:**

> Logistic Regression works well as a primary model when the focus is early risk identification rather than strict rule-based decisions.

---

### Decision Tree — Explainability and Insight Model

Decision Trees help answer a different question: **why** the model is flagging risk.

They break decisions into simple, understandable rules and highlight which features influence outcomes the most.  
This makes them useful for operational discussions and for validating whether the model logic aligns with real-world behavior.

Feature importance analysis shows:
- **rides_avg_7d contributes ~70%**
- **battery_decline_7v14 contributes ~30%**

This indicates that recent usage intensity is the strongest signal for maintenance risk, while battery degradation plays a secondary but meaningful role.

**Key takeaway:**

> Decision Trees provide transparency into operational drivers of risk and support explainability, even if their recall is lower.

---

## Final Recommendation

Based on model behavior and business context:

- **Logistic Regression** is better suited as the **primary risk scoring model** due to its high recall and smooth probability outputs.
- **Decision Trees** are best used as a **supporting model** to explain predictions and communicate risk drivers to operations teams.

Together, this approach balances predictive performance with interpretability and practical decision-making.
