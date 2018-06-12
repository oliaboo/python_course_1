import time

def my_decorator(some_function):
    def wrapper(arg1):
        begin = time.time()
        some_function(arg1)
        end = time.time()
        print(end-begin)
    return wrapper

@my_decorator
def just_some_function(name):
    print("Function process", name)

just_some_function('Sergey')
