def div():
    try:
        a=int(input('enter number: '))
        b=int(input('enter numbner: '))
        c=a/b
        print(c)
    except ZeroDivisionError:
        print('cannot divided by zero')
    except ValueError:
        print('string inpuit will not be allowed')
div()
def add():
    e=int(input('enter number: '))
    f=int(input('enter numbner: '))
    r=e+f
    print(r)
add()






def div():
    try:
        a=int(input('enter number: '))
        print(b)
    except NameError:
        print('variable is not defined')
div()





try:
    v=[1,2,4]
    print(v[4])
except IndexError:
    print('out of the list')