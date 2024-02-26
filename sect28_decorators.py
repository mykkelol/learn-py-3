""" 
Higher order functions
    - multiple types of high order functions
    - func argument: when passing one function to another function as an argument
        - example: def sum(n, func) ... def square(n)... sum(1, square)
    - nested functions: when we use a private function within a function
    - returning function: when we use nested function and returning the inner function
    - closure: when we use nested function and returning the inner function, but the inner function accesses the outer function's scope

Decorators
    - decorators are just high order functions that wraps other functions to enhance their behavior i.e. we decorate the outer functions :)
    - in py, decorators are prefixed with syntatic suguar '@' (see example A)
    - problems with when decorators when used with high order functions (see example B)
        - func.__name__ or func.__doc__ refers to the inner high order function and never the original function
        - this is especially problematic when we want to create logger decorator functuons
        - to resolve, py has a module, wraps from functools, and is decorator for our wrapper in within the decorator lol 
    - given decorators are always paired with *args and **kwargs, we may need to validate and enforce specific types or values (see example C)

"""
from functools import wraps

# example A, create a high order function to make greeting polite and two greeting functions, create two greeter functions, one with decorator and one without
def be_polite(fn):
    def wrapper(*name, **kwargs):
        print('What a pleasure to meet you!')
        fn(*name, **kwargs)
        print('Have a great day!')
    return wrapper

def greet(name):
    print(f'Hi {name}')

greet = be_polite(greet) # without decorator, have to 
greet('Nickel')

@be_polite #with decorator
def rage(name):
    print(f'{name} you stinkybug')

rage('Nickel')

#example B: create functions, add and multiply, that uses a decorator that logs and documents math tools
def log_function_executions(fn):
    import time
    @wraps(fn) # with wraps, __name__, __doc__, and help will properly preserve the func and reference it
    def wrapper(*args, **kwargs):
        print(f'Executing {fn.__name__}')
        print(f'The function purpose: {fn.__doc__}')
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        print(f'Time elapsed: {end_time - start_time}')
        return result
    return wrapper

@log_function_executions
def add(n1, n2):
    """Accepts two arguments, n1 and n2, and sums the two arguments"""
    return n1 + n2

@log_function_executions
def multiply(n1, n2):
    """Accepts two arguments, n1 and n2, and multiplies the two arguments"""
    return n1 * n2

print(add(1,2))

#example C: create a decorator that can validate for specific types and typecast if it's not to its corresponding types
def enforce_types(*types):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            newargs = []
            for (a, t) in zip(args, types):
                newargs.append(t(a))
            return fn(*newargs, **kwargs)
            # raise ValueError(f'First input must be a str and equal to: {val}')
        return wrapper
    return inner

@enforce_types(str, str)
def greet_world(greet, name):
    return f'{greet} {name}'

@enforce_types(int, int)
def divide(n1, n2):
    print(n1 / n2)

print(greet_world('HELLO', 5))
divide('1', 5)