dict1 = {
    "key": "value",
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
print(dict1['one'])
# accessing dict value using index


def access(dict, index):
    list1 = list(dict1.keys())
    key = list1[index]
    value = dict[key]
    if index > len(list1):
        print('index out of range!')
    else:
        print(f"found {key} with key value as {value} ")


access(dict1, 5)

print(dict1.keys())
