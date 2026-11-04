
# Week 10 Lab — Comparing Classification Algorithms with Spambase

**Course:** Programming for AI  
**Program:** BS Artificial Intelligence  
**Lab:** Week 10 — Classification Algorithms Comparison  
**Dataset:** UCI Spambase  
**Main File:** `compare_classifiers.py`

---

## 1. Introduction

This lab compares four machine learning classification algorithms using the Spambase email dataset.

The main objective is to classify emails as spam or legitimate and compare the performance of different algorithms.

The algorithms used are:

1. Decision Tree
2. k-Nearest Neighbors (k-NN)
3. Logistic Regression
4. Gaussian Naive Bayes
5. Majority Baseline

The models are compared using five-fold cross-validation and evaluated using accuracy, precision, recall, and F1-score.

---

## 2. Dataset Information

**Dataset Name:** Spambase  
**Source:** UCI Machine Learning Repository  
**Dataset URL:** https://archive.ics.uci.edu/dataset/94/spambase

Spambase contains numerical characteristics of emails.

### Dataset Features

- 48 word-frequency features
- 6 character-frequency features
- 3 capital-letter run statistics
- Total input features: 57

### Target Variable

- 0 = Legitimate Email
- 1 = Spam Email

The target column is named `is_spam` and is not included in the input features.

---

## 3. Data Cleaning

Before training the models, the dataset was inspected and cleaned.

### Cleaning Results

| Description | Count |
|---|---:|
| Original Records | 4601 |
| Total Input Features | 57 |
| Missing Values | 0 |
| Exact Duplicate Rows Removed | 391 |
| Ambiguous Rows Excluded | 6 |
| Final Clean Records | 4204 |

### Class Distribution

| Class | Number of Emails | Percentage |
|---|---:|---:|
| Legitimate (0) | 2528 | 60.1% |
| Spam (1) | 1676 | 39.9% |

### Cleaning Rules

1. Checked missing and infinite values.
2. Verified all features were numeric.
3. Removed exact duplicate rows.
4. Excluded feature-identical records having conflicting labels.
5. Preserved the original dataset archive.

Duplicate and ambiguous records were removed to make the comparison consistent and prevent identical feature patterns from crossing the data split.

Opposite labels for identical feature summaries do not necessarily mean the original labels were incorrect.

---

## 4. Train-Test Split

The cleaned dataset was divided into development and testing sets.

- Development Data: 75%
- Testing Data: 25%
- Random State: 42
- Stratification: Enabled

### Split Results

| Dataset | Total | Legitimate | Spam |
|---|---:|---:|---:|
| Development | 3153 | 1896 | 1257 |
| Testing | 1051 | 632 | 419 |

The `train_test_split()` function was used with `stratify=y`.

Stratification helps maintain similar class proportions in both datasets.

The reserved test dataset was not used during model selection.

---

## 5. Classification Algorithms

### 5.1 Decision Tree

Decision Tree classifies emails using rule-based decisions.

Configuration:
- Maximum Depth: 4
- Random State: 42

### 5.2 k-Nearest Neighbors

k-NN classifies emails based on nearby examples.

Configuration:
- Number of Neighbors: 5
- StandardScaler used

### 5.3 Logistic Regression

Logistic Regression models the probability of an email belonging to a class.

Configuration:
- Maximum Iterations: 2000
- StandardScaler used

### 5.4 Gaussian Naive Bayes

Gaussian Naive Bayes uses probability distributions to classify emails.

Configuration:
- GaussianNB
- No scaling required for this lab

### 5.5 Majority Baseline

The Majority Baseline always predicts the most common training class.

It provides a basic reference for comparing the other classifiers.

---

## 6. Machine Learning Pipelines

Scikit-learn pipelines were used to combine preprocessing and classification.

StandardScaler was included inside the pipelines for:

- k-Nearest Neighbors
- Logistic Regression

Keeping scaling inside the pipeline prevents data leakage during cross-validation.

The scaler learns only from the training portion of each validation fold.

---

## 7. Cross-Validation

Five-fold stratified cross-validation was used.

Configuration:

- Number of Folds: 5
- Shuffle: True
- Random State: 42
- Same validation folds for every model

Each model was evaluated using:

1. Accuracy
2. Precision
3. Recall
4. F1-score

