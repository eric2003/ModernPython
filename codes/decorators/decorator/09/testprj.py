#https://www.runoob.com/w3cnote/python-func-decorators.html

def hello_decorator(num):
    """Simple decorator function that supports parameters"""

    def inner_func(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """Simple decorator wrapper function"""
            result = func(*args, **kwargs)
            result = result + num
            return result
        return wrapper
    return inner_func


@hello_decorator(100)
def add(a, b):
    """Simple function that returns sum of two numbers"""
    return a + b