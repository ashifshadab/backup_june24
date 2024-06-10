import numpy as np

#### Checking the Data Type
arr = np.array([1, 2, 3, 4])

# Get the data type of an array object
print("Data type of an array object: ",arr.dtype)

arr1 = np.array(['apple', 'banana', 'cherry'])
# Get the data type of an array containing strings
print("Data type of an array object: ",arr1.dtype)

#### Creating Arrays With a Defined Data Type

# Creating Arrays With a String Data Type
arr2 = np.array([1, 2, 3, 4], dtype='S')

# Print Array
print("Created Array with data type String \n",arr2)

# Get the data type of an array object
print("Data type of an array object: ",arr2.dtype)

# Creating Arrays With a Integer Data Type
arr3 = np.array([1, 2, 3, 4], dtype='i')

# Print Array
print("Created Array with data type integer \n",arr3)

# Get the data type of an array object
print("Data type of an array object: ",arr3.dtype)

# Create an array with data type 4 bytes integer:
arr4 = np.array([1, 2, 3, 4], dtype='i4')

# Print Array
print("Created Array with data type integer \n",arr4)

# Get the data type of an array object
print("Data type of an array object: ",arr4.dtype)

"""If a type is given in which elements can't be casted 
then NumPy will raise a ValueError.
ValueError: In Python ValueError is raised when the type of passed argument to 
a function is unexpected/incorrect.
"""
#arr5 = np.array(['a', '2', '3'], dtype='i')

### Converting Data Type on Existing Arrays
arr6 = np.array([1.1, 2.1, 3.1])

# Print Array
print("arr6: \n",arr6)

# Print Data type of Array
print("\n Data type of an array object: ",arr6.dtype)

# Change data type from float to integer by using 'i' as parameter value
newarr = arr6.astype('i')

# Print Array
print("newarr: \n",newarr)

# Print Data type of Array
print("\n Data type of an array object: ",newarr.dtype)

# Change data type from float to integer by using int as parameter value
newarr1 = arr6.astype('int')

# Print Array
print("newarr1: \n",newarr1)

# Print Data type of Array
print("\n Data type of an array object: ",newarr1.dtype)

#Change data type from integer to boolean:
newarr2 = arr6.astype('bool')

# Print Array
print("newarr2: \n",newarr2)

# Print Data type of Array
print("\n Data type of an array object: ",newarr2.dtype)