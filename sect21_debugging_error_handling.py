""" 
    Common Errors
        - SyntaxError - occurs when Python encounters incorrect syntax it cannot parse
        - NameError - occurs when a variable is not defined i.e. hasn't been assigned yet
        - TypeError - occurs when an operation or function is applied to wrong type e.g. len(5) or 3 + 's'
        - IndexError - occurs when accessing element in a list using invalid index e.g. [][-1]
        - ValueError - occurs when an operation or function receives correct data type but not appropriate value as arguments e.g. int('foo')
        - KeyError - occurs when a dictionary doesn't have a key e.g. {}['foo']
        - AttributeError - occurs when a variable doesn't have an attribute e.g. [1,2,3].hello()

    raise
        - similar to JS throw but can be used with existing errors
        - example: raise NameError('hello!')
        - example: if type(text) is not str: raise TypeError('type entered not a string')

    try/except blocks
        - similar to JS try/catch
        - example:
            try:
                ...
            except NameError as e:
                print(e)
            except:
                print('unhandled error')
        - example:
            while True:
                try:
                    num = int(input('enter a number you silly goose: '))
                except:
                    print('not a number silly...') # any datatype not number
                else:
                    print('yay!') # if no error caught
                    break
                finally:
                    print('my pleasure!') # run regardless if except/else runs

    import pdb
        - pdb.set_trace() - to set breakpoints in code for debugging with commands below
            - l - list all lines for debugging
            - n - go to next line
            - p - prints a variable but we can also enter the variables directly; however, still useful if any variable matches command e.g. variable named "l"
            - c - continue and finish debugging
        - typically imported within block for debugging and is removed after debugging
"""

# import pdb to debug and explain each line below
first = 'First'
second = 'Second'
import pdb; pdb.set_trace()
result = first + second # shows in pdb
third = 'Third' # in pdb, if we access third, we'll get NameError variable not defined
result += third
print(result)

""" 
Write a function called divide, which accepts two parameters (you can call them num1 and num2).
The function should return the result of num1 divided by num2. 

If you do not pass the correct type of arguments to the function, it should return the string "Please provide two integers or floats".
If you pass as the second argument a 0, Python will raise a ZeroDivisionError, 
so if this function is invoked with a 0 as the value of num2, 
return the string "Please do not divide by zero"
"""
def divde(num1, num2):
    try:
        result = num1 / num2
    except TypeError:
        return "Please provide two integers or floats"