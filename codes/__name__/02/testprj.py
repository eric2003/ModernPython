class A1:
    def __init__(self):
        print(type(self).__name__)

class _A1:
    def __init__(self):
        print(type(self).__name__)
        
class A2(object):
    def __init__(self):
        print(type(self).__name__)
        
class B:
    def __init__(self):
        print(self.__class__.__name__)

class C(A1):
    def __init__(self):
        print(type(self).__name__)
        
class D(A2, C):
    def __init__(self):
        print(type(self).__name__)
        
class E(C, A2):
    def __init__(self):
        print(type(self).__name__)
        
class F(A1, _A1):
    def __init__(self):
        print(type(self).__name__)
        
        
A1()
A2()
B()

C()
D()
E()
F()