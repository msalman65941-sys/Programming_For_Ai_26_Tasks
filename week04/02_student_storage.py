import csv
from pathlib import Path
from student import Student

def load_students(file_path):
    """Load students from a CSV file and return a list of Student objects."""
    students = []
    with Path(file_path).open("r", encoding="utf-8", newline="")as file:
        reader=csv.DictReader(file)
        for row in reader:
            marks=[float(row["mark1"]), float(row["mark2"]), float(row["mark3"])]
            students.append(Student(row["sap_id"], row["name"], marks))
    return students


def save_student_report(student, file_path):
    file_path=Path(file_path)

    file_path.parent.mkdir(parents=True, exist_ok=True)

    report=(f"SAP ID: {student.sap_id}\n"  
            f"Student Name: {student.name}\n"
            f"Average: {student.calculate_average():.2f}\n"
            f"Grade: {student.calculate_grade()}\n")
    with file_path.open("w", encoding="utf-8") as file: file.write(report)


def main():
    file_path = Path("week04/data/students.csv")

    students = load_students(file_path)

    print("Students loaded:")
    print()

    total_average = 0

    for student in students:
        print(student.format_profile())
        print()

        total_average += student.calculate_average()

        report_path = (Path("week04/reports")/ f"{student.sap_id}.txt")

        save_student_report(student, report_path)

    class_average = total_average / len(students)

    print(f"Class average: {class_average:.2f}")
    print()

    print("Saved reports:")

    for student in students:
        report_path = (Path("week04/reports")/ f"{student.sap_id}.txt")

        print(f"\n--- {report_path} ---")

        with report_path.open("r",encoding="utf-8") as file:print(file.read())


if __name__ == "__main__":
    main()