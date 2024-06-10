import numpy as np

# Python normal List
cars = ["Ford", "Volvo", "BMW"]

# Print list
print("Python list: " , cars)

# Check types of Object
print("\n Types of Object: ", type (cars))

# Convert Normal Python List to numpy Array
arr = np.array(cars)

# Print numpy Array
print("\n numpy array: ", arr)

# Check types of Object
print("\n Types of Object: ", type(arr))

# Create numpy 3-D Arrays
arr2 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])

# Print numpy Array
print("\n numpy 3d array: \n", arr2)

# Create numpy 2-D Arrays
arr3 = np.array([[1,2,3],[100,102,103]])

# Print numpy Array
print("\n numpy 2d array: \n", arr3)

# Create numpy 1-D Arrays
arr4 = np.array([1, 2, 3, 4, 5])

# Print numpy Array
print("\n numpy 1d array: \n", arr4)

# Create numpy 0-D Arrays
arr5 = np.array(42)

# Print numpy Array
print("\n numpy 0d array: \n", arr5)

# Print the number of axes (dimensions) of the array.
print("\n The number of axes in 0D array: ", arr5.ndim)
print("\n The number of axes in 1D array: : ", arr4.ndim)
print("\n The number of axes in 2D array: : ", arr3.ndim)
print("\n The number of axes in 3D array: : ", arr2.ndim)

# Create an array with 5 dimensions
arr6 = np.array([1, 2, 3, 4], ndmin=5)

# Print numpy Array
print("\n numpy array: \n", arr6)

