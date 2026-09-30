#Explain why addition fails and choose a correction that matches a stated intention.
import Numpy as np #this was missing 
a = np.ones((3, 4))
b = np.ones((3, 2))
result = a + b


#Replace the invalid Boolean expression with element-wise conditions.
values = np.array([10, 20, 30, 40])
selected = values[values > 15 and values < 35]

#Changes made below
values = np.array([10, 20, 30, 40])
selected = values[(values > 15) & (values < 35)]
print(selected)


#Correct the calculation so each row receives one student average.
scores = np.array([
    [70, 80, 90],
    [60, 75, 85]
])
student_averages = np.mean(scores, axis=0)

#Changes Below

scores = np.array([
    [70, 80, 90],
    [60, 75, 85]
])

student_averages = np.mean(scores, axis=1)

print(student_averages)