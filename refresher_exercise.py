from pyfiglet import Figlet
from termcolor import colored
from functools import wraps

def print_art(message):
    ascii_art = Figlet().renderText(message)
    colored_ascii = colored(ascii_art, color='blue')

    print(colored_ascii)
    return None

""" ------------------------------------------------- """
""" ------------------------------------------------- """
""" -------------------- basics --------------------- """
""" ------------------------------------------------- """
""" ------------------------------------------------- """
print_art('basics')

# create create_smile_armies function that accepts number of armies and number of rows per army, returning armies of smilies
def create_smile_armies(num_of_armies, num_of_rows):
    smile = '\U0001f600'
    pass    

print('create_smile_armies(): ', create_smile_armies(5, 5))

# create intersection function that accepts two two lists and returns a list of intersection
def intersection(a, b):
    pass

print('intersection(): ', intersection([1,2,3,4],[3,4,5,6]))

""" ------------------------------------------------- """
""" ------------------------------------------------- """
""" --------------------- list ---------------------- """
""" ------------------------------------------------- """
""" ------------------------------------------------- """
print_art('list')

# create low_reversal function that accepts a list of names, returning a list of it reversed and lowercase
def lower_reversal(names):
    pass

print('lower_reversal(): ', lower_reversal(["Elie", "Tim", "Matt"]))

# create get_n_matrix that accepts an N and returns a NxN matrix of stars
def get_n_matrix(N): 
    pass

print('get_n_matrix(): ', get_n_matrix(3))

""" ------------------------------------------------- """
""" ------------------------------------------------- """
""" --------------- dict, tuple, set ---------------- """
""" ------------------------------------------------- """
""" ------------------------------------------------- """
print_art('dict, tuple, set')

# create dict_it_up function that accepts str1 and str2, returning two dicts
# one dict must use fromkeys and update() dict method and returns str2 chars concat with existing value as values
# one dict must use dict comprehension and returns str2 chars as values
def dict_it_up(str1, str2):
    pass

print('dict_it_up(): ', dict_it_up('ABC', '123'))

# create do_it_all function that accepts a list, converts it into tuple and returns a unique list
def do_it_all(nums):
    pass

print('do_it_all(): ', do_it_all([1,2,2,3,3,3,4,4,4,4]))

# create multiple_letter_count function that accepts a string and returns a dict that counts the number of occurence of each letter
def multiple_letter_count(string):
    pass

print('multiple_letter_count(): ', multiple_letter_count('Ellie'))

# create check_palindrome that accepts a string and returns boolean
def check_palindrome(string):
    pass

print('check_palindrome(): ', check_palindrome('Rotator'))

# create intersection_join() that returns a list of intersection between two lists using join
def intersection_join(a, b):
    pass

print('intersection_join(): ', intersection_join([1,2,3,4,5], [-1,-2,3,2,6,7]))

""" ------------------------------------------------- """
""" ------------------------------------------------- """
""" ------------ lambda, *args, *kwargs ------------- """
""" ------------------------------------------------- """
""" ------------------------------------------------- """
print_art('lambda, *args, *kwargs')

# given a list of nums and a callback that will validate each element is truthy/falsy, return a partition of truthy list and falsy list
def partition(nums, callback):
    pass

print('partition(): ', partition([1,2,3,4,5], lambda n: n % 2 == 0))

# explain what each parameter will equate if printed
def all_my_friends(a, b, *numbers, word='woof', **words):
    return numbers
    # parameters of 1, 2 
    # *args with tuple of (3,) 
    # default parameter of 'woof' 
    # **kwargs with dict of {'beep':1,'boop':2,'bop':3}

print('all_my_friends(): ', all_my_friends(1, 2, 3, beep=1,boop=2,bop=3))

# create a function, decrement_list, that accepts a list of nums and returns a list with all element decremented by 1
# use map and lambda, not comprehension
def decrement_list(l):
    pass

print('decrement_list(): ', decrement_list([-1,3,32,5,6,-5,-8]))

# create a function, is_all_strings, that accepts list and returns boolean if list contains all strings
def is_all_strings(l):
    pass

print('is_all_strings(): ', is_all_strings(['hey','hello','hi',5,6,-5,-8]))

# given dict, create get_longest_lyrics_songs function that accepts a playlist and returns it sorted by longest lyrics
def get_longest_lyrics_songs(l):
    pass

print('get_longest_lyrics_songs(): ', get_longest_lyrics_songs([
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
]))

# given a list, create a function that returns the max magnitude (furthest from zero)
def max_magnitude(l):
    pass

print('max_magnitude(): ', max_magnitude([-1, -3, -4, 1, 2,9,11, -12]))

# given three lists of student names, midterm grades, and final grades, create function that returns a dict of students and their average grades
# do both comprehension and lambda approaches
students = ['aang', 'korra', 'sato']
finals = [98, 89, 99]
midterms = [91, 95, 90]
def student_avg_grades_lambda(students, finals, midterms):
    pass

def student_avg_grades_list(students, finals, midterms):
    pass

print('student_avg_grades_lambda(): ', student_avg_grades_lambda(students, finals, midterms))
print('student_avg_grades_list(): ', student_avg_grades_list(students, finals, midterms))

