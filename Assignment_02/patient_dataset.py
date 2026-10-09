"""Load, audit, and clean a patient dataset."""

import json
from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = ["patient_id", "age", "heart_rate", "department"]


class PatientDataset:
    """Load, audit, and clean patient records."""

    def __init__(self, path):
        """Load the CSV file and keep the original data."""
        self.path = Path(path)

        self.raw = pd.read_csv(
            self.path,
            na_values=["", "missing", "N/A", "-"],
            dtype={"patient_id": "string"},
        )

    def validate_required(self, columns):
        """Check whether all required columns exist."""
        missing_columns = []

        for column in columns:
            if column not in self.raw.columns:
                missing_columns.append(column)

        if len(missing_columns) > 0:
            raise ValueError(f"Missing required columns: {missing_columns}")

    def audit(self):
        """Return a summary of problems in original data."""
        self.validate_required(REQUIRED_COLUMNS)

        report = {}

        report["row_count"] = int(len(self.raw))
        report["column_count"] = int(len(self.raw.columns))

        report["missing_counts"] = {}

        for column in self.raw.columns:
            report["missing_counts"][column] = int(self.raw[column].isna().sum())

        report["exact_duplicate_count"] = int(self.raw.duplicated().sum())

        data = self.raw.drop_duplicates()

        report["repeated_id_count"] = int(data["patient_id"].duplicated().sum())

        report["invalid_value_counts"] = {}
        report["nonnumeric_counts"] = {}

        for column in ["age", "heart_rate"]:
            numbers = pd.to_numeric(self.raw[column], errors="coerce")

            nonnumeric = self.raw[column].notna() & numbers.isna()

            report["nonnumeric_counts"][column] = int(nonnumeric.sum())

            if column == "age":
                invalid = (numbers < 0) | (numbers > 120)
            else:
                invalid = (numbers < 30) | (numbers > 220)

            invalid = invalid & numbers.notna()

            report["invalid_value_counts"][column] = int(invalid.sum())

        labels = self.raw["department"].dropna().unique()

        report["department_labels"] = []

        for label in labels:
            report["department_labels"].append(str(label))

        report["department_labels"].sort()

        return report

    def cleaned(self):
        """Return a cleaned copy without changing original data."""
        self.validate_required(REQUIRED_COLUMNS)

        data = self.raw.copy(deep=True)

        data = data.drop_duplicates()
        data = data.reset_index(drop=True)

        data["patient_id"] = data["patient_id"].str.strip()

        if data["patient_id"].isna().any():
            raise ValueError("Patient ID cannot be missing.")

        if data["patient_id"].eq("").any():
            raise ValueError("Patient ID cannot be empty.")

        if data["patient_id"].duplicated().any():
            raise ValueError("Repeated patient IDs found.")

        data["department"] = data["department"].astype("string").str.strip()

        data["department"] = data["department"].str.upper()

        data["department"] = data["department"].replace(
            {
                "GEN MED": "GENERAL MEDICINE",
                "GENERAL MED": "GENERAL MEDICINE",
                "GENERAL-MED": "GENERAL MEDICINE",
                "CARDIO": "CARDIOLOGY",
            }
        )

        data["department"] = data["department"].fillna("Unknown")
        data["department"] = data["department"].replace("", "Unknown")

        for column in ["age", "heart_rate"]:
            data[column] = pd.to_numeric(data[column], errors="coerce")

            if column == "age":
                invalid = (data[column] < 0) | (data[column] > 120)
            else:
                invalid = (data[column] < 30) | (data[column] > 220)

            data.loc[invalid, column] = float("nan")

            flag = column + "_imputed"
            data[flag] = data[column].isna()

            median_value = data[column].median()

            if pd.isna(median_value):
                raise ValueError(f"No valid values for {column} median.")

            data[column] = data[column].fillna(median_value)

        return data

    def save_audit(self, path):
        """Save the original data audit as a JSON file."""
        output_path = Path(path)

        output_path.parent.mkdir(parents=True, exist_ok=True)

        report = self.audit()

        with output_path.open("w", encoding="utf-8") as file:
            json.dump(report, file, indent=4)
