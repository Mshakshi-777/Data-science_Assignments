import numpy as np

# Create a 1D array with 15 elements
array = np.arange(1, 16)

print("Original Array:")
print(array)

# Extract elements from index 2 to 10 with a step of 2
sliced = array[2:10:2]

print("\nExtracted Elements (index 2 to 10 with step 2):")
print(sliced)
