# Programming for Artificial Intelligence (PFAI) — Coursework Repository

A week-by-week collection of Python programming exercises, practical notebooks, data analysis labs, and introductory machine-learning projects completed as part of the **Programming for Artificial Intelligence (PFAI)** coursework.

The repository documents a progression from Python fundamentals to data manipulation, visualization, supervised learning, regression, and unsupervised customer segmentation.

## Repository Overview

| Weeks / Area | Topics and practical work |
|---|---|
| Week 1 | Python introduction, input/output, variables, calculations, and simple programs |
| Week 2 | Conditions, loops, control flow, comprehensions, patterns, and debugging |
| Week 3 | Functions, modular programming, exception handling, testing, and refactoring |
| Week 4 | Object-Oriented Programming, classes, inheritance, file handling, and experiment tracking |
| Week 5 | NumPy arrays, indexing, shapes, copies, vectorization, and numerical analysis |
| Week 6 | Pandas, CSV data cleaning, missing/invalid records, grouping, and summaries |
| Week 7 | Data visualization and dashboard-style reporting |
| Week 9 | Machine-learning workflow with a Decision Tree classifier |
| Week 10 | Comparing classification algorithms using the Spambase dataset |
| Week 11 | Regression analysis using the concrete strength dataset |
| Week 12 | Unsupervised learning and K-Means customer segmentation |

*The overview reflects the week folders and materials currently present in this repository.*

## Weekly Topics & Practical Work

### Week 1 — Python Fundamentals
- Writing and running Python programs.
- Printing output and taking user input.
- Variables, data types, and arithmetic expressions.
- Temperature conversion and area calculations.
- Basic calculator, BMI, age, currency, percentage, and bill programs.
- Introductory Jupyter Notebook practice.

### Week 2 — Control Flow & Problem Solving
- Conditional statements and decision-making.
- Loops and tracing program execution.
- Voting and BMI classification examples.
- Summation and multiplication-table programs.
- `break` and `continue`.
- Pattern printing and comprehensions.
- Marks analysis, traffic signal logic, and debugging.

### Week 3 — Functions, Exceptions & Testing
- Defining and calling functions.
- Returning values and reusable program logic.
- Student summary and grade calculation.
- Exception handling.
- Separating utility functions into modules.
- Testing helper functions.
- Debugging and refactoring code.

### Week 4 — Object-Oriented Programming & File Handling
- Classes, objects, attributes, and methods.
- Constructors and validation.
- Inheritance and method overriding.
- Student record management.
- CSV and JSON data storage.
- Text-file reports.
- Experiment records and experiment tracking.
- Debugging object-oriented programs.

### Week 5 — NumPy
- Creating and working with NumPy arrays.
- Array indexing and slicing.
- Understanding array shapes and dimensions.
- Copies and references.
- Vectorized numerical operations.
- Patient-data analysis and feature normalization.

### Week 6 — Pandas & Data Cleaning
- Loading structured data with Pandas.
- Inspecting DataFrames and their columns.
- Cleaning messy student records.
- Working with attendance and student datasets.
- Handling invalid records and data quality issues.
- Grouping and summarizing data.
- Exporting processed CSV files and cleaning reports.

### Week 7 — Data Visualization
- Creating visual representations of data.
- Exploring charts and graphical summaries.
- Presenting student-related information through a dashboard-style output.
- Saving visualizations as PNG and PDF files.

### Week 9 — Introduction to Machine Learning
A Decision Tree classification workflow using a machine-condition dataset.

Practical work includes:
- Loading and validating a dataset.
- Selecting input features and target variable.
- Splitting data into training and testing sets.
- Training a Decision Tree classifier.
- Evaluating accuracy and confusion matrix.
- Comparing tree depths and discussing overfitting.
- Saving and loading a trained model with Joblib.
- Making predictions for new machine records.
- Debugging data leakage and feature-name issues.

### Week 10 — Classification Algorithms Comparison
A comparative classification lab using the **UCI Spambase** dataset.

Algorithms represented:
- Decision Tree
- k-Nearest Neighbors (k-NN)
- Logistic Regression
- Gaussian Naive Bayes
- Majority-class baseline

The workflow includes:
- Dataset inspection and cleaning.
- Handling duplicate and ambiguous records.
- Stratified train/test splitting.
- Scikit-learn pipelines and feature scaling.
- Five-fold cross-validation.
- Comparing accuracy, precision, recall, and F1-score.
- Selecting a model based on validation performance.
- Evaluating the selected model on a reserved test set.
- Saving comparison reports and visualizations.

