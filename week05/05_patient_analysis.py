import numpy as np

patient_data = np.array([
    [101, 45, 38.5, 100, 92],
    [102, 23, 36.8, 75, 98],
    [103, 67, 39.1, 110, 89],
    [104, 54, 37.0, 80, 96],
    [105, 34, 38.0, 95, 93],
    [106, 72, 36.5, 70, 97],
], dtype=float)


# 1. Display array information
print("Shape:", patient_data.shape)
print("Dimensions:", patient_data.ndim)
print("Size:", patient_data.size)
print("Data type:", patient_data.dtype)


# 2. Separate patient IDs and clinical features
patient_ids = patient_data[:, 0].astype(int)
clinical_features = patient_data[:, 1:]

print("\nPatient IDs:")
print(patient_ids)

print("Clinical features:")
print(clinical_features)


# 3. Average age and mean of every clinical feature
average_age = clinical_features[:, 0].mean()
feature_means = clinical_features.mean(axis=0)

print("\nAverage age:", average_age)
print("Mean of clinical features:", feature_means)


# 4. Select patients older than 60,
# hotter than 38°C, and oxygen below 94%
selected = patient_data[
    (patient_data[:, 1] > 60) &
    (patient_data[:, 2] > 38) &
    (patient_data[:, 4] < 94)
]

print("\nSelected patients:")
print(selected)


# 5. High-risk mask
high_risk_mask = (
    (patient_data[:, 2] > 38) &
    (patient_data[:, 4] < 94)
)

high_risk_ids = patient_ids[high_risk_mask]

print("\nHigh-risk mask:")
print(high_risk_mask)

print("High-risk count:", high_risk_mask.sum())
print("High-risk IDs:", high_risk_ids)


# 6. Normalize only clinical features
feature_min = clinical_features.min(axis=0)
feature_max = clinical_features.max(axis=0)

normalized_features = (
    (clinical_features - feature_min) /
    (feature_max - feature_min)
)

print("\nNormalized feature matrix:")
print(normalized_features)
print("Normalized shape:", normalized_features.shape)


# Required tests
print("\nTests:")
print("Shape is (6, 4):", normalized_features.shape == (6, 4))
print("Values between 0 and 1:",
      np.all((normalized_features >= 0) & (normalized_features <= 1)))

print("Original data unchanged:")
print(patient_data)

print("High-risk IDs are integers:",
      np.issubdtype(high_risk_ids.dtype, np.integer))

# Save and reload
# Save one NumPy array in binary format, preserving its shape and data type.
np.save("week05/data/patient_data.npy", patient_data)

# Load the saved NumPy array. 
loaded_npy = np.load("week05/data/patient_data.npy")

# Save normalized features as readable CSV values with four decimal places. 
np.savetxt(
    "week05/output/normalized_features.csv",
    normalized_features,
    delimiter=",",
    fmt="%.4f"
)

# Load numerical values from the CSV file. 
loaded_csv = np.loadtxt(
    "week05/output/normalized_features.csv",
    delimiter=","
)

# Verification
print("\nSave and Reload Verification:")
print("Numpy file exact match:",
      np.array_equal(patient_data, loaded_npy))

print("CSV values match:",
      np.allclose(normalized_features, loaded_csv))