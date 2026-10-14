import numpy as np

data = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])

# 1. First row
first_row = data[0]
print("First row:", first_row)

# 2. Last column
last_column = data[:, -1]
print("Last column:", last_column)

# 3. Middle 2 x 2 block
middle_block = data[1:3, 1:3]
print("Middle 2 x 2 block:\n", middle_block)

# 4. Every second row
every_second_row = data[::2]
print("Every second row:\n", every_second_row)

# 5. Values greater than 75
greater_75 = data[data > 75]
print("Values greater than 75:", greater_75)

# 6. Values divisible by 20
divisible_by_20 = data[data % 20 == 0]
print("Values divisible by 20:", divisible_by_20)