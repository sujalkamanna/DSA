import numpy as np

arr = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [7, 8, 9],
])


for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 3:
            print("the array is at", i, "row at", j, "column")\

# deleting
