list1 = [1,2,4,5,3,6,7,8,1]

key = 5
print(list1)

if key in list1:
    print("found",list1.index(key))
else :
    print("Not founf")    

#linear search
def find(list , n):
    for i in range(len(list)):
        if list[i] == key:
            return list.index(n)
    return -1    

index = find(list1,8)
print(index)

if index != -1:
    print("Element found at position: " + str(index + 1)) 
else:
    print("Element not found")