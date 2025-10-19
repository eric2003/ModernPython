import sys

def my_function():
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")
        read_string(arg)        
        
def read_string(path):
    print(f"In read_string path= {path}")        

my_function()
    