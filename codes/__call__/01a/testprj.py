class Example: 
    def __init__(self): 
        print("Instance Created") 
      
    # Defining __call__ method 
    def __call__(self): 
        print("Instance is called via special method") 
        
    # Defining __call__ method 
    def __call__(self, a): 
        print("__call__ a={}", a)         
  
# Instance created 
e = Example() 
  
# __call__ method will be called 
e() 
e(1234)