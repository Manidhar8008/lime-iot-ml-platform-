import subprocess
import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def run_step(name, command):
    print(f"\n▶ Running step: {name}")
    print(f"▶ Command: {' '.join(command)}")

    result = subprocess.run(
        command,
        cwd=PROJECT_ROOT,
        shell=False
    )

    if result.returncode != 0:
        print(f"\n❌ Step failed: {name}")
        sys.exit(1)

    print(f"✅ Step completed: {name}")

def main():
    print("====================================")
    print(" Lime IoT Decision System Pipeline")
    print("====================================")

    # -----------------------------
    # Step 1: Validate decision data exists
    # -----------------------------
    decision_file = os.path.join(
        PROJECT_ROOT,
        "data",
        "Decision",
        "asset_decision_final.csv"
    )

    if not os.path.exists(decision_file):
        print("❌ Missing decision table:")
        print(decision_file)
        sys.exit(1)

    print("✅ Decision table found")

    # -----------------------------
    # Step 2: Generate visual artifacts
    # -----------------------------
    run_step(
        "Generate Visualization Artifacts",
        [sys.executable, "scripts/generate_visuals.py"]
    )

    # -----------------------------
    # Future steps (intentionally explicit)
    # -----------------------------
    print("\nℹ️ Model training and decision generation")
    print("ℹ️ are intentionally excluded from this runner")
    print("ℹ️ until decision authority is finalized.")

    print("\n🎯 Pipeline execution completed successfully")

if __name__ == "__main__":
    main()
