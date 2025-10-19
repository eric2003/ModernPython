#https://www.runoob.com/w3cnote/python-func-decorators.html
def hi():
    return "hi yasoob!"
 
def doSomethingBeforeHi(func):
    print("I am doing some boring work before executing hi()")
    print(func())
 
doSomethingBeforeHi(hi)
#outputs:I am doing some boring work before executing hi()
#        hi yasoob!