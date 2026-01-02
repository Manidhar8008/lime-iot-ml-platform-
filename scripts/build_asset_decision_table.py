"""
Purpose:
    Generate decision-ready asset table from raw IoT telemetry

Input:
    data/raw/lime_vehicles_sample.csv

Output:
    data/generated/asset_decision_table_v1.csv
    data/generated/asset_decision_table_v1.xlsx

Decisions Enabled:
    - Continue operation
    - Schedule repair
    - Decommission asset

Assumptions:
    - Battery health inferred from battery_level
    - Utilization inferred from rides_today
    - Proxies used where direct cost data is unavailable
"""


import pandas as pd
import numpy as np

# ----------------------------
# Load asset-level base data
# ----------------------------
df = pd.read_csv("data/lime_vehicles_sample.csv")

# ----------------------------
# Time-based aggregates
# ----------------------------
df["battery_level_avg_7d"] = df["battery_level"].rolling(7, min_periods=1).mean()
df["battery_level_avg_30d"] = df["battery_level"].rolling(30, min_periods=1).mean()

df["battery_trend_7d_vs_30d"] = (
    df["battery_level_avg_7d"] - df["battery_level_avg_30d"]
)

df["health_decline_rate"] = -df["battery_trend_7d_vs_30d"]

# ----------------------------
# Usage features
# ----------------------------
df["rides_per_day_avg"] = df["rides_today"].rolling(7, min_periods=1).mean()
df["utilization_trend"] = df["rides_today"].diff().fillna(0)

df["utilization_percentile"] = df["rides_per_day_avg"].rank(pct=True)

# ----------------------------
# Zone construction (simple)
# ----------------------------
df["zone_id"] = df["city"]

zone_stats = (
    df.groupby("zone_id")
    .agg(
        zone_rides=("rides_today", "mean"),
        zone_assets=("vehicle_id", "nunique"),
    )
    .reset_index()
)

zone_stats["deployment_density"] = (
    zone_stats["zone_rides"] / zone_stats["zone_assets"]
)

df = df.merge(zone_stats, on="zone_id", how="left")

# ----------------------------
# Zone stress index
# ----------------------------
df["zone_stress_index"] = pd.qcut(
    df["deployment_density"],
    q=3,
    labels=["Low", "Medium", "High"]
)

# ----------------------------
# Intervention risk score
# ----------------------------
df["intervention_risk_score"] = (
    0.5 * df["health_decline_rate"].clip(lower=0)
    + 0.3 * df["utilization_trend"].clip(lower=0)
    + 0.2 * (df["zone_stress_index"] == "High").astype(int)
)

# ----------------------------
# Confidence level
# ----------------------------
conditions = [
    (df["battery_level_avg_30d"].notna()) & (df["rides_per_day_avg"] > 0),
    (df["battery_level_avg_30d"].notna()),
]

choices = ["High", "Medium"]
df["confidence_level"] = np.select(conditions, choices, default="Low")

# ----------------------------
# Recommended action
# ----------------------------
def decide(row):
    if row["intervention_risk_score"] > 1.0 and row["confidence_level"] == "High":
        return "repair_or_rotate"
    if row["intervention_risk_score"] > 1.0:
        return "inspect"
    return "continue"

df["recommended_action"] = df.apply(decide, axis=1)

# ----------------------------
# Final decision table
# ----------------------------
final_cols = [
    "vehicle_id",
    "city",
    "zone_id",
    "battery_health_index",
    "battery_level_avg_7d",
    "battery_level_avg_30d",
    "health_decline_rate",
    "rides_per_day_avg",
    "utilization_percentile",
    "battery_trend_7d_vs_30d",
    "zone_stress_index",
    "deployment_density",
    "intervention_risk_score",
    "confidence_level",
    "recommended_action",
]

df[final_cols].to_csv(
    "data/asset_decision_table_final.csv", index=False
)

print("✅ Final asset decision table generated")
