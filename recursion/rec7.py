#sum of nos using recursion

def addition(n):
    assert int(n) >=0 , "n must be zero and positive"
    if n ==0:
        return 0
        print("end")
    else :
        return int(n%10) +addition(n/10)

print(addition(46))    