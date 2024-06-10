import numpy as np

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)


arr2 = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr2:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr1 = arr[filter_arr]

print(filter_arr)
print(newarr1)


arr3 = np.array([1, 2, 3, 4, 5, 6, 7])

# Create an empty list
filter_arr1 = []

# go through each element in arr
for element in arr3:
  # if the element is completely divisble by 2, set the value to True, otherwise False
  if element % 2 == 0:
    filter_arr1.append(True)
  else:
    filter_arr1.append(False)

newarr2 = arr3[filter_arr1]

print(filter_arr1)
print(newarr2)


arr4 = np.array([41, 42, 43, 44])

filter_arr4 = arr4 > 42

newarr4 = arr4[filter_arr4]

print(filter_arr4)
print(newarr4)


arr5 = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr5 = arr5 % 2 == 0

newarr5 = arr5[filter_arr5]

print(filter_arr5)
print(newarr5)