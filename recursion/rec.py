#recursion = function calling itself

def opendolls(doll):
    if doll ==1:
        print("all dolls are open")
    else:
        opendolls(doll-1)
opendolls(10)