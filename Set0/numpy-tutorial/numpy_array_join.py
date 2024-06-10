import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

newarr = np.concatenate((arr1, arr2))

print(newarr)

arr3 = np.array([[1, 2], [3, 4]])

arr4 = np.array([[5, 6], [7, 8]])

newarr1 = np.concatenate((arr3, arr4), axis=1)

print(newarr1)

arr4 = np.array([1, 2, 3])

arr5 = np.array([4, 5, 6])

newarr2 = np.stack((arr1, arr2), axis=1)

print(newarr2)

arr6 = np.array([1, 2, 3])

arr7 = np.array([4, 5, 6])

newarr3 = np.hstack((arr1, arr2))

print(newarr3)

arr8 = np.array([1, 2, 3])

arr9 = np.array([4, 5, 6])

newarr4 = np.vstack((arr1, arr2))

print(newarr4)

arr10 = np.array([1, 2, 3])

arr11 = np.array([4, 5, 6])

newarr5 = np.dstack((arr1, arr2))

print(newarr5)