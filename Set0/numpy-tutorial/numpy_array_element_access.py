import numpy as np

# Create a numpy array
arr = np.array([1, 10, 100, 1000])

# Get the first element from the array
print("First element of Array: ",arr[0])
# Get the Second element from the array
print("Second element of Array: ",arr[1])

arr1 = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# Access the element on the first row, second column:
print('2nd element on 1st row: ', arr1[0, 1])

#Access the element on the Second row, second column:
print('2nd element on 2st row: ', arr1[1, 1])

#Access the element on the Second row, fifth column:
print('5th element on 2nd row: ', arr1[1, 4])

arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# Access the third element of the second array of the first array
print("Third element of the second array of the first array: ",arr2[0, 1, 2])

# Example Explained for arr2[0, 1, 2]

# Step 1: arr2[0]
arr3 = arr2[0]
# Step 2: arr2[1]
arr4 =arr3[1]
# Step 3: arr2[2]
arr5=arr4[2]

print("Step 1: \n",arr3)
print("\n Step 2: ",arr4)
print("\n Step 3: ",arr5)

arr6 = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# Print the last element from the 2nd dim:
print('Last element from 2nd dim: ', arr6[1, -1])
