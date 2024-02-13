""" 
    'not' logical operator
        - not is a logical negation 
        - not is one of other python logical operators such as logical conjuction 'and' and logical disjunction 'or'
        - in short, not is "truthy if the opposite is true" or if it results in true, then false vice versa
        - example 1: not 1 > 5 = true
        - example 2: not (1 + 3 == 4 and 1 - 1 == 0) = false
        - example 3: not (1 + 3 == 5 and 1 - 1 == 0) = true
        - example 4: if not (1 + 3 == 5 and 1 - 1 == 0)

    'is' vs '=='
        - similar comparators but are not the same
        - '==' compares to see if the values are the same
        - 'is' compares to see if the values/variables are stored in the same place in memory
        - example 1: 
            a = 1
            a == 1 # true
            a is 1 # true
        - example 2: 
            a = [1, 2, 3]
            b = [1, 2, 3] # creates a new place in memory
            a == b # true
            a is b # false
            c = b
            c is b # true
"""