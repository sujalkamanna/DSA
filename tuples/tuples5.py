# tuples vs list


tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(tup)

list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list1[1] = 10

print(list1)


del list1[0]
print(list1)

# tup[0] = 1
print(tup)

# del tup[0]

tup = (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
print(tup)

for i in tup: print(i)


list2 = [(1,2) , (3,4)]
print(type(list2))
print(list2)
list2[0] = 1,10
print(list2)

tup_list = (1,2,3,4,5,)
if 10 in tup_list: print("found ") 
else: print("not found ")