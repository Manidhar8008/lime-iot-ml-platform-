import joblib
import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
MODEL_PATH = PROJECT_ROOT / "src" / "battery_predict" / "battery_model.pkl"
FEATURES_PATH = PROJECT_ROOT / "src" / "battery_predict" / "battery_features.pkl"

model = joblib.load(MODEL_PATH)
feature_cols = joblib.load(FEATURES_PATH)


def predict_battery(latitude, longitude, is_disabled, is_reserved, vehicle_type: str) -> int:
    """Predict battery level (0–100) for a single vehicle."""
    # Base template for all features
    data = {col: 0 for col in feature_cols}

    # Core numeric + status features
    data.update(
        {
            "latitude": latitude,
            "longitude": longitude,
            "is_disabled": is_disabled,
            "is_reserved": is_reserved,
        }
    )

    # One-hot vehicle type
    vehicle_col = f"vehicle_type_{vehicle_type}"
    if vehicle_col in data:
        data[vehicle_col] = 1
    else:
        # If unseen vehicle type, all one-hots remain 0 -> model still works, just less specific
        print(f"⚠️ vehicle_type '{vehicle_type}' not in training columns; using default encoding.")

    df = pd.DataFrame([data])
    pred = model.predict(df)[0]
    # Clamp between 0 and 100
    return max(0, min(100, round(pred)))


if __name__ == "__main__":val = predict_battery(47.61, -122.33, 0, 0, "unknown")

