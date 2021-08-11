#不修改源码的前提下，增添新功能
class AAA():
    def __init__(self,func):
        self.__func = func
    def __call__(self,*args,**kwargs):
        self.addFunc()
        self.__func()
    def addFunc(self):
        print("新功能")
@AAA
#test1=AAA(test1)
#原有代码
def test1():
    print("原有功能")
test1()