# given two string, return one string that's interwoven of the two provided strings
def interleave(str1, str2):
    pass

print('interleave(): ', interleave('lzr','iad'))

""" ------------------------------------------------- """
""" ------------------------------------------------- """
""" ------------------ debugging -------------------- """
""" ------------------------------------------------- """
""" ------------------------------------------------- """
print_art('debugging')

# import pdb to debug and explain each line below
def run_pdb():
    first = 'First'
    second = 'Second'
    import pdb; pdb.set_trace()
    result = first + second # shows in pdb
    third = 'Third' # in pdb, if we access third, we'll get NameError variable not defined
    result += third
    print(result)

# create divide function that accepts two numbers
# if anything other than nums are provided, return 'Please provide integers or floats'
# if dividng by 0, return 'Please do not divide by zero'
def divide(num1, num2):
    pass

print('divide(): ', divide(1, 0))

""" ------------------------------------------------- """
""" ------------------------------------------------- """
""" --------------------- oop ----------------------- """
""" ------------------------------------------------- """
""" ------------------------------------------------- """
print_art('oop')

# create class User
# the class must have three instance attributes: username, likes, age
# the class must have three instance methods: logout, likes, change_username
# the class must have one class method: from_csv
# the class must have two class attributes, active_users and banned_users
# the class must have three methods to access and write a private instance attribute: status
# the class must print the username and total likes
# create class Admin that inherits User
# the class must have two instance attributes: users_banned, active_admins
# the class must have one instance method: ban_user
# the class must have polymorphed method: logout

class User:
    pass

class Admin(User):
    pass


reverseBoomer1337 = User('reverseBoomer1337', 49)
print(reverseBoomer1337)
reverseBoomer1337.change_username('boomer1337')
reverseBoomer1337.add_like()
print(User.active_users)
print(reverseBoomer1337.active_users)
print(reverseBoomer1337)

x_freakinspreadsheets_x = User.from_csv('x_freakinspreadsheets_x,35')
print(x_freakinspreadsheets_x)

im_an_ra2017 = Admin('im_an_ra2017', 70, 'admin')
print(im_an_ra2017)
print(x_freakinspreadsheets_x.status)
im_an_ra2017.ban_user(x_freakinspreadsheets_x, "used x's in names in 2024")
print(x_freakinspreadsheets_x.status)
print(vars(x_freakinspreadsheets_x))
print(Admin.active_admins)
im_an_ra2017.logout()
print(Admin.active_admins)

""" ------------------------------------------------- """
""" ------------------------------------------------- """
""" ------------ iterators & generators ------------- """
""" ------------------------------------------------- """
""" ------------------------------------------------- """
print_art('iterators & generators')

# write a function that accepts a max length of a list and returns list of fib sequence while viewing the memory in runtime
def get_fib_list(n):
    fib = [0, 1] + [0] * (n-1)
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[1:]

print('get_fib_list(): ', get_fib_list(10))

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

# write two functions, one with gen expression and one with list comprehension, to find a dict within a list and compare performance
def compare_generator_v_list(accounts, account_number):
    pass

compare_generator_v_list([
    { 'account_number': 150720,  'balance': 500},
    { 'account_number': 150303,  'balance': 1500},
    { 'account_number': 150415,  'balance': 198802},
    { 'account_number': 150628,  'balance': 201054},
], 150415)

""" ------------------------------------------------- """
""" ------------------------------------------------- """
""" ------------------ decorators ------------------- """
""" ------------------------------------------------- """
""" ------------------------------------------------- """
print_art('decorators')

# create functions, add and multiply, that uses a decorator that logs and documents math tools
def log_function_executions(fn):
    pass


@log_function_executions
def add(n1, n2):
    pass


@log_function_executions
def multiply(n1, n2):
    pass


print('update_users_in_csv(): ', add(1, 2))

""" ------------------------------------------------- """
""" ------------------------------------------------- """
""" -------------------- testing -------------------- """
""" ------------------------------------------------- """
""" ------------------------------------------------- """
print_art('testing')

# see sect 29

""" ------------------------------------------------- """
""" ------------------------------------------------- """
""" -------------------- fileio --------------------- """
""" ------------------------------------------------- """
""" ------------------------------------------------- """
print_art('fileio')

# create a function that update users' name and return the count of users updated in a csv
def update_users_in_csv(name, new_name):
    pass

print('update_users_in_csv(): ', update_users_in_csv('Panda', 'PANDA'))

""" ------------------------------------------------- """
""" ------------------------------------------------- """
""" --------------------- regex --------------------- """
""" ------------------------------------------------- """
""" ------------------------------------------------- """
print_art('regex')

# create parse_date function that accepts a DMY date string and returns a dict of the date and date must be exact match
def parse_date(string):
    pass

print('parse_date(): ', parse_date('01/22/1999'))

""" ------------------------------------------------- """
""" ------------------------------------------------- """
""" -------------------- sqlite3 -------------------- """
""" ------------------------------------------------- """
""" ------------------------------------------------- """
print_art('sqlite3')

def get_scraped_books():
    pass

get_scraped_books()