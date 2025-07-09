import numpy as np

# Generate two 2x3 arrays with random integers
np.random.seed(42)
A = np.random.randint(1, 11, (2, 3))
B = np.random.randint(1, 11, (2, 3))

print("Array A:")
print(A)
print("\nArray B:")
print(B)

# Initialize result arrays
add = np.zeros((2, 3))
sub = np.zeros((2, 3))
mul = np.zeros((2, 3))
div = np.zeros((2, 3), dtype=float)

# Perform element-wise operations manually
for i in range(2):
    for j in range(3):
        add[i][j] = A[i][j] + B[i][j]
        sub[i][j] = A[i][j] - B[i][j]
        mul[i][j] = A[i][j] * B[i][j]
        div[i][j] = A[i][j] / B[i][j]

print("\nAddition:\n", add)
print("\nSubtraction:\n", sub)
print("\nMultiplication:\n", mul)
print("\nDivision:\n", div)
