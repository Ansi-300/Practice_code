import numpy as np
import pygame
# Create a NumPy array
array1 = np.array([1, 2, 3, 4, 5])
print("Array 1:", array1)

# Create a 2D NumPy array (matrix)
matrix1 = np.array([[1, 2, 3],
                     [4, 5, 6]])
print("Matrix 1:")
print(matrix1)

# Perform basic operations
sum_array = array1 + 10  # Add 10 to each element
print("Array 1 + 10:")
print(sum_array)

# Matrix multiplication
matrix2 = np.array([[7, 8], [9, 10], [11, 12]])
result_matrix = np.dot(matrix1, matrix2)
print("Matrix Multiplication Result:\n", result_matrix)

# Generate a random array
random_array = np.random.rand(3, 3)  # 3x3 array with random values between 0 and 1
print("Random 3x3 Array:\n", random_array)