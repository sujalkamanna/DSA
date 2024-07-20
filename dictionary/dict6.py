dict1 = {
    'one':1,
    'two':2,
    'three':3,
    'four':4,
    'five':5,
    'six':6,
    'seven':7,
    'eight':8,
    'nine':9,
    'ten':10,
    
}

#changing values
dict1['two'] = 200

print(dict1)

dict1.update({'two':2})
print(dict1)

del dict1['one']
print(dict1)

dict1.pop('two')
print(dict1)

