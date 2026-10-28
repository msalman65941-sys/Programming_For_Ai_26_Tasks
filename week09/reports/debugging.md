
# Week 09 - Debugging Report

## E2 - Fitting on Test Set

Problem:
Model was trained using testing data.

Incorrect Code:
model.fit(X_test, y_test)

Cause:
Using test data for training causes data leakage
and makes evaluation unreliable.

Correction:
model.fit(X_train, y_train)

## E3 - Prediction Schema

Problem:
Input data contains incorrect and extra columns.

Cause:
Column "tempc" is misspelled and "machine_id"
is an unnecessary extra column.

Correction:
Rename "tempc" to "temp_c" and remove
"machine_id" before making predictions.

Result:
The corrected data matches the training
features and predictions run successfully.
