import pandas as pd

# Load students data
students = pd.read_csv(
    "week06/data/raw/students_messy.csv",
    na_values=["", "missing", "N/A", "-"]
)

# 1. Display first 5 rows
print("\n--- HEAD ---")
print(students.head())

# Display last 5 rows
print("\n--- TAIL ---")
print(students.tail())

# Display column names
print("\n--- COLUMNS ---")
print(students.columns)

# Display row and column count
print("\n--- SHAPE ---")
print("Rows:", students.shape[0])
print("Columns:", students.shape[1])

# 2. Display information about the dataset
print("\n--- INFO ---")
print(students.info())

# Display descriptive statistics
print("\n--- DESCRIBE ---")
print(students.describe(include="all"))

# 3. Missing values count
print("\n--- MISSING VALUES ---")
print(students.isna().sum())

# Exact duplicate count
print("\n--- EXACT DUPLICATES ---")
print("Exact duplicates:", students.duplicated().sum())

# Program labels
print("\n--- PROGRAM LABELS ---")
print(students["program"].unique())

# City labels
print("\n--- CITY LABELS ---")
print(students["city"].unique())