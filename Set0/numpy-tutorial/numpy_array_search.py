import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)

arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8])

y = np.where(arr2%2 == 0)

print(y)

z = np.where(arr2%2 == 1)

print(z)

arr3 = np.array([6, 7, 8, 9])

xx = np.searchsorted(arr3, 7)

print(xx)

arr4 = np.array([6, 7, 8, 9])

xxx = np.searchsorted(arr4, 7, side='right')

print(xxx)

arr5 = np.array([1, 3, 5, 7])

xxxx = np.searchsorted(arr5, [2, 4, 6])

print(xxxx)