import numpy as np 
import array

arr = array.array('i',[1,2,3,4,5,6,7,8,9])
print(arr)

arr.insert(2,10)
print(arr)

arr.append(10)
print(arr)

arr.remove(10)
print(arr)
arr.remove(10)
print(arr)


print(arr[1])
print(arr[2])

arr[2] = 4
print(arr[2])

print(arr)

# arr2 = array.array("i",[10,20,30,40,50])
# arr2.insert(2,20)
# print(arr2)
# print(type(arr2))