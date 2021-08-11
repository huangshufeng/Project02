#不带参数
def funcOut(x):
    def funcIn():
        print("新增功能")
        x()
    return funcIn
@funcOut
def function1():
    print("我是功能一")
@funcOut
def function2():
    print("我是功能二")
#function1=funcOut(function1)
#function2=funcOut(function2)
function1()
function2()



