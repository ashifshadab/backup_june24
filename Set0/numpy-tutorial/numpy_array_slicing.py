import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Slice elements from index 1 to index 5
print("Slice elements from index 1 to index 5: \n",arr[1:5])

# Slice elements from index 4 to the end of the array:
print("Slice elements from index 4 to the end of the array: \n",arr[4:])

# Slice elements from the beginning to index 4 (not included)
print("Slice elements from the beginning to index 4: \n",arr[:4])

# Slice from the index 3 from the end to index 1 from the end
print("Slice from the index 3 from the end to index 1 from the end: \n",arr[-3:-1])

# Slicing 2-D Arrays
arr1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# From the second element, slice elements from index 1 to index 4 (not included):
print("From the second element, slice elements from index 1 to index 4: \n",arr1[1, 1:4])

# From both elements, return index 2:
print("From both elements, return index 2: \n",arr1[0:2, 2])

# From both elements, slice index 1 to index 4 (not included), this will return 2DArray
print("From both elements, slice index 1 to index 4: \n",arr1[0:2, 1:4]) 

# STEP - Use the step value to determine the step of the slicing
# [start:end:step]

arr2 = np.array([1, 2, 3, 4, 5, 6, 7])
# Return every other element from index 1 to index 5
print("Return every other element from index 1 to index 5: \n",arr2[1:5:2])

# Return every other element from the entire array
print("Return every other element from the entire array: \n",arr2[::2])
