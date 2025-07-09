import numpy as np

# Create a 1D array
a = np.array([5, 10, 15, 20, 25])

# Divide each element by 5 using broadcasting
result = a / 5

# Display results
print("Original Array:")
print(a)

print("\nArray after dividing by 5:")
print(result)
