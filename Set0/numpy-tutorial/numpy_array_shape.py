import numpy as np

##### NumPy Array ShapeNumPy Array Shape
"""Shape of an Array-- The shape of an array is the number of elements in each dimension
"""

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# Print the shape of a 2-D array
print(arr.shape)
"""Explenation:- The example above returns (2, 4), 
                which means that the array has 2 dimensions, 
                where the first dimension has 2 elements 
                and the second has 4."""

# Create an array with 5 dimensions using ndmin 
# using a vector with values 1,2,3,4 
# and verify that last dimension has value 4:
arr1 = np.array([1, 2, 3, 4], ndmin=5)

# Print Array
print(arr1)

# Print the shape of a 5-D array
print('shape of array :', arr1.shape)

# NumPy Array Reshaping
""" Reshaping means changing the shape of an array.
    The shape of an array is the number of elements in each dimension.
    By reshaping we can add or remove dimensions 
    or change number of elements in each dimension.
"""

arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Convert the following 1-D array with 12 elements into a 2-D array.
# The outermost dimension will have 4 arrays, each with 3 elements:
newarr = arr2.reshape(4, 3)

print(newarr)

# Convert the following 1-D array with 12 elements into a 3-D array.
# The outermost dimension will have 2 arrays 
# that contains 3 arrays, each with 2 elements:
newarr1 = arr2.reshape(2, 3, 2)

print(newarr1)

### Flattening the arrays
# Flattening array means converting a multidimensional array into a 1D array.

# We can use reshape(-1) to do this.
arr3 = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr3.reshape(-1)

print(newarr)
