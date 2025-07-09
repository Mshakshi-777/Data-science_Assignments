import numpy as np

# Initialize a 4x4 zero matrix
identity_matrix = np.zeros((4, 4), dtype=int)

# Set diagonal values to 1
for i in range(4):
    identity_matrix[i][i] = 1

# Display the identity matrix
print("4x4 Identity Matrix:")
print(identity_matrix)
