import numpy as np
from array import *

array_1 = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
array_2 = np.array([10, 20, 30, 40, 50])
# 1.Create an array and traverse
for i in array_2:
    print(i)

# 2.Access individual elements through indexes
print("<------>")
print(array_1[0])
print(array_1[2])
# 3 append any value to array using append() method
array_1.append(30)
print(array_1)
print("<------>")

# 4 Insert value into array using insert() method
array_1.insert(10, 20)
print(array_1)
print("<------>")
# 5 Extend python array using extend() method
array_1.extend(array_2)
print(array_1)
print("<------>")
# 6 add items from list into array using fromlist() method
list1 = [10, 20, 100, 200, 300]
array_1.fromlist(list1)
print(array_1)
print("<------>")
# 7 remove any element using remove() method
array_1.remove(300)
print(array_1)
print("<------>")
# 8 remove last array element using pop() method
array_1.pop()
print(array_1)
print("<------>")
# 9 fetch any element through its index using index() method
index = array_1.index(10)
print(index)
print("<------>")
# 10 reverse a python array using reverse() method
array_1.reverse()

# 11 get array buffer info through buffer_info() method
array_1.reverse()
buffer = array_1.buffer_info()
print(buffer)
print("<------>")
# 12 check for no of occurance of element using count method
print(array_1.count(10))
print("<------>")

# 13 remove all occurances of element in array using remove() method
array_1.remove(10)
print(array_1)

# 14 convert array to string using tostring() method
array_3 = array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
string_conversion = str(array_3)
print(string_conversion)
print(type(string_conversion))
print("<------>")

# 15 convert array to list using fromstrinf() method
array_4 = array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
list_conversion = list(array_4)
print(type(list_conversion))

# 16 slice elements from array
array_5 = array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(array_5[:5])
print("<------>")
# 17 append string to char array using fromstring() method
array_6 = array("u", "array data structure")
print(array_6)
