import numpy as np

# Create a 1D array of 10 random integers
np.random.seed(42)
array = np.random.randint(1, 11, 10)

print("Original Array:")
print(array)

# Compute cumulative sum manually
cumulative_sum = []
running_total = 0

for val in array:
    running_total += val
    cumulative_sum.append(running_total)

print("\nCumulative Sum:")
print(cumulative_sum)
