from student_utils import calculate_average, calculate_grade


def parse_marks(text):
    """Convert comma-separated text into a validated list of marks.
    Raises ValueError if any mark is invalid.
    Arguments:
        text: str, comma-separated marks
    Returns:
        list of float, validated marks"""
    if not text.strip():
        raise ValueError("Enter at least one mark.")

    parts = text.split(",")
    marks = []

    for part in parts:
        if not part.strip():
            raise ValueError("A mark is missing between commas.")

        mark = float(part.strip())

        if mark < 0 or mark > 100:
            raise ValueError("Every mark must be between 0 and 100.")

        marks.append(mark)

    return marks


def generate_summary(name, marks):
    """Return a multi-line student report.
    Arguments:
        name: str, student name
        marks: list of float, validated marks
    Returns:
        str, the student report"""
    average = calculate_average(marks)
    grade = calculate_grade(average)

    report = (
        f"Student Name: {name}\nMarks: {marks}\nAverage: {average:.2f}\nGrade: {grade}"
    )

    return report


def save_report(filename, report):
    """Write the report to a UTF-8 text file.
    Arguments:
        filename: str, the name of the file to save
        report: str, the report content
    Returns:
        None"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(report)
