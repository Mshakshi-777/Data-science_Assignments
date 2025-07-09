import numpy as np

# Create two 3x3 matrices
matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matrix2 = np.array([[10, 11, 12],
                    [13, 14, 15],
                    [16, 17, 18]])

# Stack horizontally (side by side)
horizontal_stack = np.hstack((matrix1, matrix2))

# Stack vertically (top to bottom)
vertical_stack = np.vstack((matrix1, matrix2))

# Display results
print("Matrix 1:\n", matrix1)
print("\nMatrix 2:\n", matrix2)

print("\nHorizontally Stacked (3x6):\n", horizontal_stack)
print("\nVertically Stacked (6x3):\n", vertical_stack)
