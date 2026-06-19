import numpy as np

#sort in ascending order
arr1 = np.array([[1,9],[2,8]])
print(np.sort(arr1)) 
print("________________________________")

print(np.sort(arr1, axis=None)) #sorts in flattened array
print("________________________________")


arr2 = np.array([[5, 1],
                [2, 9]])

print(np.sort(arr2, axis=0))
print("________________________________")
print(np.sort(arr2, axis=1))
print("________________________________")
print("________________________________")

dtype = [('name', "U10"), ('height', float), ('age', int)]
values = [('Arthur', 1.8, 41), ('Lancelot', 1.9, 38),
          ('Galahad', 1.7, 38)]
a = np.array(values, dtype=dtype)   
print(np.sort(a, order = "height"))
