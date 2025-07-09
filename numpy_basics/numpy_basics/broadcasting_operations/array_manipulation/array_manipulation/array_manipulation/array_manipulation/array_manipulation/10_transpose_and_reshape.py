import numpy as np

# Create a 3x2 matrix
matrix = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])

print("Original 3x2 Matrix:")
print(matrix)

# Transpose the matrix
transposed = matrix.T
print("\nTransposed Matrix (2x3):")
print(transposed)

# Reshape to 3x2
reshaped = transposed.reshape(3, 2)
print("\nReshaped to 3x2:")
print(reshaped)
