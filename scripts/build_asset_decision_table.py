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

# Load base telemetry data
df = pd.read_csv("data/raw/lime_vehicles_sample.csv")

print("COLUMNS:", df.columns.tolist())

# -----------------------------
# PROXY & DERIVED FEATURES
# -----------------------------

# Vehicle type proxy (based on usage intensity)
df["vehicle_type"] = np.where(
    df["distance_km"] / df["rides_today"].replace(0, np.nan) > 3,
    "scooter",
    "bike"
)
df["vehicle_type"] = df["vehicle_type"].fillna("bike")


# Battery health proxy (0–1)
df["battery_health_index"] = df["battery_level"] / 100

# Utilization proxy
df["utilization_score"] = df["rides_today"]

# Usage intensity proxy
df["distance_per_ride"] = df["distance_km"] / df["rides_today"].replace(0, np.nan)
df["distance_per_ride"] = df["distance_per_ride"].fillna(0)

# City → zone proxy
def city_to_zone(city):
    high_load = ["bangalore", "hyderabad", "delhi"]
    if city.lower() in high_load:
        return "high_load"
    return "normal"

df["zone_type"] = df["city"].apply(city_to_zone)

# -----------------------------
# ECONOMIC PROXIES (ASSUMED)
# -----------------------------

# Revenue proxy
df["revenue_per_day"] = df["rides_today"] * 10  # assumed avg revenue per ride

# Cost proxies
df["battery_cost_per_day"] = (1 - df["battery_health_index"]) * 20
df["maintenance_cost_per_day"] = df["distance_km"] * 0.5

# Net margin
df["net_margin_per_day"] = (
    df["revenue_per_day"]
    - df["battery_cost_per_day"]
    - df["maintenance_cost_per_day"]
)

# -----------------------------
# DECISION LOGIC
# -----------------------------

def recommend(row):
    if row["net_margin_per_day"] < 0:
        return "decommission"
    if row["battery_health_index"] < 0.3:
        return "repair"
    if row["zone_type"] == "high_load" and row["battery_health_index"] < 0.5:
        return "rotate"
    return "continue"

df["recommended_action"] = df.apply(recommend, axis=1)

# -----------------------------
# SAVE DECISION TABLE
# -----------------------------

df.to_csv("data/generated/asset_decision_table_v1.csv", index=False)

print("✅ Asset decision table generated successfully")

df.to_excel(
    "data/generated/asset_decision_table_v1.xlsx",
    index=False,
    sheet_name="asset_decisions"
)

