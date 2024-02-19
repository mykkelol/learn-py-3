""" 
    Lambdas
        - short and one-liner functions with no names that's similar to JS anonymous functions (maybe even similar to HOF arrow function?)
            - example (albeit lambda aren't usually stored in variables like so): 
                square = lambda num: num * num
                square(2)
        - similar to when we use .map().reduce() in JS without defining a function, lambdas primary use case is when we need to pass a function to another function that will never be used again

    Built-in python functions
        - map(function, iterable) - runs a lambda for each iterable and returns a map object that can be converted to another data structure
            - example: list(map(lambda n: n * 2, range(6)))
            - example: list(map(lambda name: name[0].upper() + name[1:], ['diana maria', 'nickel', 'rascal']))
        - filter(function, iterable) - runs a lambda for each iterable and returns a filter object of truthy that can be converted to another data structure
            - example: list(filter(lambda n: n % 2 == 0, range(6)))
        - sorted(iterable, key to sort by, reverse=True) - returns sorted list of all items in iterable
            - example: sorted({...'name': 'charlie'..}, key=lambda n: len(some_list['name']), reverse=True)
        - all(iterable) - returns True if ALL elements in a list is truthy
            - example: all([n[0] == 'c' for n in ['casey', 'cody', 'chris', 'charles']]) # True
            - example with generator: all(n[0] == 'c' for n in ['casey', 'cody', 'chris', 'charles'])
                # notice we didn't pass the iterable as a list and this is known as a generator
                # generators are is useful for scenarios like this where we only need to know True/False without a list returned
                # generators are also much more performant and lightweight
        - any(iterable) - returns True if ANY element in a list is truthy i.e. at least one
            - example: all([n[0] == 'c' for n in ['casey', 'kody', 'khris', 'kristy']]) # True
            - example with generator: all(n[0] == 'c' for n in ['casey', 'kody', 'khris', 'kristy']) # notice we didn't pass the iterable as a list
        - zip(iterable1, iterable2, iterableN) - returns zip object of tuples where i-nth of iterable1 aligns with i-nth of iterable2, assuming both iterables are of equal length
            - example: dict(zip([1,2,3],['a','b','c'])) # { 1:'a', 2:'b', 3:'c' }
            - example with unpacking: list(zip(*[(0,1),(1,2),[2,3]]) # [(0,1,2), (1,2,3)]
        - max()/min()/reversed(iterator) - returns largest/smallest item of iterable or largest/smallest of any of two or more arguments
            - example: max(len(n) for n in ['arya','tim','rascal'])
            - example: min(['arya','tim','rascal'], lambda s: len(s))
        - abs(number)/math.fabs(number)/sum(iterable, start)/round(number, ndigits)
            - example: math.fabs(-4) # 4.00 returns absolute in floats
            - example: sum((1,2,3), -6) # 0 as it starts with -6
            - example: sum(1.2) # 1 rounding to nearest integer unless ndigit is provided
        - sys.getsizeof()
            - within sys import, allows us to see the size of the memory stored
            - example: sys.getsizeof(n > 0 for n in range(1000)) < sys.getsizeof([n > 0 for n in range(1000)]) # False, notice how generator much more lightweight

    Map + Filter
        - similar to JS, we can combine and chain! while fun, comprehension are of course more scalable and preferable
            - example with lambda: list(map(lambda n: f"your name {n} is gt 5 chars", filter(lambda n: len(n) > 5, ['bob', 'jane','nickel'])))
            - example with comprehension: [f"your name {n} is gt 5 chars" for n in ['bob', 'jane','nickel']]

"""

# create a function, decrement_list, that accepts a list of nums and returns a list with all element decremented by 1
# use map and lambda, not comprehension
def decrement_list(l):
    return list(map(lambda n: n - 1, l))

# create a function, remove_negatives, that accepts a list of nums and returns a list with all elements not negative
# use map and lambda, not comprehension
def remove_negatives(l):
    return list(map(lambda n: n >= 0, l))

# create a function, is_all_strings, that accepts list and returns boolean if list contains all strings
def is_all_strings(l):
    return all(type(s) == str for s in l)

# given the following dict, create a function get_longest_lyrics_songs, that accepts a playlist and returns it sorted by longest lyrics
playlist = [
    {
        'name': 'Talking to the moon',
        'lyric': 'mooooooooo mooooooooon'
    },
    {
        'name': 'Malibu',
        'lyric': 'ma bu'
    },
    {
        'name': 'Smooth criminal',
        'lyric': 'mooooooooonwalking'
    },
]
def get_longest_lyrics_songs(l):
    return sorted(l, key=lambda s: len(s), reverse=True)

def get_longest_lyrics(l):
    return max(l,key=lambda s: len(s['lyric']))

# given a list, create a function that returns a tuple of (min, max)
def get_extremes(l):
    return (min(l), max(l))

# given a list, create a function that returns the max magnitude (furthest from zero)
def max_magnitude(l):
    return max(abs(n) for n in l)

# given a variable number of arguments, create a function that returns sum of even values
def sum_of_evens(*l):
    return sum(n for n in l if n % 2 == 0)

# given three lists of student names, midterm grades, and final grades, create a function that returns a dict of students and their average grades
# do both comprehension and lambda approach
students = ['aang', 'korra', 'sato']
finals = [98, 89, 99]
midterms = [91, 95, 90]
def student_avg_grades(students, finals, midterms):
    lamba_approach = dict(
        zip(
            students,
            map(lambda pair: sum(pair[0], pair[1]) / 2, (finals, midterms))
        )
    )
    comprehension_approach = {student[0]: ((student[1] + student[2]) / 2) for student in zip(students, finals, midterms)}
    return comprehension_approach

# given two string, return one string that's interwoven of the two provided strings
def interleave(str1, str2):
    return ''.join(''.join(pair) for pair in (zip(str1, str2)))

# given list of nums, return list of num divisble by 4 and tripled
def triple_and_filter(l):
    return list(map(lambda n: n * 3, filter(lambda n: n % 4 == 0, l)))