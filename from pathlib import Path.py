from pathlib import Path 
import pandas as pd 
 
DATA_PATH = Path("week06/data/processed/students_clean.csv") 
FIGURE_DIR = Path("week07/figures") 
FIGURE_DIR.mkdir(parents=True, exist_ok=True) 
 
students = pd.read_csv(DATA_PATH) 
required = {"program", "attendance", "final", "weighted_score", "grade"} 
 
print(students.shape) 
print(students[sorted(required)].head()) 
print(students[sorted(required)].isna().sum())