
# Week 10 Lab - Debugging Report

## 1. Data Leakage

**Problem:** Validation or test information affects model training.

**Cause:** StandardScaler is fitted on the complete dataset before cross-validation.

**Correction:** Keep StandardScaler inside the pipeline so it learns only from the training fold.

## 2. Unfair Model Comparison

**Problem:** Models are evaluated using different data or validation folds.

**Cause:** Different train/test splits or folds are used for different models.

**Correction:** Use the same X_dev, y_dev, and five validation folds for every model. Do not use X_test for model selection.

## 3. Metric Meaning

**Problem:** Spam classification results are interpreted incorrectly.

**Cause:** Confusion between positive and negative class labels.

**Correction:** Use 0 = legitimate and 1 = spam. A false positive marks legitimate email as spam, while a false negative misses actual spam.

## 4. Feature Schema Mismatch

**Problem:** The saved model receives incorrect or missing input features.

**Cause:** Feature columns are missing or arranged in the wrong order.

**Correction:** Use all 57 features in the saved order before calling predict().

## Conclusion

The lab uses consistent validation folds, preprocessing pipelines, correct class labels, and a saved feature schema to ensure reliable and reproducible results.
