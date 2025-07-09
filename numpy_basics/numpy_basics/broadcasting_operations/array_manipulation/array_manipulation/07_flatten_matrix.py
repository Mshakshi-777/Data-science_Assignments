import numpy as np

# Create a 3x3 matrix
matrix_2d = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])

# Flatten the matrix using reshape
flattened = matrix_2d.reshape(-1)

# Display results
print("Original 3x3 Matrix:")
print(matrix_2d)

print("\nFlattened 1D Array:")
print(flattened)
