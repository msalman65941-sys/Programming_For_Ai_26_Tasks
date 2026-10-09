"""Test the PatientDataset class using simple assertions."""

from pathlib import Path
import pandas as pd

from patient_dataset import PatientDataset

print("Current folder:", Path(__file__).parent)
print("Data folder exists:", (Path(__file__).parent / "data").exists())
print("CSV file exists:", (Path(__file__).parent / "data" / "patients_messy.csv").exists())

# Get the existing patient CSV file
csv_path = Path(__file__).parent / "data" / "patients_messy.csv"

dataset = PatientDataset(csv_path)

# Test 1: Check dataset loading
assert len(dataset.raw) == 100
print("Test 1 passed: Dataset loaded successfully.")

# Test 2: Check required columns
dataset.validate_required(["patient_id", "age", "heart_rate", "department"])
print("Test 2 passed: Required columns exist.")

# Test 3: Check audit report
report = dataset.audit()

assert report["row_count"] == 100
assert report["column_count"] == 4
assert report["exact_duplicate_count"] == 1

print("Test 3 passed: Audit results are correct.")

# Test 4: Check invalid values
assert report["invalid_value_counts"]["age"] == 4
assert report["invalid_value_counts"]["heart_rate"] == 2

print("Test 4 passed: Invalid values counted.")

# Test 5: Check cleaning
original = dataset.raw.copy(deep=True)
cleaned = dataset.cleaned()

assert len(cleaned) == 99
assert cleaned["patient_id"].isna().sum() == 0
assert cleaned["patient_id"].duplicated().sum() == 0

print("Test 5 passed: Duplicate rows removed and IDs checked.")

# Test 6: Check missing values after cleaning
assert cleaned["age"].isna().sum() == 0
assert cleaned["heart_rate"].isna().sum() == 0

print("Test 6 passed: Missing numeric values handled.")

# Test 7: Check department standardization
assert "GENERAL MEDICINE" in cleaned["department"].values
assert "CARDIOLOGY" in cleaned["department"].values

print("Test 7 passed: Department names standardized.")

# Test 8: Check original data remains unchanged
pd.testing.assert_frame_equal(dataset.raw, original)

print("Test 8 passed: Original data remains unchanged.")

# Test 9: Check audit report saving
output_path = Path(__file__).parent / "audit_test.json"
dataset.save_audit(output_path)

assert output_path.exists()

print("Test 9 passed: Audit report saved successfully.")

print("\nAll tests passed successfully!")
