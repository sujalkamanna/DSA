#decimal to binary

def bin(n):
    if n ==0:
        return 0
    else:
        n%2 + 10*bin(int(n/2))
print(bin(6))    