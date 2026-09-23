# while True:
# try:
# attendance = float(input("Enter the attendance (0 - 100): "))
# if 0 <= attendance <= 100:
# break
# else:
# print("Please enter a value between 0 and 100.")
# except ValueError:
# print("Invalid input. Please enter a numeric value.")


# while True:
# try:
# assignment_average = float(input("Enter the assignment average (0 - 100): "))
# if 0 <= assignment_average <= 100:
# break
# else:
# print("Please enter a value between 0 and 100.")
# except ValueError:
# print("Invalid input. Please enter a numeric value.")


# while True:
# try:
# missed_submission = int(input("Enter the number of missed submissions (0 or greater): "))
# if missed_submission >= 0:
# break
# else:
# print("Please enter a value of 0 or greater.")
# except ValueError:
# print("Invalid input. Please enter a numeric value.")


def read_float(prompt, minimum, maximum):
    """Reads a float value from user input within a specified range.
    Args:
        prompt (str): The prompt message to display to the user.
        minimum (float): The minimum acceptable value.
        maximum (float): The maximum acceptable value.
    Returns:
            float: The valid float value entered by the user."""
    while True:
        try:
            value = float(input(prompt))
            if minimum <= value <= maximum:
                return value
            else:
                print(f"Please enter a value between {minimum} and {maximum}.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def read_int(prompt, minimum):
    """Reads an integer value from user input that is greater than or equal to a specified minimum.
    Args:
        prompt (str): The prompt message to display to the user.
        minimum (int): The minimum acceptable value.
    Returns:
        int: The valid integer value entered by the user."""

    while True:
        try:
            value = int(input(prompt))
            if value >= minimum:
                return value
            else:
                print(f"Please enter a value of {minimum} or greater.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def classify_support(attendance, assignment_average, missed_submission):
    """Classifies the support category based on attendance, assignment average, and missed submissions.
    Args:
        attendance (float): The attendance percentage (0 - 100).
        assignment_average (float): The assignment average (0 - 100).
        missed_submission (int): The number of missed submissions (0 or greater).
    Returns:
        str: The support category."""

    if attendance < 60 or missed_submission >= 4:
        return "High Priority"
    elif attendance < 75 or assignment_average < 60 or missed_submission >= 2:
        return "Moderate Priority"
    else:
        return "Routine Monitoring"


def format_message(category):
    """Formats a message based on the support category.
    Args:
        category (str): The support category.
    Returns:
        str: The formatted message."""

    if category == "High Priority":
        return "Immediate academic support is recommended."
    elif category == "Moderate Priority":
        return "Monitor progress and provide targeted guidance."
    else:
        return "Continue routine monitoring."


def main():
    """Main function to read user input, classify support category, and display the message.
    Args:
        None
    Returns:
        None"""

    attendance = read_float("Attendance Percentage (0 - 100):", 0, 100)
    assignment_average = read_float("Assignment Average (0 - 100):", 0, 100)
    missed_submission = read_int("Missed Submissions (0 or greater):", 0)

    category = classify_support(attendance, assignment_average, missed_submission)

    message = format_message(category)

    print(f"Category: {category}")
    print(f"Message: {message}")


if __name__ == "__main__":
    main()
