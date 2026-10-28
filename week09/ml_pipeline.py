from pathlib import Path
import pandas as pd

# ==========================================
# PART A - Setup and Validate Data
# ==========================================

DATA_PATH = Path(__file__).resolve().parent / "data" / "machines_ml.csv"

machines = pd.read_csv(DATA_PATH)

required = ["temp_c", "vibration", "runtime", "pressure", "fault"]
missing = set(required) - set(machines.columns)

if missing:
    raise ValueError(f"Missing columns: {sorted(missing)}")

if machines[required].isna().any().any():
    raise ValueError("Required columns contain missing values.")

if not all(pd.api.types.is_numeric_dtype(machines[c]) for c in required):
    raise ValueError("Required columns must be numeric.")

if not set(machines["fault"].unique()).issubset({0, 1}):
    raise ValueError("fault must contain only 0 and 1.")

counts = machines["fault"].value_counts()

if set(counts.index) != {0, 1} or (counts < 2).any():
    raise ValueError("Both classes need enough rows.")

print("Dataset Loaded Successfully!")
print("\nFirst 5 Rows:")
print(machines.head())

print("\nTotal Rows:", machines.shape[0])
print("Total Columns:", machines.shape[1])

features = ["temp_c", "vibration", "runtime", "pressure"]

print("\nFeature Ranges:")
print(machines[features].agg(["min", "max"]))

print("\nFault Class Counts:")
print(counts.sort_index())

print("\nFault Class Percentages:")
print(machines["fault"].value_counts(normalize=True).sort_index() * 100)

print("\nMachine ID is excluded because it is only an identifier.")
print("\nPart A Validation Completed Successfully!")

# ==========================================
# PART B - Features and Train-Test Split
# ==========================================

from sklearn.model_selection import train_test_split

FEATURES = ["temp_c", "vibration", "runtime", "pressure"]

X = machines[FEATURES]
y = machines["fault"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

print("\n--- PART B: TRAIN-TEST SPLIT ---")

print("\nOriginal Dataset:", X.shape)
print("Training Features:", X_train.shape)
print("Testing Features:", X_test.shape)
print("Training Target:", y_train.shape)
print("Testing Target:", y_test.shape)

print("\nOriginal Class Proportions:")
print(y.value_counts(normalize=True).sort_index() * 100)

print("\nTraining Class Proportions:")
print(y_train.value_counts(normalize=True).sort_index() * 100)

print("\nTesting Class Proportions:")
print(y_test.value_counts(normalize=True).sort_index() * 100)

assert len(X_train) == len(y_train)
assert len(X_test) == len(y_test)
assert len(X_train) + len(X_test) == len(X)

print("\nTrain-Test Split Verified Successfully!")
print("Part B Completed Successfully!")

# ==========================================
# PART C - Train and Evaluate Classifier
# ==========================================

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)

train_predictions = model.predict(X_train)
test_predictions = model.predict(X_test)

train_accuracy = accuracy_score(y_train, train_predictions)
test_accuracy = accuracy_score(y_test, test_predictions)

print("\n--- PART C: MODEL TRAINING ---")
print("\nTraining Accuracy:", train_accuracy)
print("Testing Accuracy:", test_accuracy)

print("\nTraining Accuracy (%):", round(train_accuracy * 100, 2))
print("Testing Accuracy (%):", round(test_accuracy * 100, 2))

cm = confusion_matrix(y_test, test_predictions, labels=[0, 1])

print("\nConfusion Matrix:")
print(cm)

tn, fp, fn, tp = cm.ravel()

print("\nConfusion Matrix Results:")
print({"TN": tn, "FP": fp, "FN": fn, "TP": tp})

manual_accuracy = (tn + tp) / cm.sum()

print("\nManual Accuracy:", manual_accuracy)
print("Testing Accuracy:", test_accuracy)

assert abs(manual_accuracy - test_accuracy) < 1e-12

gap = train_accuracy - test_accuracy

print("\nTraining-Testing Gap:", round(gap, 4))

print("\nActual Test Class Counts:")
print(y_test.value_counts().sort_index())

print("\nModel Evaluation:")
print("TN = Normal correctly predicted")
print("FP = Normal incorrectly predicted as Fault")
print("FN = Fault incorrectly predicted as Normal")
print("TP = Fault correctly predicted")

print("\nNote: One train-test split does not prove model reliability.")
print("\nPart C Completed Successfully!")

# ==========================================
# PART D - Depth Experiment and Persistence
# ==========================================

import joblib

results = []
trained_models = {}

depth_values = [1, 2, 3, 5, None]

