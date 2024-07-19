
dict3 = {
    "one":"1",'two':'2',
    'three':'3','four':'4',
    'five':'5','six':'6',
    'seven':'7','eight':'8',
    'nine':'9','ten':'10'
}
for i , j in enumerate(dict3):
    print(i+1, j)
print("-------------------------")    
for i in dict3:
    print(i,dict3[i])    

for x, y in enumerate(dict3,start=1):
    print(x, y)
print("-------------------------")    