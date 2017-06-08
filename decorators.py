import functools

def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("before")
        func()
        print("after")
    return function_that_runs_func

@my_decorator
def my_func():
    print("running")

# my_func()

##
# avoid code duplicate
def decorator_with_arguments(numbers):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print("before")
            if numbers == 56:
                print("yes")
            else:
                func(*args, **kwargs)
            print("after")
        return function_that_runs_func
    return my_decorator

@decorator_with_arguments(55)
def my_func_2(x, y):
    print(x + y)

my_func_2(44, 99)
