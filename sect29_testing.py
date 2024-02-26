""" 
    Testing 
        - concept of creating test cases to ensure minimal bugs in code, new features or refactoring doesn't introduce new bugs, and for some make dev more fun
        - py has three builtin functionalities for testing: assert, doctests, and unittest
        
    Test Driven Development
        - most test cases are done after building our core code but TDD is opposite
        - TDD is a framework where development starts with writing tests and only after tests are done we can write core code
        - once all tests passes, feature is considered completed
        - Red, Green, Refactor - starts with writing tests that fails (Red), MVP code with tests that succeeds (Green), and refactor MVP code

    Unit Testing
        - test smallest parts of an application in isolation i.e. units
        - units are individual classes, modules, or functions
        - units are NOT classes or modules with dependencies

    assert
        - py keyword that accepts an expression and an optional default value (see Example A)
        - if expression is truthy, returns None and proceeds but raises AssertionError if falsy
        - while powerful for testing, it's no longer commonly used given a single flag "-O" will make the entire file not evaluate the keyword

    doctests
        - as name implies, a way to test in python by writing the red and green tests directly under docs and with repl ">>>" (see Example B)
        - can be really buggy since it's like raw comments and freaks out with whitespace, if "" was used instead of '', etc.
        - while the code is compiled, python will run all the doctests and cleanly describe the test successes and failures
        - must state when compiling "python3 -m doctest -v my_file.py"

    unittest
        - most common builtin test in py that follows unit testing framework
        - py has a builtin module "unittest" and with it is a class "unittest.TestCase" that we can inherit and encapsulate our tests into
        - unittest will then inherit many assertions (see example C)
        - unittest also allow testing for errors with assertRaises but the function tested must raise an error for us to test
        - unittest and all our tests can be executed by running "unittest.main()" 
        - unittest also has the before/after hooks concept where setup/teardown e.g. in a large app or class that requires attributes to test, we can use setUp to test
"""

#example A: write a function adds a and b, assserting if a and b are gte to 0
def add_with_assert(a, b):
    assert a > 0 and b > 0, 'Both values must be gte 0'
    return a + b

# print(add_with_assert(1, -1)) 

# example B: write a function that doubles all elements of a list using doctests to test
# notice if docstring was written as [1,2,3] or ["aa". "bb", "cc"] it'd fail since quote and whitespace matters
# notice that we can only test with doctests by compiling with "python3 -m doctest -v my_file.py"
def double_with_doctest(values):
    """ accepts iterable and doubles all its values

    >>> double_with_doctest([1,2,3])
    [2, 4, 6]
    
    >>> double_with_doctest([])
    []
    
    >>> double_with_doctest(['a','b','c'])
    ['aa', 'bb', 'cc']

    >>> double_with_doctest([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * n for n in values]
 
print(double_with_doctest([1, 2, 3])) 

# example C: write test cases of functions from and encapsulates in class FunctionTests() using unittest
# notice that when compiling with -v, the doc of our tests are also displayed even if it doesn't fail
import unittest
from sect20_lambdas import interleave, triple_and_filter

class FunctionTests(unittest.TestCase):
    def setUp(self):
        # this setup shows what we can do with unittest
        # if say we wanted to test a class where we need to create the instance first, we could do it in setUp
        # this allow us to avoid having to create multiple instances in each and every test
        self.some_attribute = 'hi_there'
    
    def test_interleave_success(self): # notice that prefix test_ and suffix _whatToTest must be added
        """testing interleave logic"""
        self.assertEqual(
            interleave('lzr', 'iad'),
            'lizard'
        )
    
    def test_interleave_string(self): # notice that prefix test_ and suffix _whatToTest must be added
        """all arguments must be strings"""
        with self.assertRaises(ValueError):
            interleave(123213, True)

    def test_triple_and_filter_right(self):
        """testing if elements that are divisible of 4 are returned and tripled"""
        self.assertEqual(
            triple_and_filter([0,1,2,3,4,5,6,7,8,9]),
            [0, 12, 24]
        )

if __name__ == '__main__':
    unittest.main()
