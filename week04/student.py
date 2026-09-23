class Student:
    def __init__(self, sap_id, name, marks):
        self.sap_id = sap_id
        self.name = name
        self.set_marks(marks)

    def set_marks(self, marks):
        """Validate and store the student's marks."""
        if not marks:
            raise ValueError("Marks cannot be empty.")

        for mark in marks:
            if mark < 0 or mark > 100:
                raise ValueError("Each mark must be between 0 and 100.")

        self._marks = marks

    def get_marks(self):
        """Return a copy of the student's marks."""
        return self._marks.copy()

    def calculate_average(self):
        """Return the student's average mark."""
        return sum(self._marks) / len(self._marks)

    def calculate_grade(self):
        """Return the letter grade based on the average."""
        average = self.calculate_average()

        if average >= 85:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "F"

    def format_profile(self):
        """Return the student's details as a formatted string."""
        return (
            f"SAP ID: {self.sap_id}\n"
            f"Name: {self.name}\n"
            f"Marks: {self._marks}\n"
            f"Average: {self.calculate_average():.2f}\n"
            f"Grade: {self.calculate_grade()}"
        )


def main():
    """Create students and display their profiles."""
    students = [
        Student("1001", "Ali", [78, 86, 91]),
        Student("1002", "Ahmed", [65, 72, 80]),
        Student("1003", "Hamza", [88, 92, 90]),
    ]
    print(type(students))

    # Print every student's profile.
    for student in students:
        print(student.format_profile())
        print()

    # Find the student with the highest average.
    # highest_student = max(
    #   students,
    #   key=lambda student: student.calculate_average()
    # )

    # print("Student with the highest average:")
    # print(highest_student.format_profile())

    # Confirm that get_marks() returns a copy.
    returned_marks = students[0].get_marks()
    returned_marks.append(100)

    # Test invalid marks.
    try:
        Student("1004", "Usman", [])
    except ValueError as error:
        print("\nEmpty-list test:", error)

    try:
        Student("1005", "Bilal", [72, 105])
    except ValueError as error:
        print("Out-of-range test:", error)


if __name__ == "__main__":
    main()
