# list operation / function

#concatenation
a = [1,2,3]
b= [4,5,6]
c = a+b
print(c)

#repetition
a = [1,2,3]
b = a*4
print(b)

#membership
a = [1,2,3]
b = 2 in a
print(b)

#iteration
a = [1,2,3]
for i in a:
    print(i)

#slicing
a = [1,2,3,4,5,6]
print(a[1:4])

#length
a = [1,2,3,4,5,6]
print(len(a))

#append
a = [1,2,3]
a.append(10)
print(a)

#insert
a = [1,2,3]
a.insert(2,10)
print(a)

#pop
a = [1,2,3]
a.pop(2)
print(a)

#remove
a = [1,2,3]
a.remove(2)
print(a)

#del
a = [1,2,3]
del a[1]
print(a)

#clear
a = [1,2,3]
a.clear()
print(a)

#reverse
a = [1,2,3]
a.reverse()
print(a)

a = [1,2,3]
print(a[0:0:-1])

#extend
a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a)

#count
a = [1,2,3,4,5,6,7,8,9,10]
print(a.count(2))

#sort
a = [1,2,3,4,5,6,7,8,9,10]
a.sort()
print(a)

# max 
a = [1,2,3,4,5,99,88,55,22,1,4,78,651,]
print(max(a))

# min
a = [1,2,3,4,5,99,88,55,22,1,4,78,651,]
print(min(a))

#sum
a = [1,2,3,4,5,6,7,8,10,9]
print(sum(a))

#avg 
a = [1,2,3,4,5,6,7,8,10,9]
print(sum(a))
print(sum(a)/len(a))

