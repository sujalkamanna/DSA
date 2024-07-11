def fibionacci(n):
    assert int(n) >=0 , "only int and positive nos"
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fibionacci(n-1) + fibionacci(n-2) 

print(fibionacci(5))
print(fibionacci(4))
print(fibionacci(3))
print(fibionacci(2))
print(fibionacci(-5))