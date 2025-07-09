import numpy as np

# Create a 1D array with random values
array = np.array([5, 12, 8, 15, 3, 10, 18, 9])

print("Original Array:")
print(array)

# Replace all elements greater than 10 with 10
array[array > 10] = 10

print("\nModified Array (values > 10 replaced with 10):")
print(array)
