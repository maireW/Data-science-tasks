import numpy as np
#task1 Create a 1D array of numbers from 0 to 9
array = np.array([0,1,2,3,4,5,6,7,8,9])
print (array[0:10])

#task2 Create a 3×3 NumPy array of all Boolean value Trues
array2 = np.array([1,1,1,1,1,1,1,1,1])
newarray2 = array2.reshape(3,3)
print(newarray2)

#task3 Extract all odd numbers from array of 1-10
array3 = np.arange(1,11,2)
print(array3)

#task4 change all odd numbers to -1
array4 = np.arange(1, 91, 1) 
array4[array4%2==1] *= -1        
#above select & multiply only odd numbers, doesn't effect even ones
print(array4)


#task 5 convert 1d array to 2d with 2 rows)
array_5 = np.array([1,2,3,4,5,6,7,8,9,10])
print(array_5)
newArray_5 = array.reshape(2,5)
print(newArray_5)

#task6 Create two arrays a and b, stack these two arrays vertically use the np.dot and np.sum to calculate totals
aArray = np.arange(4).reshape (2,2)
print(aArray)
bArray = np.array([4,5,6,7]).reshape (2,2)
print(bArray)
cArray = np.dot(aArray, bArray)
print (cArray)
#sum all
sum = np.sum(cArray)
print(sum)
#sum row*
d = np.sum(cArray,axis = 1)
print(d)


