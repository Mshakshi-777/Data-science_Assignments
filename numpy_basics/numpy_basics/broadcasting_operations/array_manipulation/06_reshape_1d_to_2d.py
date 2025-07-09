import numpy as np

# Create a 1D array of 12 elements
array_1d = np.arange(1, 13)

# Reshape it into a 3x4 matrix
array_2d = array_1d.reshape(3, 4)

# Display results
print("Original 1D Array:")
print(array_1d)

print("\nReshaped 3x4 Matrix:")
print(array_2d)
