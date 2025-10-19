def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(prefix, "Executed Before", original_function.__name__)
            result = original_function(*args, **kwargs)
            print(prefix, "Executed After", original_function.__name__,"\n")
            return result
        return wrapper_function
    return decorator_function

@prefix_decorator('TESTING')
def display_info(name, age):
    print("display_info ran with arguments ({}, {})".format(name, age))
    
@prefix_decorator('DEBUG')
def add_abc(a, b, c):
    print("add_abc ran with arguments ({}+{}+{}={})".format(a, b, c,a+b+c))

    
display_info('john',25)
display_info('Travis',30)

add_abc(1,2,3)
add_abc(a=1,b=2,c=3)
add_abc(a=3,b=2,c=1)
