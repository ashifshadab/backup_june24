import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)

arr1 = np.array([1, 2, 3, 4, 5, 6])

newarr1 = np.array_split(arr1, 4)

print(newarr1)

arr2 = np.array([1, 2, 3, 4, 5, 6])

newarr2 = np.array_split(arr2, 3)

print(newarr2[0])
print(newarr2[1])
print(newarr2[2])

arr3 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr3 = np.array_split(arr3, 3)

print(newarr3)

arr4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr4 = np.array_split(arr4, 3)

print(newarr4)

arr5 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr5 = np.array_split(arr5, 3, axis=1)

print(newarr5)

arr6 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr6 = np.hsplit(arr6, 3)

print(newarr6)