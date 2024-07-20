dict1 = {
    'one':1,
    'two':2,
    'three':3,
    'four':4,
    'five':5,
    'six':6,
    'seven':7,
}

dict1['eins'] = dict1.pop('one')
print(dict1)

dict1['zwei'] = dict1.pop('two')
print(dict1)


dict1.update({"drie":dict1.pop("three")})
print(dict1)