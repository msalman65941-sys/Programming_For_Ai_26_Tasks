# Week 09 – Introduction to Machine Learning with Scikit-learn

**Course:** Programming for AI (PFAI)  
**Lab:** Week 09  
**Topic:** Machine Learning with Scikit-learn  
**Algorithm:** Decision Tree Classifier  

---

## 1. Introduction

The objective of this lab is to understand the basic machine learning workflow using Python and scikit-learn.

A Decision Tree Classifier is used to predict whether a machine is operating normally or has a fault based on its operating conditions.

This lab covers data validation, feature selection, train-test splitting, model training, evaluation, model comparison, saving, loading, and making predictions.

## 2. Dataset Description

**Dataset Name:** `machines_ml.csv`

The dataset contains synthetic machine records used for binary classification.

**Total Records:** 160  
**Total Features Used:** 4  
**Target Column:** `fault`

### Input Features

| Feature | Description |
|---|---|
| temp_c | Machine temperature in Celsius |
| vibration | Machine vibration in mm/s |
| runtime | Machine operating hours |
| pressure | Machine pressure in bar |

### Target Variable

- **0:** Normal machine
- **1:** Faulty machine

The `machine_id` column is excluded because it is an identifier rather than a meaningful measurement for predicting machine faults.

## 3. Technologies and Libraries

The following technologies were used:

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- VS Code
- Git
- uv Package Manager

## 4. Part A – Data Loading and Validation

The dataset was loaded using Pandas.

The following validation steps were performed:

1. Checked whether all required columns were present.
2. Verified that the required columns contained no missing values.
3. Checked numerical data types.
4. Confirmed that the target contained only binary values (0 and 1).
5. Verified that both target classes were present.
6. Displayed the first five records.
7. Displayed feature ranges and class proportions.

**Result:** Dataset validation completed successfully.

## 5. Part B – Feature Selection and Train-Test Split

Four input features were selected:

`temp_c`, `vibration`, `runtime`, `pressure`

The target variable was `fault`.

The dataset was divided using the following configuration:

- Training Data: 75%
- Testing Data: 25%
- Random State: 42
- Stratified Sampling: Enabled

**Training Records:** 120  
**Testing Records:** 40

Stratified sampling maintains approximately similar class proportions in both datasets.

The random state ensures reproducibility of the train-test split.

**Result:** Train-test split verified successfully.

## 6. Part C – Model Training and Evaluation

A Decision Tree Classifier was trained using the training dataset.

**Baseline Model Configuration:**

- Algorithm: Decision Tree Classifier
- Maximum Depth: 3
- Random State: 42

### Model Accuracy

| Metric | Result |
|---|---|
| Training Accuracy | 89.17% |
| Testing Accuracy | 80.00% |
| Training-Testing Gap | 9.17 percentage points |

### Confusion Matrix

| | Predicted Normal | Predicted Fault |
|---|---|---|
| Actual Normal | 25 | 3 |
| Actual Fault | 5 | 7 |

### Confusion Matrix Interpretation

- **True Negative (TN):** 25 normal machines correctly predicted.
- **False Positive (FP):** 3 normal machines incorrectly classified as faulty.
- **False Negative (FN):** 5 faulty machines incorrectly classified as normal.
- **True Positive (TP):** 7 faulty machines correctly predicted.

### Manual Accuracy Verification

Accuracy = (TN + TP) / Total Predictions

Accuracy = (25 + 7) / 40

**Accuracy = 80.00%**

The manual accuracy matches the scikit-learn testing accuracy.

**Result:** Model training and evaluation completed successfully.

## 7. Part D – Model Depth Comparison

Different Decision Tree depths were tested to compare their performance.

### Depth Comparison Results

| Max Depth | Training Accuracy | Testing Accuracy | Gap |
|---|---|---|---|
| 1 | 80.83% | 80.00% | 0.83% |
| 2 | 80.83% | 80.00% | 0.83% |
| 3 | 89.17% | 80.00% | 9.17% |
| 5 | 99.17% | 82.50% | 16.67% |
| None | 100.00% | 82.50% | 17.50% |

