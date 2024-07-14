import numpy as np 

arr = np.array([
    [1,2,3],
    [2,3,4],
    [7,8,9],
])

print(arr)
def function(array,row,col):
    if row>= len(array) and col >= len(array):
        print("out of bound")
    else:
        print(array[row][col])
function(arr , 0 ,2)

print(arr[0][1])