for depth in depth_values:
    candidate = DecisionTreeClassifier(
        max_depth=depth,
        random_state=42
    )

    candidate.fit(X_train, y_train)

    train_score = candidate.score(X_train, y_train)
    test_score = candidate.score(X_test, y_test)

    results.append({
        "max_depth": str(depth),
        "train_accuracy": train_score,
        "test_accuracy": test_score,
        "gap": train_score - test_score
    })

    trained_models[depth] = candidate

comparison = pd.DataFrame(results)

REPORT_PATH = (
    Path(__file__).resolve().parent
    / "reports"
    / "model_comparison.csv"
)

REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
comparison.to_csv(REPORT_PATH, index=False)

print("\n--- PART D: DEPTH COMPARISON ---")
print(comparison.to_string(index=False))

best_test_accuracy = comparison["test_accuracy"].max()
best_index = comparison.index[
    comparison["test_accuracy"] == best_test_accuracy
][0]

best_depth = depth_values[best_index]
model = trained_models[best_depth]

print("\nSelected Depth:", best_depth)
print("Best Testing Accuracy:", best_test_accuracy)

print("\nModel Complexity Analysis:")

if (
    comparison.iloc[0]["train_accuracy"]
    < comparison["train_accuracy"].max()
    and comparison.iloc[0]["test_accuracy"]
    < best_test_accuracy
):
    print("Depth 1 shows possible underfitting.")
else:
    print("No clear underfitting evidence at depth 1.")

overfit_found = False

for i in range(len(comparison)):
    row = comparison.iloc[i]

    if (
        row["train_accuracy"] > comparison.iloc[best_index]["train_accuracy"]
        and row["test_accuracy"] < best_test_accuracy
    ):
        print(f"Depth {row['max_depth']} shows possible overfitting.")
        overfit_found = True

if not overfit_found:
    print("No clear overfitting evidence from this comparison.")

print(
    "\nLimitation: Reusing the test set to select a model "
    "can give an optimistic accuracy estimate."
)

MODEL_PATH = (
    Path(__file__).resolve().parent
    / "models"
    / "machine_predictor.joblib"
)

MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)

bundle = {
    "model": model,
    "features": FEATURES
}

joblib.dump(bundle, MODEL_PATH)

print("\nModel Saved Successfully!")
print("Saved Model Path:", MODEL_PATH)

loaded = joblib.load(MODEL_PATH)

test_predictions = model.predict(X_test)

reloaded_predictions = loaded["model"].predict(
    X_test[loaded["features"]]
)

assert (reloaded_predictions == test_predictions).all()

print("\nModel Reloaded Successfully!")
print("Reloaded Predictions Match Original Predictions!")

print("\nPart D Completed Successfully!")

# ==========================================
# PART E - Predictions, Debugging and Git
# ==========================================

new_machines = pd.DataFrame([
    {"temp_c": 98, "vibration": 6.5, "runtime": 14200, "pressure": 3.2},
    {"temp_c": 61, "vibration": 1.2, "runtime": 2700, "pressure": 6.7},
    {"temp_c": 81, "vibration": 3.8, "runtime": 8600, "pressure": 4.8},
])

feature_order = loaded["features"]

if set(new_machines.columns) != set(feature_order):
    raise ValueError("Prediction columns do not match training features.")

new_machines["predicted_fault"] = loaded["model"].predict(
    new_machines[feature_order]
)

print("\n--- PART E: NEW MACHINE PREDICTIONS ---")
print(new_machines.to_string(index=False))

print("\nPrediction Results:")

for i, prediction in enumerate(new_machines["predicted_fault"]):
    status = "Faulty" if prediction == 1 else "Normal"
    print(f"Machine {i + 1}: {status}")

# E2: Model fitting should use X_train, y_train (as in Parts C/D),
# never X_test, y_test.

print("\n--- E3: PREDICTION SCHEMA DEBUGGING ---")

incorrect_data = pd.DataFrame([
    {
        "tempc": 75,
        "vibration": 2.5,
        "runtime": 5000,
        "pressure": 5.2,
        "machine_id": "M001"
    }
])

print("\nIncorrect Columns:")
print(incorrect_data.columns.tolist())

corrected_data = incorrect_data.rename(
    columns={"tempc": "temp_c"}
)

corrected_data = corrected_data.drop(
    columns=["machine_id"]
)

if set(corrected_data.columns) != set(feature_order):
    raise ValueError("Prediction schema is incorrect.")

corrected_prediction = loaded["model"].predict(
    corrected_data[feature_order]
)

print("\nCorrected Columns:")
print(corrected_data.columns.tolist())

print("\nCorrected Prediction:", int(corrected_prediction[0]))

print("\nPart E Completed Successfully!")
print("Week 09 Machine Learning Pipeline Finished!")
