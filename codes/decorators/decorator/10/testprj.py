#https://www.runoob.com/w3cnote/python-func-decorators.html

from functools import wraps

def is_authenticated(user):
    return user == "authenticated_user"
    
def authentication_decorator(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        user = kwargs.get("user")
        if is_authenticated(user):
            return f(*args, **kwargs)
        else:
            raise PermissionError("User is not authenticated")
        return decorated
        
@authentication_decorator
def restricted_function(user):
    print("Access granted to the restricted function")

#restricted_function(user = "authenticated_user")
restricted_function("authenticated_user")

restricted_function(user="haha")
