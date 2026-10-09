# AI Use Record — Assignment 2

## 1. AI Tools Used

I used ChatGPT as an AI assistant to understand the assignment requirements, prepare synthetic dataset records, write and understand Python code, debug errors, and prepare the project documentation.

I reviewed and ran the code to check its behavior. I am responsible for understanding and explaining the final submitted work.

## 2. Prompts Used and Summary of Responses

### Prompt 1: Understanding the Assignment

**Prompt:** Explain the requirements of Assignment 2 and help me complete the PatientDataset class using simple Python and Pandas.

**Summary:** ChatGPT helped me understand the required class methods, CSV loading, required-column validation, data auditing, duplicate detection, numeric validation, department standardization, median filling, imputation flags, and JSON export.

### Prompt 2: Preparing the Synthetic Patient Dataset

**Prompt:** The two CSV files exist, but they do not contain data. Help me prepare the CSV data according to the Assignment 2 PDF.

**Summary:** The assignment already provided nine example patient records. ChatGPT helped me prepare synthetic patient data to complete the 100-row dataset according to the assignment requirements. The dataset was intended to include missing values, exact duplicates, invalid numeric values, nonnumeric entries, and inconsistent department labels.

The dataset was used as input for developing and testing the patient data auditing and cleaning program. The original supplied dataset is kept unchanged in the project.

### Prompt 3: Debugging the CSV File Path

**Prompt:** My test_patient_dataset.py program gives a FileNotFoundError. Help me identify and fix the problem.

**Summary:** ChatGPT helped me check the current folder, confirm that the data folder existed, and display the actual filenames inside it. I discovered that my CSV file was named `patients_messy.csv`, while the code was looking for `patient_messy.csv`.

I corrected the filename in the file path and ran the tests again. The test program then displayed `All tests passed.`

### Prompt 4: Preparing Project Documentation

**Prompt:** Review the Assignment 2 requirements and help me prepare README.md and AI_USE.md.

**Summary:** ChatGPT helped me organize the documentation, explain the data cleaning decisions, describe the purpose of each project file, and prepare a checklist for verifying the expected results.

## 3. AI Suggestion Tested and Improved

During debugging, the program could not find the input CSV file. Instead of changing the data-cleaning logic, I checked the current directory, verified the data folder, and printed the filenames inside it.

This investigation identified a mismatch between the filename in the code and the actual CSV filename. I corrected the path and reran the tests successfully.

## 4. Testing and Verification

I performed the following checks during development:

1. Ran `test_patient_dataset.py` and confirmed that it displayed `All tests passed.`
2. Ran `demo.py` to check the demonstration program.
3. Checked the input CSV filename and folder location.
4. Reviewed the assignment's expected results, including the original row count, exact duplicates, invalid numeric values, medians, and imputation flags.
5. Checked the project structure and the locations of the input and output files.
6. Reviewed the requirement that the original DataFrame must remain unchanged when the audit and cleaning methods are called.
7. Used the synthetic patient dataset to test the program's data auditing and cleaning behavior.
8. Checked that the audit JSON and cleaned CSV files were generated and should match the assignment's expected results.

The final output values and personal test-case results must be checked against the actual generated files before submission.

## 5. What I Learned

Through this assignment, I learned how to:

* Create and use a Python class with methods.
* Load CSV files using Pandas.
* Validate required columns.
* Identify missing values, duplicates, invalid numeric values, and nonnumeric entries.
* Standardize inconsistent department labels.
* Use numeric conversion and median filling.
* Create Boolean imputation flags.
* Preserve the original DataFrame using a deep copy.
* Save an audit summary in JSON format.
* Write and run tests using ordinary Python assertions.
* Debug file path errors and verify program output.

## 6. Responsible Use of AI

AI was used as a learning, coding, dataset-preparation, and debugging assistant. I ran the program and checked its behavior rather than relying only on AI-generated suggestions.

I understand that I must explain the code, the cleaning sequence, the test results, and the purpose of the generated files during the assignment demonstration.

The submitted code and documentation should reflect the results I actually obtained and verified.