The mean and sample standard deviation of each metric were calculated.

The selection rule was the highest unrounded mean cross-validation F1-score.

In an exact tie, the alphabetically first model name would be selected.

---

## 8. Model Comparison Results

### Five-Fold Cross-Validation Results

| Model | Accuracy | Precision | Recall | F1 |
|---|---:|---:|---:|---:|
| Logistic Regression | 0.923 | 0.920 | 0.884 | 0.901 |
| Decision Tree | 0.893 | 0.912 | 0.811 | 0.858 |
| k-NN | 0.890 | 0.886 | 0.831 | 0.858 |
| Gaussian NB | 0.826 | 0.712 | 0.951 | 0.814 |
| Majority Baseline | 0.601 | 0.000 | 0.000 | 0.000 |

### Cross-Validation Standard Deviations

| Model | Accuracy SD | Precision SD | Recall SD | F1 SD |
|---|---:|---:|---:|---:|
| Logistic Regression | 0.007 | 0.017 | 0.010 | 0.008 |
| Decision Tree | 0.015 | 0.039 | 0.009 | 0.017 |
| k-NN | 0.022 | 0.032 | 0.028 | 0.029 |
| Gaussian NB | 0.020 | 0.026 | 0.013 | 0.017 |
| Majority Baseline | 0.001 | 0.000 | 0.000 | 0.000 |

The values above are rounded for display. The original unrounded values are saved in `reports/model_comparison.csv`.

### Observations

- Logistic Regression achieved the highest mean F1-score of 0.901.
- Logistic Regression also achieved the highest accuracy.
- Gaussian NB achieved the highest recall of 0.951.
- Gaussian NB had lower precision than Logistic Regression.
- All four classification algorithms outperformed the majority baseline on F1-score.

The standard deviations show variation between validation folds.

---

## 9. Best Model Selection

**Selected Model: Logistic Regression**

Logistic Regression was selected because it achieved the highest mean cross-validation F1-score.

Validation performance:

- Accuracy: 92.3%
- Precision: 92.0%
- Recall: 88.4%
- F1-score: 90.1%

A fresh copy of the selected model was trained on all 3153 development records.

The final test set was used only after model selection.

---

## 10. Final Test Results

The selected Logistic Regression model was evaluated on 1051 reserved test records.

| Metric | Final Score |
|---|---:|
| Accuracy | 0.924 |
| Precision | 0.908 |
| Recall | 0.900 |
| F1-score | 0.904 |

### Interpretation

- Accuracy: 92.4% of test emails were correctly classified.
- Precision: 90.8% of predicted spam emails were actually spam.
- Recall: Approximately 90.0% of actual spam emails were detected.
- F1-score: 90.4%, indicating a good balance between precision and recall.

The final results are saved in:

`reports/final_test_metrics.csv`

---

## 11. Confusion Matrix

The confusion matrix shows correct and incorrect predictions.

| Actual / Predicted | Legitimate (0) | Spam (1) |
|---|---:|---:|
| Legitimate (0) | 594 | 38 |
| Spam (1) | 42 | 377 |

### Explanation

**True Negative (TN): 594**

Legitimate emails correctly predicted as legitimate.

**False Positive (FP): 38**

Legitimate emails incorrectly predicted as spam.

**False Negative (FN): 42**

Spam emails incorrectly predicted as legitimate.

**True Positive (TP): 377**

Spam emails correctly predicted as spam.

### Summary

- Correct Predictions: 971
- Incorrect Predictions: 80
- Total Test Records: 1051

False positives may block important legitimate emails.

False negatives may allow spam emails to reach users.

The confusion matrix is saved in:

`reports/confusion_matrix.csv`

---

## 12. Data Visualization

A bar chart was generated to compare the classification algorithms.

The chart displays:

- Accuracy
- Precision
- Recall
- F1-score

The chart uses a 0–1 vertical axis.

Saved Figure:

`figures/model_comparison.png`

The graph demonstrates that Logistic Regression achieved the highest mean validation F1-score.

---

## 13. Model Saving and Loading

The selected model was saved using Joblib.

Saved Model:

`models/spam_predictor.joblib`

The saved bundle contains:

- Trained classification model
- Ordered list of 57 input features
- Target label mapping
- Selected model name
- Scikit-learn version

