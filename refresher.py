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
    for army in range(num_of_armies):
        for smiley in range(1, num_of_rows + 1):
            print(smile * smiley)

print('create_smile_armies(): ', create_smile_armies(5, 5))

# create intersection function that accepts two two lists and returns a list of intersection
def intersection(a, b):
    return [num for num in a if num in b]

print('intersection(): ', intersection([1,2,3,4],[3,4,5,6]))

""" ------------------------------------------------- """
""" ------------------------------------------------- """
""" --------------------- list ---------------------- """
""" ------------------------------------------------- """
""" ------------------------------------------------- """
print_art('list')

# create low_reversal function that accepts a list of names, returning a list of it reversed and lowercase
def lower_reversal(names):
    return [name[::-1].lower() for name in names]

print('lower_reversal(): ', lower_reversal(["Elie", "Tim", "Matt"]))

# create get_n_matrix that accepts an N and returns a NxN matrix of stars
def get_n_matrix(N): 
    return [['*' * N for c in range(1,N+1)] for r in range(1,N+1)]

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
    my_dict1 = {}.fromkeys(list(str1), 0)
    for i, (key, value) in enumerate(my_dict1.items()):
        my_dict1.update({key: str2[i] + str(value)})
    
    my_dict2 = {str1[i]: str2[i] for i in range(len(str1))}

    return [my_dict1, my_dict2]

print('dict_it_up(): ', dict_it_up('ABC', '123'))

# create do_it_all function that accepts a list, converts it into tuple and returns a unique list
def do_it_all(nums):
    nums = tuple(nums)
    nums = set(nums)
    return list(nums)

print('do_it_all(): ', do_it_all([1,2,2,3,3,3,4,4,4,4]))

# create multiple_letter_count function that accepts a string and returns a dict that counts the number of occurence of each letter
def multiple_letter_count(string):
    string = string.lower()
    return {c:string.count(c) for c in set(string)}

print('multiple_letter_count(): ', multiple_letter_count('Ellie'))

# create check_palindrome that accepts a string and returns boolean
def check_palindrome(string):
    string = string.lower()
    return string == string[::-1]

print('check_palindrome(): ', check_palindrome('Rotator'))

# create intersection_join() that returns a list of intersection between two lists using join
def intersection_join(a, b):
    return list(set(a) & set(b))

print('intersection_join(): ', intersection_join([1,2,3,4,5], [-1,-2,3,2,6,7]))

""" ------------------------------------------------- """
""" ------------------------------------------------- """
""" ------------ lambda, *args, *kwargs ------------- """
""" ------------------------------------------------- """
""" ------------------------------------------------- """
print_art('lambda, *args, *kwargs')

# given a list of nums and a callback that will validate each element is truthy/falsy, return a partition of truthy list and falsy list
def partition(nums, callback):
    return [[n for n in nums if callback(n)], [n for n in nums if not callback(n)]]

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
    return list(map(lambda n: n - 1, l))

print('decrement_list(): ', decrement_list([-1,3,32,5,6,-5,-8]))

# create a function, is_all_strings, that accepts list and returns boolean if list contains all strings
def is_all_strings(l):
    return all(type(s) == str for s in l)

print('is_all_strings(): ', is_all_strings(['hey','hello','hi',5,6,-5,-8]))

# given dict, create get_longest_lyrics_songs function that accepts a playlist and returns it sorted by longest lyrics
def get_longest_lyrics_songs(l):
    return sorted(l, key=lambda s: len(s['lyric']), reverse=True)

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
    return max(abs(n) for n in l)

print('max_magnitude(): ', max_magnitude([-1, -3, -4, 1, 2,9,11, -12]))

# given three lists of student names, midterm grades, and final grades, create function that returns a dict of students and their average grades
# do both comprehension and lambda approaches
students = ['aang', 'korra', 'sato']
finals = [98, 89, 99]
midterms = [91, 95, 90]
def student_avg_grades_lambda(students, finals, midterms):
    return dict(
        zip(
            students,
            map(lambda pair: (sum([pair[0], pair[1]]) / 2), zip(finals, midterms))
        )
    )

def student_avg_grades_list(students, finals, midterms):
    return {student[0]: ((student[1] + student[2]) / 2) for student in zip(students, finals, midterms)}

print('student_avg_grades_lambda(): ', student_avg_grades_lambda(students, finals, midterms))
print('student_avg_grades_list(): ', student_avg_grades_list(students, finals, midterms))

