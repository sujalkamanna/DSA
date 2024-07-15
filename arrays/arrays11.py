import numpy as np 
import arrays as arr 

arr1=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9],
    ]
)
print(arr1)
for i in range(len(arr1)):
    for j in range(len(arr1[i])):
        if arr1[i][j] == 3:
            arr2 = np.delete(arr1 ,1 ,axis=0)

print("\n",arr2)