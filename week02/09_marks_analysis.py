marks = [78, 65, 92, 85, 48, 91]

passing_marks = []
failing_marks = []

for i in marks:
    if i >= 50:
        passing_marks.append(i)
    else:
        failing_marks.append(i)

total = 0

for i in marks:
    total += i

average = total / len(marks)

highest = max(marks)
lowest = min(marks)

print("Passing marks:", passing_marks)
print("Failing marks:", failing_marks)
print("Class average:", round(average, 2))
print("Highest mark:", highest)
print("Lowest mark:", lowest)