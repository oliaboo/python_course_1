from functools import wraps

def logged(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        print(func.__name__)
    return decorated_function


@logged
def some_function():
    pass
