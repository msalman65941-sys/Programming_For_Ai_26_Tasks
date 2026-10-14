# Assignment 2 — Student Dataset Audit Toolkit

## 1. Program Description

This project implements a reusable Python class called `PatientDataset` to load, audit, and clean a synthetic patient dataset using Pandas.

The program identifies missing values, exact duplicate rows, repeated patient IDs, invalid numeric values, nonnumeric entries, and inconsistent department labels. It returns a cleaned DataFrame and saves an audit summary in JSON format.

This project is only a data-quality auditing exercise. It is not a medical diagnostic system.

## 2. Files and Folders

* `patient_dataset.py`: Contains the `PatientDataset` class and its methods.
* `demo.py`: Runs the program, displays the audit and cleaned data, and saves the output files.
* `test_patient_dataset.py`: Tests the program using ordinary Python assertions.
* `data/patients_messy.csv`: The supplied dataset containing 100 original records. This file remains unchanged.
* `data/personal_cases.csv`: Contains additional synthetic records for personal testing.
* `output/audit.json`: Contains the audit summary of the original dataset.
* `output/patients_clean.csv`: Contains the cleaned patient records.
* `README.md`: Documents the program, its rules, and testing results.
* `AI_USE.md`: Records the use of AI tools and the verification process.

## 3. Validation Rules

The program requires four columns:

* `patient_id`
* `age`
* `heart_rate`
* `department`

The patient ID must not be missing or empty, and it must be unique after exact duplicate rows are removed.

Age must be between 0 and 120 inclusive. Heart rate must be between 30 and 220 inclusive. Values outside these ranges are treated as invalid for this programming exercise.

## 4. Data Cleaning Rules

The program follows these steps:

1. Load the CSV file and recognize empty strings, `missing`, `N/A`, and `-` as missing-value markers.
2. Check that all required columns are present.
3. Create a deep copy of the original DataFrame.
4. Remove exact duplicate rows and reset the index.
5. Remove surrounding spaces from patient IDs and check for missing, empty, or repeated IDs.
6. Standardize department labels.
7. Replace missing or empty department values with `Unknown`.
8. Convert age and heart rate to numeric values. Nonnumeric entries become missing values.
9. Replace out-of-range numeric values with missing values.
10. Create Boolean imputation flags before filling missing numeric values.
11. Fill missing numeric values using the median of valid values in the same column.
12. Return the cleaned DataFrame without changing the original data.

## 5. Department Standardization

The following department labels are standardized:

| Original label | Standardized label |
| -------------- | ------------------ |
| GEN MED        | GENERAL MEDICINE   |
| GENERAL MED    | GENERAL MEDICINE   |
| GENERAL-MED    | GENERAL MEDICINE   |
| CARDIO         | CARDIOLOGY         |
| NEUROLOGY      | NEUROLOGY          |
| ORTHOPEDICS    | ORTHOPEDICS        |

Department labels are stripped of surrounding spaces and converted to uppercase before mapping.

## 6. Running the Program

Run these commands from the repository root using the existing course environment:

```bash
uv run python Assignment_02/demo.py
```

Run the tests:

```bash
uv run python Assignment_02/test_patient_dataset.py
```

The test program should display:

```text
All tests passed.
```

## 7. Expected Results for the Supplied Dataset

The assignment specifies the following results for `patients_messy.csv`.

| Audit or cleaning check                           | Expected result |
| ------------------------------------------------- | --------------: |
| Original rows                                     |             100 |
| Original columns                                  |               4 |
| Exact duplicate rows                              |               1 |
| Repeated ID occurrences after exact deduplication |               0 |
| Invalid age values                                |               4 |
| Invalid heart-rate values                         |               2 |
| Nonnumeric age entries                            |               1 |
| Nonnumeric heart-rate entries                     |               1 |
| Cleaned rows                                      |              99 |
| Median used for age filling                       |              52 |
| Median used for heart-rate filling                |            80.5 |
| `age_imputed` count                               |              11 |
| `heart_rate_imputed` count                        |               9 |

**Actual results:** The test script displayed `All tests passed.` The demonstration program was also run. The values in the generated audit and cleaned files should be checked against the expected results above.

## 8. Personal Test Cases: Predictions and Results

The personal dataset contains additional synthetic records for testing boundaries, missing values, nonnumeric entries, invalid numeric values, and department standardization.

Before running the program, I will calculate the expected median using only valid numeric values and predict the cleaning results.

| Test                       | Prediction before running                                                  | Actual result                      |
| -------------------------- | -------------------------------------------------------------------------- | ---------------------------------- |
| Invalid numeric values     | Out-of-range values will be replaced with missing values before filling.   | To be recorded after verification. |
| Median filling             | Each missing numeric value will be filled using its column's valid median. | To be recorded after verification. |
| Department standardization | `GEN MED` will become `GENERAL MEDICINE`.                                  | To be recorded after verification. |

The actual results must be recorded after running the program with `personal_cases.csv`. Any incorrect prediction will be kept and explained rather than changed to match the output.

## 9. Five Important Programming Decisions

### 1. Why does `cleaned()` start with a deep copy?

A deep copy creates an independent DataFrame. Cleaning operations can then be performed without changing the original data stored in `self.raw`. This is important because the original data is needed for auditing.

### 2. Why are exact duplicates removed before checking repeated IDs?

An exact duplicate is a repeated copy of the same complete record. Removing it first prevents it from being incorrectly treated as a conflicting patient record. If the same ID appears in different records after deduplication, the program raises an error so the records can be investigated.

### 3. What does `errors="coerce"` do?

When Pandas converts a column to numeric values, `errors="coerce"` changes entries that cannot be converted into numbers to missing values. These values can then be identified and handled during cleaning.

### 4. Why are invalid numeric values excluded before calculating medians?

Values outside the assignment's allowed ranges are not considered valid for filling missing values. If these invalid values were included, they could distort the median. The program therefore replaces invalid values with missing values before calculating the median.

### 5. Why are imputation flags important?

The `age_imputed` and `heart_rate_imputed` columns identify records where the original numeric value was missing, nonnumeric, or invalid. These flags help reviewers distinguish substituted values from observed values.

## 10. Known Limitations

1. Department standardization uses a fixed set of mappings. Other spelling variations may require additional mappings.
2. Median filling substitutes missing values and can reduce variation in the dataset.
3. The program cannot determine the correct value for a conflicting patient ID without additional source information.
4. The numeric ranges are fixed for this classroom exercise and are not medical diagnostic rules.

## 11. Conclusion

This assignment demonstrates Python classes, methods, file handling, exception handling, Pandas data inspection and cleaning, JSON export, and assertion-based testing. The program preserves the original dataset, identifies data-quality issues, and produces a separate cleaned dataset for review.
