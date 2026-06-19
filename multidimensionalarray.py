import numpy as np 

array1 = np.array('A')
print(array1.ndim)

array2 = np.array([1, 2, 3, 4, 5])
print(array2.ndim)  

array3 = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(array3.ndim)

array4 = np.array([
                  [[1,2],[5,6]],
                  [[3,4],[7,8]],
                  [[13,14],[17,65]]
                  ])
print(array4.ndim) # calculates the dimension of the array
print(array4.shape) # calculates the shappe - depth, row and column of the array
 
print(array4[1,1,0]) # access the element at depth 1, row 1 and column 0 also known as mUltidimensional array indexing