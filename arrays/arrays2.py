from array import *
import numpy as np

array1 = array('i', [1, 2, 3, 4, 5])
print(type(array1))


array1.append(10)
print(array1)

array1.insert(2, 20)
print(array1)

# insert(before index , vvalue to insert)
array1.insert(3, 30)
print(array1)
