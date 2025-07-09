import numpy as np

# Create a 5x5 matrix with values from 1 to 25
matrix = np.arange(1, 26).reshape(5, 5)

print("Original 5x5 Matrix:")
print(matrix)

# Extract submatrix: rows 1–3 (index 1 to 4), columns 2–4 (index 2 to 5)
sub_matrix = matrix[1:4, 2:5]

print("\nExtracted Sub-matrix (rows 1–3, columns 2–4):")
print(sub_matrix)
