# accessing list
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
for i in list1:
    print(i)
print(list1)


# list slicing
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
print(list2[0:5])
print(list2[::-1])

# accessing elements

shopping_list = ["milk", "cheese", "butter"]
print(shopping_list[0])

print(shopping_list)


enter_value = int(input("enter index:"))
if enter_value> len(shopping_list):
    raise IndentationError
    print("not available")
else:
    print("available:",shopping_list[enter_value])


list3 = []

for _ in list3:
    add = list3.append(input("Enter elements to add in list"))
    print(list3)