""" 
    Functions
        - there's a important distinction between parameter (the variable in the function) and arguments (the values passed as the variable into the function)
            - example: def my_func(param1, param2): ....
            - example: my_func(arg1, arg2)
        - in python there's a concept of defensive programming and default params are example of such defensive logic
            - to use function as a default param, use keyword fn
            - example: math(a, b, fn=add) wherein add(a, b) is a function

    Keyword arguments
        - in functions, order of arguments passed matters but if we know the parameters, keyword arguments can be used to bypass ordering
            - example: def get_fullname(first, last): ...
            - example: get_fullname(last='Squarepants', first='Spongebob')

    Function scope
        - global
            - unlike JS, python disallow usage of global scoped variables in functions and will raise errors
            - to use global variable, keyword global must be explicitly used
            - example: 
                total = 0
                def add_to_total(num):
                    global total 
                    global += num
        - nonlocal
            - when needing to access variables that are within the nested function but not within global
            - it's a different keyword 'nonlocal' that must be explicitly used
            - example:
                def outer():
                    count = 0
                    def inner():
                        nonlocal count
                        count += 1
                        return count
                    return inner()

    Documenting functions
        - when documentiong function, use multiline commenting on first line within block of function
        - my_function.__doc__ - this is because python has a method that'd allow us to access documentation
         - example:
                def outer():
                    \""" counts and return total count \"""
                    count = 0
                    def inner():
                        nonlocal count
                        count += 1
                        return count
                    return inner()
                
                outer.__doc__
                [].pop.__doc__
                [].append.__doc__

    *args
        - similar to JS rest/spread but returns a tuple
        - example: def sum_numbers(num1, *nums)

    **kwargs
        - keyword args is like *args but gathers keywords to produce a dictionary
        - example: def fav_colors(**people)... fav_colors(bob='purple',jane='red',joe='blue)

    Parameter ordering
        - in exact order: parameters, *args, default parameters, **kwargs
    
    Unpacking list & tuple (*list)
        - if we want to pass in multiple args as a single list or tuple, we need to use unpack tuple
        - example: my_func(*[1,2,3,4]) or my_func(*(1,3,3,7))

    Unpacking dictionary (**dict)
        - similar to unpacking list & tuple, just use double stars
        - example: my_funct(**my_dict)
"""

# create a function that accepts a number and returns the corresponding day in a week with Sunday as 1
def return_day(n):
    try:
        return ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"][n-1]
    except IndexError as e:
        return None
def return_day(n):
    days = ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
    return {i:days[i] for i in range(len(days))}.get(n-1)

# create a function that accepts a string and returns a dict that counts the number of occurence of each letter
def multiple_letter_count(string):
    return {l: string.count(l) for l in string}
def multiple_letter_count(string): # imo this approach seems more optimal
    return {l: string.count(l) for l in set(string)}

def check_palindrome(string):
    stripped = string.lower().strip()
    return stripped == stripped[::-1]

# given a list of nums, return product of all evens
def product_of_even(nums):
    product = 1
    for num in nums:
        if num % 2 == 0:
            product *= num
    return product

# capitalize without using python function
def capitalize_string(string):
    return string[0].upper() + string[1:]

# given list of truthy and falsy values, return list of truthy only
def compact(collection):
    return [truth for truth in collection if truth]

# given two collection, find their intersection/inner joins
def intersection(collection1, collection2):
    return list(set(collection1) & set(collection2))

# given a list of nums and a callback that will validate each element is truthy/falsy, return a partition of truthy list and falsy list
def isEven(num):
    return num % 2 == 0

def partition(nums, callback): 
    return [[n for n in nums if callback(n)], [n for n in nums if not callback(n)]] # not efficient but cool lol

# explain what each parameter will equate if printed
def all_my_friends(a, b, *numbers, word='woof', **words):
    return numbers
    # parameters of 1, 2 
    # *args with tuple of (3,) 
    # default parameter of 'woof' 
    # **kwargs with dict of {'beep':1,'boop':2,'bop':3}

all_my_friends(1, 2, 3, beep=1,boop=2,bop=3)

# create a calculator that accepts kwargs (operation, make_float, first, second, message) and returns a string message with the result
# if make_float is false then return an integer else float
# if first or second are not provided, assume 0
# if message is not provided, default to "The result is N"
# supported operations are add, subtract, divide, multiple

def calculate(**args):
    result = 0
    make_float = args.get('make_float', False)
    operation = args.get('operation')
    message = args.get('message', 'The result is')
    first = args.get('first', 0)
    second = args.get('second', 0)
    
    if operation == 'add':
        result = first + second
    elif operation == 'subtract':
        result = first - second
    elif operation == 'divide':
        result = first / second
    elif operation == 'multiply':
        result = first * second
        
    result = float(result) if make_float else int(result)
    return f"{message} {result}"