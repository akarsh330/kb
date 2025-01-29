def add():
    a,b=10,20
    print(a+b)
    def sub():
        c=(a-b)
        print(c)
    sub()
add()



def add():
    a,b=10,20
    print(a+b)
add()
print(add)



def alpha(beta):
    print("alpha")
    beta()
def beta():
    print("beta")
alpha(beta)