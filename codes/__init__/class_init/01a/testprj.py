# A Sample class with init method
class Person:
 
    # init method or constructor
    def __init__(self, name):
        self.name = name
        self.age = 1
        
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name, ' my age is',  self.age)
 
 
p = Person('Nikhil')
p.say_hi()

p1 = Person('tom',10)
p1.say_hi()