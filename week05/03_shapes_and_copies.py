import numpy as np

# C1: Observe shared memory
original = np.array([10, 20, 30, 40, 50])

view = original[1:4]
view[0] = 999

print("C1 - Original after changing view:")
print(original)

# C2: Protect the source
independent = original[1:4].copy()
independent[0] = 555

print("\nC2 - Independent:")
print(independent)

print("Original remains:")
print(original)

# C3: Transform shapes
values = np.arange(1, 13)

reshaped = values.reshape(3, 4)
transposed = reshaped.T
flattened = reshaped.flatten()

print("\nC3 - Shapes:")
print("Original:", values.shape)
print("Reshaped:", reshaped.shape)
print("Transposed:", transposed.shape)
print("Flattened:", flattened.shape)

# Two 2 x 2 arrays
array1 = np.array([
    [1, 2],
    [3, 4]
])

array2 = np.array([
    [5, 6],
    [7, 8]
])

vertical = np.vstack((array1, array2))
horizontal = np.hstack((array1, array2))

print("Vertical:", vertical.shape)
print("Horizontal:", horizontal.shape)

# Split into three equal parts
numbers = np.arange(12)
parts = np.split(numbers, 3)

print("Split shapes:")
for part in parts:
    print(part.shape)