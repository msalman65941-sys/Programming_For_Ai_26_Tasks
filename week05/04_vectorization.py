import numpy as np

# D1: Vectorized transformations

temperatures = np.array([20, 25, 30, 35, 40])

fahrenheit = temperatures * 9 / 5 + 32

print("Celsius:", temperatures)
print("Fahrenheit:", fahrenheit)


marks = np.array([55, 67, 72, 88, 91])

adjusted = np.minimum(marks + 5, 100)

print("\nOriginal marks:", marks)
print("Adjusted marks:", adjusted)


normalized = (marks - marks.min()) / (marks.max() - marks.min())

print("Normalized marks:", normalized)


# D2: Broadcasting a bonus

scores = np.array([
    [70, 75, 80],
    [60, 65, 70],
    [85, 90, 95]
])

bonus = np.array([2, 3, 5])

adjusted_scores = scores + bonus

print("\nOriginal scores:")
print(scores)

print("Bonus:", bonus)

print("Adjusted scores:")
print(adjusted_scores)