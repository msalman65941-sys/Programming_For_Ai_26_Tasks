"""Run the patient dataset program."""

from pathlib import Path

from patient_dataset import PatientDataset


def main():
    """Audit and clean the patient records."""
    folder = Path(__file__).resolve().parent
    csv_path = folder / "data" / "patients_messy.csv"

    dataset = PatientDataset(csv_path)

    print("PATIENT DATASET AUDIT")
    print(dataset.audit())

    cleaned_data = dataset.cleaned()

    print("\nCLEANING COMPLETED")
    print("Original rows:", len(dataset.raw))
    print("Cleaned rows:", len(cleaned_data))
    print("Age values imputed:", cleaned_data["age_imputed"].sum())
    print("Heart-rate values imputed:", cleaned_data["heart_rate_imputed"].sum())

    dataset.save_audit(folder / "output" / "audit.json")

    cleaned_data.to_csv(folder / "output" / "patients_clean.csv", index=False)

    print("\nFiles saved successfully!")


if __name__ == "__main__":
    main()