After loading the saved model, its predictions were compared with the original model predictions.

Both sets of predictions matched successfully.

Only trusted Joblib files should be loaded because deserialization can execute code.

---

## 14. Email Prediction Test

One record from the reserved test dataset was selected to demonstrate prediction.

### Actual Output

Predicted: legitimate

Actual: legitimate

### Result

The model correctly predicted the selected email as legitimate.

The model requires 57 numerical input features and does not directly process raw email text.

---

## 15. Debugging

Four important debugging situations were documented.

### 1. Data Leakage

Problem: Validation or test data influences model training.

Solution: Keep StandardScaler inside the model pipeline.

### 2. Unfair Comparison

Problem: Different models use different evaluation conditions.

Solution: Use identical development data, validation folds, and metrics.

### 3. Metric Interpretation

Problem: Confusion between spam and legitimate class labels.

Solution: Use 0 for legitimate and 1 for spam consistently.

### 4. Feature Schema Mismatch

Problem: Missing or incorrectly ordered features affect predictions.

Solution: Use all 57 features in their saved order.

Detailed explanations are available in:

`reports/debugging.md`

---

## 16. Project Structure

Programming-for-AI-2026/

    week10/
        README.md
        compare_classifiers.py
        compare_classifiers.ipynb

        data/
            spambase.zip

        figures/
            model_comparison.png

        models/
            spam_predictor.joblib

        reports/
            model_comparison.csv
            final_test_metrics.csv
            confusion_matrix.csv
            debugging.md

The shared virtual environment, pyproject.toml, uv.lock, and Git repository remain in the course root.

The main lab implementation is in `compare_classifiers.py`.

---

## 17. How to Run the Project

### Step 1

Open the `Programming-for-AI-2026` folder in VS Code.

### Step 2

Verify the installed scikit-learn version:

    uv run python -c "import sklearn; print(sklearn.__version__)"

Scikit-learn version used:

**Replace this line with your installed version.**

### Step 3

Run the main Python script from the course root:

    uv run python week10/compare_classifiers.py

### Step 4

Check the generated outputs:

- Model comparison CSV
- Final test metrics CSV
- Confusion matrix CSV
- Model comparison graph
- Saved trained model

The supplied Spambase archive is loaded locally from `week10/data/spambase.zip`.

If the archive is missing, the script attempts to download it from UCI.

---

## 18. Limitations

This experiment has several limitations.

1. Spambase is a historical dataset donated in 1999.
2. Modern email patterns may differ from historical email patterns.
3. Duplicate removal and ambiguous-row exclusion change the evaluated dataset.
4. The model only accepts numerical email features, not raw email messages.
5. The highest F1-score does not necessarily mean the highest precision or recall.
6. Five-fold standard deviations do not provide formal confidence intervals.
7. The test results do not guarantee production performance.

This experiment is intended for educational purposes rather than production email filtering.

---

## 19. Reflection

### Q1. Why might the highest F1 model differ from the highest precision model?

F1 balances precision and recall, while precision only measures how many positive predictions are correct.

### Q2. Why must StandardScaler be inside the pipeline?

It prevents data leakage by fitting the scaler only on the training portion of each cross-validation fold.

### Q3. How can duplicate rows and historical patterns affect evaluation?

Duplicate rows may create overly optimistic results, while historical patterns may not represent modern email behavior.

---

## 20. Conclusion

In this lab, four machine learning classification algorithms and a majority baseline were compared using the UCI Spambase dataset.

The dataset was cleaned, divided into development and testing sets, and evaluated using five-fold stratified cross-validation.

Logistic Regression achieved the highest mean validation F1-score and was selected as the best model.

### Final Performance

- Accuracy: 92.4%
- Precision: 90.8%
- Recall: 90.0%
- F1-score: 90.4%

The trained model was successfully saved, reloaded, and tested on a held-out email record.

The experiment demonstrates the importance of fair model comparison, preprocessing pipelines, cross-validation, proper evaluation, and model persistence.

---

## 21. Git Commands

Run these commands from the existing course repository root:

    git status

    git add week10 pyproject.toml uv.lock

    git commit -m "Complete Week 10 Spambase validation and persistence"

    git log --oneline -10

No separate Git repository or virtual environment is required inside week10.

---

**Lab Status:** Implementation and evaluation completed successfully.
