import student_utils

name = "Salman"
marks = [78, 86, 91]
average = student_utils.calculate_average(marks)
grade = student_utils.calculate_grade(average)
summary = student_utils.format_summary(name, average, grade)
print(summary)