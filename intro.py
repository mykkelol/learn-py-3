""" 
Operators

    ** - exponentiation
    % - modulo
    // - integer division bc python respects float v int and won't inherently round without explicit (e.g. 1/2 automatically rounds down to float as .5 but // will round to 0 and stays as int)
    *, /, -, + - typical

Variables and Strings

    Dynamic typing - similar to JS, Python allows variables reassignment to different types (e.g. name = 'Micheal' can be reassigned to name = False)
    Dunder - double under are variables with prefix and subfix with underscore to indicate private and do not use (_dnu_)
    "None" - special value that's equivalent to null in other languages
    String interpolation - python so mid it needs a special key 'f' to allow interpolation (e.g. f'{js_better} is better than {py_mid}')
    Negative string index - python allows negative string index which is the reverse (e.g. 'animal'[-1] = l)
    Data type conversion - string interpolation or division vs. integer divsion implicitly converts data type. As for explicitly converting, python allows
        - int(9.99) = 9
        - float('9.99') = 9.99
        - float(9) = 9.0
        - str([1,2,3]) = '[1, 2, 3]'
"""