import numpy as np

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr1.shape)
print(arr2.shape)

z = np.zeros((5,5))
o = np.ones((5,5))

print(z.shape)
print(o.shape)

ar = np.arange(10)
print(ar)

ar = ar.reshape(2,5)
print(ar)

arr5 = np.array([1,2,3])
arr6 = np.array([4,5,6])
arr7 = arr5+arr6
print("arr7:",arr7)

arr8 = arr5 * arr6
print("arr8:",arr8)