#factorial 

n = 0

def fact(n):
    assert int(n) >= 0 , "no must be positive int and real no"
    if n in [0,1]:
        return 1
    else :
        return n*fact(n-1)
n = int(input("enter n :"))
print(fact(n))
