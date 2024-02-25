""" 

Iterables vs Iterators
    - iterable - object that can be iterated on such as str, tuple, list, etc. that can return one element at a time when next() is called on it
    - iterator - object that returns an iterator when iter(iterable) is called on it
        - example: next([1,2,3]) # will fail because while it's an iterable, it's not an iterator
        - example: next(iter([1,2,3])) # iter converts our list to an iterator and next will return 1 on first try and 2, 3 thereafter
    - above examples of iterator illustrates that underneath, for loop in py is actually just running iter() or our iterable and next() each iteration
    - if we keep run next() on an iterator when there's nothing else to iterate, py of course raises StopIteration
    - in class, if there's an instance attribute we'd like to iterate on without accessing the attributes direcly we can use dunder __iter__
        - example: class User: self.my_records ...  def __iter__(self): return iter(self.my_records)
        - in this example, we can go from for x in User.my_records to for x in User

Generators
    - generators are iterators that allow us to use keyword 'yield' and can be created with either generator function or expression
    - it's powerful in that unlike regular functions that uses keyword 'return' to return a value, it uses 'yield' to do so
    - yield is useful in that after a function is called and yielded, we can call that same function and it stores the value yielded from the last time it was called
        - example:
            def count_to_max(max):
                count = 1
                while count <= max:
                    yield count
                    count += 1
            counter = count_to_max(5)
            next(counter) #1
            next(counter) #2
            next(counter) #3 this is possible because generator function always returns a generator which again are iterators
    - hard to see its usefulness with function but in generator expression, it's useful when we don't have to convert something into a list to get what we need
        - example with generator expression: (n > 1 for n in range(2, 11)) # True
        - example without generator: all([n > 1 for n in range(2, 11)]) # True
    - lastly, generators leverages much less memory than a function returning a list a single time vs. generator yielding multiple generators/values
    - this doesn't mean generators are faster than list, it's just less memory. list are still often faster

Generator Expression
    - generator expression are just generator functions but not within functions
    - this means it allows us to leverage generators performant and lightweight memory usage
    - generator expression are useful for scenarios where we only need to know True/False without a list returned
        - example without generator: any([n > 0 for n in range(1, 10)]) # True but leverages a list
        - example with generator: any(n > 0 for n in range(1, 10)) # True but without list or any other comprehension types
"""

# create our own for loop using iterator and next only to understand innings of iterators and generators
def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            iterate = next(iterator)
        except StopIteration:
            break
        else:
            func(iterate)

def square(n):
    print(n * n)

my_for([1,2,3], print)
my_for([1,2,3], square)


# write a function that accepts a max length of a list and returns list of fib sequence while viewing the memory in runtime
def get_fib_list(max):
    nums = []
    x, y = 0, 1
    while len(nums) < max:
        nums.append(x)
        x, y = y, x + y
    return nums

print(get_fib_list(10))

# write a generator function that accepts a max int and returns a fib sequence while viewing the memory in runtime
def get_fib_generator(max):
    i = 0
    x, y = 0, 1
    while i < max:
        yield x
        x, y = y, x + y
        i += 1

for fib in get_fib_generator(10):
    print(fib)

# write an actual fib for fun
def get_fib(n):
    if n in (0, 1):
        return n
    return get_fib(n - 1) + get_fib(n - 2)

print([get_fib(n) for n in range(10)])

# write a generator that accepts number and count, returning the multiple of the number for count of times
def get_multiples(num = 2, count = 10):
    next_num = 0
    i = 0
    while i < count:
        next_num += num
        yield next_num
        i += 1 

# write a generator that accepts number, returning the multiple of the number for number of times
def get_unlimited_multiples(num = 1):
    next_num = 0
    while True:
        next_num += num
        yield next_num

# write a function that compares the time complexity of using generator expression vs. without when summing a range up to n
def compare_generator_v_list(n):
    import time
    
    gen_start_time = time.time()
    print(sum(num for num in range(n)))
    gen_end_time = time.time()
    gen_time = gen_end_time - gen_start_time
    
    
    list_start_time = time.time()
    print(sum([num for num in range(n)]))
    list_end_time = time.time()
    list_time = list_end_time- list_start_time

    print(f'sum(num for num in range(n)) took: {gen_time}')
    print(f'sum([num for num in range(n)]) took: {list_time}')

# compare_generator_v_list(100000000) # 2 second diff!
