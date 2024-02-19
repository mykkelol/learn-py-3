""" 
Tuples
    - ordered collection or grouping of items that's immutable
        - example: numbers = (1, 2, 3, 4)
        - example: tuple([1,3,3,7]) = (1, 3, 3, 7)
        - example: (1,3,(3,7))[2][1] = 7
        - example: (1,) cannot be (1)
    - given it's immutable, it's fast and more lightweight than lists
    - tuples can be used as keys in dict
        - example: { (37.7749, 122.4449) : 'San Francisco office' }

Tuple methods
    - .count(value)
    - .index(value)

Sets
    - collection of items that don't have duplicated values and are not ordered
        - example: set({1,2,3,4,5,5,5}) = {1,2,3,4,5}
        - example: {1,3,3,7}
    - cannot be accessed by index and is lightweight than lists or dict but can still be accessed via loop
        - example: for num in {1,3,3,7}
    - useful to retrieve uniques
        - example: list(set([1,3,3,7])) = [1,3,7]
    - sets comprehension
        - example: {x**2 for x in range(10)}
        - example: len({char for char in 'sequoia' if char in 'aeiou'}) == 5

Set methods
    - .add(value)
    - .remove(value) - will error if value doesn't exist
    - .discard(value) - similar to remove but doesn't error
    - .copy()
    - .clear()
    - set1 | set2 - set union between two sets to create a set of unique values; similar to union all
    - set1 & set2 - set intersection between two sets to create a set of common values; similar to inner join

"""