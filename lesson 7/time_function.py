import time

def my_decorator(some_function):
    def wrapper():
        begin = time.time()
        some_function()
        end = time.time()
        print(end-begin)
    return wrapper

def just_some_function():
    print("Function process")

just_some_function = my_decorator(just_some_function)
just_some_function()
