import numpy as np

array1 = np.zeros(2)
print(array1)
print("________________________________")

array2 = np.ones(2)
print(array2)
print("________________________________")

array3 = np.arange(4)
print(array3)

array4 = np.arange(2,10,3) # start,end and space
print(array4)
print("________________________________")

array5 = np.linspace(0,10, num=3) #start end and number of elements spaced linearly
print(array5)

#Reshape an array
a = np.arange(6)
print(a)

b = a.reshape(3,2) #reshapes array into 3 row and 2 columns
print(b)
print("------------")

#Converting 1D array to 2D Array
c = np.arange(1,6)
print(c)
print(c.shape)
print("------------")
print("------------")

c2 = a[np.newaxis,:] #converts to row vector
print(c2)
print(c2.shape) 

print("------------")
print("------------")

c3 = a[:,np.newaxis] #converts into column vector
print(c3)
print(c3.shape) 