### Selected Model

**Selected Depth:** 5

**Selected Model Training Accuracy:** 99.17%

**Selected Model Testing Accuracy:** 82.50%

Depth 5 was selected because it achieved the highest testing accuracy while being simpler than an unrestricted Decision Tree.

### Model Analysis

- Smaller tree depths may underfit the data.
- Larger tree depths increase model complexity.
- Depth 5 achieved the highest observed testing accuracy.
- The large training-testing accuracy gap suggests possible overfitting.
- Reusing the testing dataset for model selection can produce optimistic performance estimates.

**Result:** Model comparison completed successfully.

## 8. Model Saving and Loading

The selected trained model was saved using Joblib.

**Saved Model:** `models/machine_predictor.joblib`

The model bundle contains:

- Trained Decision Tree Classifier
- Ordered feature names

The saved model was reloaded and its predictions were compared with the original model predictions.

**Result:** Model reloaded successfully, and predictions matched.

## 9. Part E – Predictions on New Machines

Three hypothetical machine records were created for predictions.

| Machine | Temperature | Vibration | Runtime | Pressure |
|---|---|---|---|---|
| 1 | 98 | 6.5 | 14200 | 3.2 |
| 2 | 61 | 1.2 | 2700 | 6.7 |
| 3 | 81 | 3.8 | 8600 | 4.8 |

The saved model was used to predict whether each machine was normal or faulty.

The input feature names and their order were verified before prediction.

The prediction program displays:

- 0 = Normal
- 1 = Faulty

**Result:** New machine predictions completed successfully.

## 10. Debugging

Two debugging scenarios were examined.

### E2 – Incorrect Model Training

**Problem:** Training the model using testing data.

**Cause:** Using testing data for training contaminates the evaluation.

**Correction:** Train the model using `X_train` and `y_train`.

### E3 – Incorrect Prediction Features

**Problem:** Incorrect or extra input feature names.

**Cause:** The input contained `tempc` instead of `temp_c` and an unnecessary `machine_id` column.

**Correction:** Rename the incorrect column and remove the extra column before prediction.

Detailed debugging information is documented in `reports/debugging.md`.

## 11. Project Structure

**Main Folder:** `Programming-for-AI-2026/week09/`

- `ml_pipeline.py` – Complete machine learning pipeline.
- `README.md` – Lab documentation.
- `data/machines_ml.csv` – Machine dataset.
- `models/machine_predictor.joblib` – Saved trained model.
- `reports/model_comparison.csv` – Tree depth comparison results.
- `reports/debugging.md` – Debugging documentation.

## 12. How to Run the Project

Open the existing Programming-for-AI-2026 project in VS Code.

Use the existing shared Python environment.

Install scikit-learn from the project root if it is not already installed:

`uv add scikit-learn`

Run the complete lab program from the project root:

`uv run python week09/ml_pipeline.py`

The program loads and validates the dataset, trains and evaluates the classifier, compares different tree depths, saves the selected model, and predicts new machine records.

## 13. Limitations

- The dataset contains synthetic machine records.
- The dataset may not represent real-world industrial conditions.
- Accuracy alone does not fully describe model performance.
- False negatives may be dangerous because faulty machines could be classified as normal.
- A single train-test split is insufficient to establish model reliability.
- Model selection using the test set may introduce optimistic evaluation results.
- Additional validation and real-world testing would be required before deployment.

## 14. Responsible AI Considerations

Machine learning predictions should not be treated as guaranteed results.

Predictions should be reviewed by qualified personnel before making safety-critical decisions.

Data quality, model limitations, privacy, and the consequences of incorrect predictions must be considered.

## 15. Conclusion

In this lab, a complete machine learning classification pipeline was implemented using Python and scikit-learn.

A Decision Tree Classifier was trained and evaluated using machine operating data.

The baseline model achieved 80.00% testing accuracy, while the selected depth-5 model achieved 82.50% testing accuracy.

The trained model was successfully saved, reloaded, and used for new predictions.

This lab provided practical experience with data validation, classification, model evaluation, overfitting, model persistence, and responsible machine learning.