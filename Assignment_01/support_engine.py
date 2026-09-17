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
    if attendance < 60 or missed_submission >= 4:
        return "High Priority"
    elif attendance < 75 or assignment_average < 60 or missed_submission >= 2:
        return "Moderate Priority"
    else:
        return "Routine Monitoring"


def format_message(category):
    if category == "High Priority":
        return "Immediate academic support is recommended."
    elif category == "Moderate Priority":
        return "Monitor progress and provide targeted guidance."
    else:
        return "Continue routine monitoring."


def main():
    attendance = read_float("Attendance Percentage (0 - 100):", 0, 100)
    assignment_average = read_float("Assignment Average (0 - 100):", 0, 100)
    missed_submission = read_int("Missed Submissions (0 or greater):", 0)

    category = classify_support(attendance, assignment_average, missed_submission)

    message = format_message(category)

    print(f"Category: {category}")
    print(f"Message: {message}")


if __name__ == "__main__":
    main()