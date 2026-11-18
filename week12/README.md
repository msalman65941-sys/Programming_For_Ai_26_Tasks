
# Week 12 – Wholesale Customer Segmentation

## 1. Project Overview

This project applies Unsupervised Learning using K-Means clustering to segment wholesale customers based on their annual spending patterns.

The main objective is to identify groups of customers with similar spending behaviour and understand how these segments can support business decisions.

## 2. Dataset Information

- **Dataset:** Wholesale Customers
- **Source:** UCI Machine Learning Repository
- **Dataset Link:** https://archive.ics.uci.edu/dataset/292/wholesale+customers
- **Total Customers:** 440
- **Total Columns:** 8

The dataset contains six annual spending categories:

1. Fresh
2. Milk
3. Grocery
4. Frozen
5. Detergents_Paper
6. Delicassen

It also includes two categorical columns: Channel and Region.

Channel and Region are used for contextual analysis, not as clustering features.

## 3. Data Preprocessing

The following preprocessing steps were applied:

- Checked missing values and duplicate records.
- Verified numeric spending values.
- Checked that spending values were non-negative.
- Excluded customer identifiers from clustering.
- Excluded categorical columns from the spending features.
- Applied `log1p` transformation to reduce skewness.
- Applied `StandardScaler` to standardise the features.

The same fitted preprocessing pipeline is used for new customer assignments.

## 4. Clustering Method

K-Means clustering was used to group customers according to spending similarities.

- **Algorithm:** K-Means
- **Random State:** 42
- **Initialisations:** 10
- **Candidate k values:** 1 to 8
- **Final selected k:** [Enter your FINAL_K value]

The number of clusters was evaluated using:
- Elbow Method (Inertia)
- Silhouette Score
- Cluster sizes
- Spending profiles
- Business usefulness

## 5. Final Model and Analysis

The final model was used to:

- Assign customers to clusters.
- Calculate customer share and spending share.
- Analyse median and mean spending profiles.
- Compare Channel distribution across clusters.
- Visualise clusters using PCA.
- Check clustering agreement across different random seeds.

PCA was used to display the six-feature clustering in two dimensions.

## 6. Model Persistence

The trained preprocessing pipeline and K-Means model were saved together using Joblib.

**Model file:**

`models/wholesale_segments.joblib`

The saved bundle contains:
- Feature names
- Fitted preprocessing pipeline
- Trained K-Means model
- Selected number of clusters
- Spending unit information
- Scikit-learn version

The saved model was loaded again and its predictions were verified against the original cluster assignments.

## 7. New Customer Assignment

An illustrative new customer was created using the same six spending features.

The saved preprocessing pipeline transformed the customer's spending values, and the trained model assigned the customer to the nearest cluster.

This assignment indicates similarity to an existing segment, not a guaranteed business outcome.

## 8. Project Structure

```text
week12/
│
├── data/
│   └── wholesale_customers.csv
│
├── figures/
│   ├── spending_skew.png
│   ├── k_evaluation.png
│   └── pca_clusters.png
│
├── models/
│   └── wholesale_segments.joblib
│
├── reports/
│   ├── k_evaluation.csv
│   ├── clustered_customers.csv
│   ├── segment_summary.csv
│   ├── segment_medians.csv
│   ├── segment_means.csv
│   ├── channel_context.csv
│   ├── inverse_centers_mu.csv
│   ├── stability.csv
│   ├── k_decision.md
│   ├── business_action.md
│   └── debugging.md
│
└── README.md
```

## 9. Environment and Libraries

- Python: [Enter your Python version]
- Scikit-learn: [Enter your sklearn version]
- NumPy
- Pandas
- Matplotlib
- Joblib
- Jupyter Notebook
- VS Code

## 10. How to Run

From the existing course repository root, run:

```bash
uv run python week12/customer_segmentation_lab.py
```

The project uses the dependencies defined in `pyproject.toml` and `uv.lock`.

## 11. Limitations

This dataset contains annual aggregate spending only. It does not provide order dates, purchase frequency, item quantities, stockouts, campaign responses, or profit margins.

Therefore, this project does not establish a validated demand forecast, recommended reorder quantity, retention score, profitability ranking, or measured return on investment.

Business recommendations should be tested through a controlled pilot before implementation.

## 12. Conclusion

This project demonstrates how K-Means clustering can identify wholesale customer segments using spending behaviour. Data preprocessing, cluster evaluation, PCA visualisation, model persistence, and new customer assignment were performed as part of the workflow.

The resulting segments can support further business investigation, but their practical value requires validation with additional business data.
```

---

### 3 cheezein README mein zaroor update karna

1. `[Enter your FINAL_K value]` mein apna selected `k` likhna — tumne D1 mein 3 enter kiya tha, is liye agar final decision bhi 3 hai toh `3` likho.
2. Python version check karne ke liye terminal mein `python --version` run karo.
3. Scikit-learn version check karne ke liye:

```python
import sklearn
print(sklearn.__version__)
```

**Note:** README mein project structure tabhi final samajhna jab listed files actually create ho chuki hon. `customer_segmentation_lab.py` bhi ensure karna ke repository mein maujood ho.