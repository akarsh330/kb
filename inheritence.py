class alpha:
    def fun1(self):
        print('inside alpha  fun1()')
class beta(alpha):
    def fun2(self):
        print('inside beta fun2()')
class gamma(beta):
    pass
g=gamma()
g.fun1()
g.fun2()







class alpha:
    def fun1(self):
        print('alpha class  fun1()')
class beta(alpha):
    def fun2(self):
        print('beta class fun2()')
class gama(alpha,beta):
    pass
g=gamma()
g.fun1()
g.fun2()