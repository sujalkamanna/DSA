#update/insert

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list1)
list1[0] = "0.1"
print(list1)

list1.append(10)
print(list1)
print(list1[0])

list1.insert(2,20)
print(list1)

popping = list1.pop(2)
print(popping)

# while list1:
#     list1.pop()
# print(list1)

list1.remove(10)
list1.__delitem__(7)
print(list1)

list3 = ['a','b','c','d']
print(list3)

del list3[0]
print(list3)

list3[0:1] = ['x','y','z']
print(list3)

