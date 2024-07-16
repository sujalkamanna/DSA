list3 = []
n = int(input("how many elements de you want to add:"))
for _ in range(n):
    elements = input("add elements isn list:")
    list3.append(elements)
print(list3)

list2 = []
list4 = [1,2,3,4,5,6,7,8,9]

n = int(input("how many elements de you want to add:"))
for _ in range(n):
    elements = input("add elements isn list:")
    list2.append(elements)
list4.extend(list2)
print(list4)