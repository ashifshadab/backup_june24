import numpy as np

# Iterate on the elements of the following 1-D array
arr = np.array([1, 2, 3])

for x in arr:
  print(x)

# In a 2-D array it will go through all the rows.
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr2:
  print(x)

# To return the actual values, the scalars, 
# we have to iterate the arrays in each dimension.
# Iterate on each scalar element of the 2-D array
arr4 = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr2:
  for y in x:
    print(y)  

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr3:
  print(x)

for x in arr3:
  for y in x:
    for z in y:
      print(z)


arr4 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr4):
  print(x)

arr5 = np.array([1, 2, 3])

for x in np.nditer(arr5, flags=['buffered'], op_dtypes=['S']):
  print(x)  

arr6 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr6[:, ::2]):
  print(x)  

arr7 = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr7):
  print(idx, x)  

arr8 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr8):
  print(idx, x)  