### Week 11 — Regression
The Week 11 folder contains a concrete-strength dataset and a regression notebook with generated reports and figures.

The available artifacts indicate practical work involving:
- Regression model analysis.
- Model coefficient reporting.
- Comparing model performance.
- Generating predictions.
- Regression diagnostic visualization.

### Week 12 — Unsupervised Learning: Customer Segmentation
A K-Means clustering project using the **Wholesale Customers** dataset.

The project explores customer spending patterns across six annual spending categories:
- Fresh
- Milk
- Grocery
- Frozen
- Detergents_Paper
- Delicassen

Practical workflow:
- Dataset inspection and validation.
- Handling missing values and duplicate records.
- Excluding identifiers and non-clustering categorical fields.
- Applying `log1p` transformation to reduce skewness.
- Standardizing numerical features with `StandardScaler`.
- Evaluating candidate cluster counts using inertia and silhouette scores.
- Training a K-Means model.
- Visualizing clusters using PCA.
- Comparing cluster means, medians, and customer shares.
- Checking stability across different random seeds.
- Saving the trained model with Joblib.
- Assigning a new customer to an existing segment.
- Writing business-oriented segment summaries and recommendations.

## Tools & Technologies

| Tool / Technology | Purpose |
|---|---|
| **Python** | Main programming language |
| **Visual Studio Code** | Development and code editing |
| **Jupyter Notebook** | Interactive labs and experiments |
| **uv / pip** | Python package and environment management |
| **NumPy** | Numerical computing and array operations |
| **Pandas** | Data loading, cleaning, transformation, and analysis |
| **Matplotlib** | Data visualization |
| **Scikit-learn** | Machine-learning models, preprocessing, validation, and evaluation |
| **Joblib** | Model persistence |
| **CSV / JSON** | Structured data storage and reports |
| **Git & GitHub** | Version control and repository hosting |

## Repository Structure

The coursework is organized into week-based folders.

```text
Programming_For_Ai_26_Tasks/
│
├── week01/       # Python basics
├── week02/       # Conditions, loops, and control flow
├── week03/       # Functions, exceptions, and testing
├── week04/       # OOP, files, and experiment tracking
├── week05/       # NumPy
├── week06/       # Pandas and data cleaning
├── week07/       # Data visualization
├── week09/       # Decision Tree machine-learning workflow
├── week10/       # Classification model comparison
├── week11/       # Regression analysis
├── week12/       # K-Means customer segmentation
│
└── README.md
```

Each week may contain Python scripts, Jupyter notebooks, datasets, reports, figures, or saved models depending on the practical task.

## Getting Started

### Requirements
- Python 3
- Visual Studio Code or Jupyter Notebook
- Required packages for the selected week

### Run an individual Python task

From the repository root:

```bash
python week01/01_hello.py
```

Replace the path with the script you want to execute.

### Work with Jupyter Notebooks

1. Open the repository in VS Code or Jupyter Notebook.
2. Select the appropriate Python environment/kernel.
3. Open the required `.ipynb` file.
4. Install any dependencies required by that week's lab.
5. Run cells in order.

### Machine-learning labs
For Weeks 9–12, use the README and dependency instructions inside the relevant week folder when available. Some labs require their supplied datasets and saved model/output directories.

## Learning Outcomes

This coursework demonstrates practical experience with:

- Writing structured Python programs.
- Applying conditions, loops, functions, and exception handling.
- Organizing programs with classes and modules.
- Reading and writing CSV and JSON data.
- Performing numerical operations with NumPy.
- Cleaning and analyzing datasets with Pandas.
- Communicating findings through visualizations.
- Building and evaluating supervised machine-learning models.
- Comparing classifiers using cross-validation and evaluation metrics.
- Understanding regression workflows.
- Applying K-Means clustering to customer data.
- Saving, loading, and reusing trained models.
- Interpreting model outputs and documenting analytical results.

## Academic Note

This is an academic learning repository containing weekly exercises, notebooks, datasets, generated reports, and machine-learning artifacts. The projects are intended for educational practice and experimentation, not as production-ready systems.

---

**Coursework:** Programming for Artificial Intelligence (PFAI)  
**Primary Language:** Python  
**Repository:** [Programming_For_Ai_26_Tasks](https://github.com/msalman65941-sys/Programming_For_Ai_26_Tasks)
