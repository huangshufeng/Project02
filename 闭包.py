import time
def writeLog(func):
    try:
        file=open('log.txt','a',encoding='utf-8')
        file.write(func.__name__)
        file.write('\t')
        file.write(time.asctime())
        file.write('\n')
    except Exception as e:
        print(e.args)
    finally:
        file.close()
def funcOut(func):
    def funcIn():
        writeLog(func)
        func()
    return funcIn()
def func1():
    print("我是功能1")
def func2():
    print("我是功能2")
func1 = funcOut(func1)
func2 = funcOut(func2)
func1
func2