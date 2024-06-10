import numpy as np

### Copy
# Create Array
arr = np.array([1, 2, 3, 4, 5])

# Print Original Array
print("Origina Array before copy: \n",arr)

# Copy Data from Original Array and create new one
x = arr.copy()

# Print new array which comes from copy activity
print("Print new array which comes from copy activity: \n",x)

# Modify Original Array
arr[0] = 9

# Print Original Array
print("Origina Array After copy and modif: \n",arr)

print("Print new array which comes from copy activity after modify: \n",x)


### View
# Create Array
arr1 = np.array([10, 20, 30, 40, 50])

# Print Original Array
print("\n Origina Array before View: \n",arr1)

# Copy Data from Original Array
x1 = arr1.view()

# Print new array which comes from copy activity
print("Print new array which comes from copy activity: \n",x1)

# Modify Original Array
arr1[0] = 45

# Print Original Array
print("Origina Array After view and modif: \n",arr1)

print("Print array which comes from view activity after modify: \n",x1)


### Check if Array Owns its Data
"""Every NumPy array has the attribute base 
that returns None if the array owns the data.
Otherwise, the base  attribute refers to the original object.
"""
# Create Array
arr3 = np.array([1, 2, 3, 4, 5])

#Copy
x3 = arr3.copy()

#View
y = arr3.view()

#Check if the array owns the data
print("\n Array owns the data (copy): ",x3.base)

#Check if the array owns the data
print("Array owns the data (view): ",y.base)