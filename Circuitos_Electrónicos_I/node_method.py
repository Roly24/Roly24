import numpy as np

# Let's think if we have the following system of equations
# Video link: https://www.youtube.com/watch?v=h4YU2F85z38
"""
8V1 - 5V2 = -60 (1)
2V1 - 3V2 = -36 (2)

To solve: Ax = b
A = [[8, -5], 
     [2, -3]]

b = [[-60], 
     [-36]]
"""

# Defining the matrix A
A = np.array([[8, -5], [2, -3]])

# Defining the matrix b
b = np.array([[-60], [-36]])

# Using the linalg class from numpy
x = np.linalg.solve(A, b)

print(x)