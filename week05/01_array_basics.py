import numpy as np


marks = np.array([78, 85, 91, 66, 88])
matrix = np.arange(12).reshape(3, 4)
images = np.zeros((2, 4, 4))
identity = np.eye(4)
values = np.linspace(0, 1, 10)


arrays = {
    "marks": marks,
    "matrix": matrix,
    "images": images,
    "identity": identity,
    "values": values
}

for name, arr in arrays.items():
    print(f"\n{name}:")
    print("Shape:", arr.shape)
    print("Dimensions:", arr.ndim)
    print("Size:", arr.size)
    print("Data type:", arr.dtype)


print("\nTests:")
print("matrix.size =", matrix.size)
print("images.ndim =", images.ndim)

# Explanation
print("\nExplanation:")
print("marks.shape is (5,) because marks is a one-dimensional array with 5 elements,")
print("while matrix.shape is (3, 4) because it has 3 rows and 4 columns.")