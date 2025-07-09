import numpy as np

# Create a 1D array with 8 elements
array = np.array([10, 20, 30, 40, 50, 60, 70, 80])

print("Original Array:")
print(array)

# Use fancy indexing to extract elements at positions 0, 2, 4, 6
indices = [0, 2, 4, 6]
selected = array[indices]

print("\nSelected elements at positions [0, 2, 4, 6]:")
print(selected)
