# operations and built in operations

myDict = {
    'one': "uno",
    'two': "dos",
    'three': "tres",
    'four': "cuatro",
    'five': "cinco",
    'six': "seis",
    'seven': "siete",
    'eight': "ocho",
    'nine': "nueve",
    'ten': "diez"
}

print("uno" in myDict.values())

print("uno" in myDict.keys())

print("uno" in myDict)

print("uno" not in myDict)

print(len(myDict))



print(myDict.keys())
for key in myDict:
    print(key, end=",")

dict1 = {
    1: True,
    0: False
}
print(all(dict1))


dict2 = {
    1:True,
    0 : False,
}

print(any(dict2))

vovels = {
    "i":3,
    "a":1,
    "e":2,
    "u":5,
    "o":4,
}


print(sorted(vovels))