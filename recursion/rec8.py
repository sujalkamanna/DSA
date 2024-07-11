#power of no using recursion
def power(base , expo):
    if expo ==0:
        return 1
    else:
        return base*power(base,expo-1)

print(power(2,4))


