""" 

Common list functions
    - list[-1]reverse retrieval starts at -1
    - stringDelimiter.join(list) - e.g. ', '.join([1,3,3,7]) is 1,3,3,7
    - .count(item)
    - .reverse() - can use [::-1] as well
    - .sort()
    - .index(item) - returns index of first item found and similar to JS .find/.indexOf but can specify start/end and errors if not found
        - [1,3,3,7].index(3, 2) starts at 2 and returns 2
        - [1,3,3,3,3,7].index(3, 4, 5) starts at 4, ends at 5 and returns 4
    - slicing with [start:end:step]
        - [start:]
            - returns empty array if invalid start index e.g. [1,2,3,4][4:] returns []
            - if end is not provided, inclusive of all values to the end e.g. [1,2,3,4,5][2:] returns [3,4,5]
                - this also means that [0:] is equivalent to creating a shallow copy of current list
                - [:] is shorthand for [0:]
                - we can test it's shallow copy wherein list_a == list_a[:] returns true but list_a is list_a[:] returns false
            - similar to reverse retrieval can slice with negative index e.g. [1,2,3,4][-3:] returns [2,3,4] since it's inclusive up to -3
        - [:end] the index to copy up to (exclusive counting)
            - since it's exclusive, the index that doesn't exist means it copies the whole list e.g. [1,2,3,4][:6] = [1,2,3,4]
            - end can also be negative but it means index to excludes from copy e.g. [1,2,3,4][-1] = [1,2,3] or [1,2,3,4][1:-1] = [2,3]
        - [::step] how many to skip
            - [1,2,3,4,5,6][::2] creates [1,3,5]
            - with negative skips, we reverse the copied list e.g. [1,2,3,4,5][1::-1] = [2,1] or [1,2,3,4,5][-1::-1] = [5,4,3,2,1]
        - can use to modify arrays
            - numbers = [1,2,3,4,5,6] and numbers[1:3] = ['a','b','c'] results in [1,'a','b','c',5,6]
            - ['apple','yellow','orange'][1][::-1] results in 'egnaro'
    - swap
        - names = ['james', 'jane']
        - names[0], names[1] = names[1], names[0] results in ['jane', 'james']

Adding to list
    - .append(index)
    - .extend(list)
    - .insert(index, value) - insert at specific index but if with -1, never last index but rather index before last 

Removing from list
    - .clear() - clear list completely
    - .pop() - remove last index if not specifed or specific index if specified
    - .remove(item) - remove first value in list e.g [1,3,3,7].remove(3) will remove only index 1

"""