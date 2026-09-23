import csv
import json


# F1
# Error: self is missing from the constructor.
# Cause: Instance methods need self as their first parameter.
# Fix: Add self to __init__.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


# F2
# Error: The file is opened in read mode.
# Cause: "r" does not allow writing rows to the CSV file.
# Fix: Use "w" mode.

with open("students.csv","w",newline="") as file:

    writer = csv.writer(file)
    writer.writerow(["Ali", 85])


# F3
# Error: A custom Python object cannot be directly serialized to JSON.
# Cause: json.dump() supports JSON-compatible data types.
# Fix: Convert the object into a dictionary first.

model = {"name": "Decision Tree","accuracy": 0.91}

with open("model.json","w",encoding="utf-8") as file:

    json.dump(model, file, indent=4)


print("Debugging tasks completed.")