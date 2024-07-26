def function(fun1):
    def dec1():
        print("*"*10)
        fun1()
        print("*"*10)
    return dec1        

def hello():
    print("hello")

x = function(hello)


def decorator():
    pass