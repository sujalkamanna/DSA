#what will be the output
#1
init_tuple = ()

print(init_tuple.__len__())

#2
init_tuple_a = 'a','b'
init_tuple_b = ('a','b')
print(init_tuple_a == init_tuple_b)

#3
init_tuple_a = '1','2'
init_tuple_b = ('3','4')
print(init_tuple_a +init_tuple_b)

#4
init_tuple_a = '1','2'
init_tuple_b = ('3','4')
[print(sum(x)) for x in [init_tuple_a + init_tuple_b]]

#5
# init_tup = [(0,1),(1,2),(2,3)]
# result = sum(n for_,n in init_tup)
# print(result)