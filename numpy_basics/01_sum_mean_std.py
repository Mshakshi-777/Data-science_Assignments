import numpy as np

# Create a 3x3 array with random integers between 0 and 10
np.random.seed(42)
array = np.random.randint(0, 11, (3, 3))

print("Array:")
print(array)

# Compute sum manually
total_sum = 0
for row in array:
    for val in row:
        total_sum += val

# Compute mean
num_elements = array.shape[0] * array.shape[1]
mean = total_sum / num_elements

# Compute standard deviation
sum_squared_diff = 0
for row in array:
    for val in row:
        sum_squared_diff += (val - mean) ** 2

std_dev = (sum_squared_diff / num_elements) ** 0.5

print(f"\nSum: {total_sum}")
print(f"Mean: {mean}")
print(f"Standard Deviation: {std_dev}")
