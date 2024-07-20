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
dict2 = {
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
}

dict1.clear()
print(dict1)

dict3 = dict2.copy()
print(dict3)

dict4 = {}.fromkeys([1, 2, 3], 0)
print(dict4)

print(dict3.items())

