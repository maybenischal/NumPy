import numpy as np

array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [11,12,13,14],
                  [15,16,17,18]])

#slicing syntax = array[start:end:steps]

print(array[0:3]) #selects first 3 indexes
print('---------------------------------')

print(array[-1]) #selects last index 
print('---------------------------------')

print(array[1:]) #selects from index 1 to the end 
print('---------------------------------')

print(array[0:4:2]) #selects every 2nd element starting from index 0
print('---------------------------------')

print(array[::2]) #selects every 2nd element starting from first to last index
print('---------------------------------')

print(array[::-1]) #selects every element in reverse order
print('---------------------------------')

print(array[:,1]) #select all column in 2nd index
print('---------------------------------')

print(array[:,0:3]) #selects first 3 column
print('---------------------------------')

print(array[:, ::2]) #selects every column after one gap
print('---------------------------------')

print(array[:, ::-1]) #selects all column in reverse order
print('---------------------------------')
