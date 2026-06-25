import numpy as np

arr1 = np.arange(1,11).reshape(2,5)
print(arr1)
print("-------------------------------------")
print("-------------------------------------")

arr2 = np.arange(11,21).reshape(2,5)
print(arr2)
print("-------------------------------------")
print("-------------------------------------")

#Basic Operations
print(arr1 + arr2)
print(arr2 - arr1)
print(arr1/arr1)
print(arr1 * arr2)

print("-------------------------------------")
print("-------------------------------------")

print(arr1.sum()) #Sum of elements in array
print(arr1.sum(axis = 0)) #sum along axis of row
print(arr1.sum(axis=1)) #sum along axis of column