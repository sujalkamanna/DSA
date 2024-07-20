# linear search

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


def funct(dict, value):
    for key in dict:
        if dict[key] == value:
            print(f"found {key} with value {value}")
    return "not found"


funct(dict1, 10)
