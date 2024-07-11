def recmethod(n):
    if n<2:
        print("n is less than one")
    else :
        recmethod(n-1)
        print(n)

recmethod(10)            