# given two string, return one string that's interwoven of the two provided strings
def interleave(str1, str2):
    return ''.join(''.join(pair) for pair in zip(str1, str2))

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
    try:
        return num1 / num2
    except TypeError:
        return "Please provide two integers or floats"
    except ZeroDivisionError:
        return "Please do not divide by zero"

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
    active_users = 0
    banned_users = []

    @classmethod
    def from_csv(cls, csv):
        username,age = csv.split(',')
        return cls(username, int(age))

    def __init__(self, username, age, type = 'member'):
        if username in User.banned_users:
            raise ValueError(f'User {username} is banned.')
        self.username = username
        self.age = age
        self.type = type
        self.likes = 0
        self._status = 'Active'
        User.active_users += 1

    def __repr__(self):
        return f'{self.username} has {self.likes} of likes.'

    def logout(self):
        User.active_users -= 1

    def add_like(self):
        self.likes += 1

    def change_username(self, username):
        self.username = username

    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, status):
        if status == 'banned':
            self._status = status
            self.likes = 0
            User.active_users -= 1
            User.banned_users.append(self.username)

class Admin(User):
    active_admins = 0
    
    @classmethod
    def display_active_admins(cls):
        return cls.active_admins

    def __init__(self, username, age, type):
        super().__init__(username, age, type)
        self._users_banned = []
        Admin.active_admins += 1

    def __repr__(self):
        return f'{self.username} banned {len(self._users_banned)} users'

    def ban_user(self, user, reason):
        user.status = 'banned'
        self._users_banned.append({'user': user, 'reason': reason})

    def logout(self):
        User.active_users -= 1
        Admin.active_admins -= 1

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
    def get_fib(i):
        if i in (0, 1):
            return i
        return get_fib(i - 1) + get_fib(i - 2)
   
    return [get_fib(i) for i in range(n)]

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
    import time

    g_start_time = time.time()
    g = next((a for a in accounts if a['account_number'] == account_number), None)
    g_time = time.time() - g_start_time
    print(f'compare_generator_v_list Time elapsed for Generator: {g_time}', g)
    
    l_start_time = time.time()
    l = [a for a in accounts if a['account_number'] == account_number][0]
    l_time = time.time() - l_start_time
    print(f'compare_generator_v_list Time elapsed for List: {l_time}', l)


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
    import time
    @wraps(fn) # with wraps, __name__, __doc__, and help will properly preserve the func and reference it
    def wrapper(*args, **kwargs):
        print(f'Executing {fn.__name__}')
        print(f'The function purpose: {fn.__doc__}')
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        print(f'Time elapsed: {end_time - start_time}')
        return result
    return wrapper

@log_function_executions
def add(n1, n2):
    """Accepts two arguments, n1 and n2, and sums the two arguments"""
    return n1 + n2

@log_function_executions
def multiply(n1, n2):
    """Accepts two arguments, n1 and n2, and multiplies the two arguments"""
    return n1 * n2

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
    from csv import reader, writer
    count = 0

    with open('../practice.csv') as file:
        csv_reader = reader(file)
        rows = list(csv_reader)
    
    with open('../practice.csv', 'w') as file:
        csv_writer = writer(file)
        for row in rows:
            if row[0] == name:
                count += 1
                csv_writer.writerow([new_name, row[1], row[2]])
            else:
                csv_writer.writerow(row)

    return count

print('update_users_in_csv(): ', update_users_in_csv('Panda', 'PANDA'))

""" ------------------------------------------------- """
""" ------------------------------------------------- """
""" --------------------- regex --------------------- """
""" ------------------------------------------------- """
""" ------------------------------------------------- """
print_art('regex')

# create parse_date function that accepts a DMY date string and returns a dict of the date and date must be exact match
def parse_date(string):
    import re
    match = re.fullmatch(r'(?P<d>\d\d)[,./](?P<m>\d\d)[,./](?P<y>\d{4})', string)
    if match:
        return {
            'd': match.group('d'),
            'm': match.group('m'),
            'y': match.group('y'),
        }
    return None

print('parse_date(): ', parse_date('01/22/1999'))

""" ------------------------------------------------- """
""" ------------------------------------------------- """
""" -------------------- sqlite3 -------------------- """
""" ------------------------------------------------- """
""" ------------------------------------------------- """
print_art('sqlite3')

def get_scraped_books():
    import sqlite3
    conn = sqlite3.connect('../scraped_books.db')
    c = conn.cursor()
    
    query = f'SELECT * FROM books WHERE rating=? AND price<?'
    c.execute(query, (5, 50))
    books = c.fetchall()
    
    conn.commit()
    conn.close()

    print(books)

get_scraped_books()