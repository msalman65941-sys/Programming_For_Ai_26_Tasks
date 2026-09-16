def calculate_grade(marks):
    if marks >= 85:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

def calculate_average(marks):
    return sum(marks) / len(marks)

def format_summary(name, average, grade):
    return f"{name} average is {average:.2f} with grade {grade}"