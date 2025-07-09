import numpy as np

# Create two 1D arrays of different lengths
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7])

print("Array a:", a)
print("Array b:", b)

# Concatenate them along a new axis using object array
concatenated = np.array([a, b], dtype=object)

print("\nConcatenated along a new axis (object array):")
print(concatenated)
