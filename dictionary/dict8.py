dict1 = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10
}
pop = dict1.pop("one")
print(dict1)

item = dict1.popitem()
print(dict1)

del dict1['two']
print(dict1)

dict1.clear()
print(dict1)

del dict1
