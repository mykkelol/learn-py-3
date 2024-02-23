""" 
    OOP
        - method of programming to model process or things in the world as class or object with a goal of encapsulating into logical, hierarchy groupings
        - class - blueprints, recipes, or specifications for objects containing methods (functions) and attributes
        - instance (self) - objects constructed from a class blueprint that contains their class' methods and attributes
            - everything in python has a class blueprint e.g. int, list, etc.
            - in terminal, we can run help(int) and it'll show the class' methods and attributes
            - this is because every time we create an int or list variables, we're creating a new instance of class int or class list
        - encapsulation - grouping of private vs. public methods and attributes within classes, making abstraction possible
            - e.g. car class may make turn, shift gear, turn light on, etc. public methods and color, model, type public attributes
            - e.g. car class may make powering steering, electrical wires, battery, etc. private methods and engine number private attributes
        - abstraction - expose only "relevant" and public data in a class interface, hiding private methods/attributes (aka "inner workings") from users
        - class attributes - attributes that differs from instance attributes and can also be defined directly on a class so that it can be shared across all instances of the class and the class itself
        - @classmethods - syntax sugar that turns method defined directly under as a class method and are methods that concerns the class itself, not the instanes (hence self becomes cls)

    __name__ - in general, a convention that we should avoid overridng dunder as it's reserved for many python builtin methods e.g. __init__, etc.
    _name - single underscore is just a convention to indicate a private method or attribute
    __name - double underscores is Name Mangling wherein py will prefix the class name (e.g. ClassName__name) and used in inheritance
    __init__ - similar to JS constructor() to initialize and construct a new instance
    __repr__ - py dunder "representation" returns a nice, clean string representation of class object when we print the instance since without it, it'd return the literal unreadable class object

"""

# create class User that has class attributes, active_users and banned_users
# the class should have three instance attributes: username, likes, age
# the class should have three instance methods: logout, likes, change_username
# the class should have one class method: from_csv
# the class should print the username and total likes

class User:
    active_users = 0
    banned_users = []

    @classmethod
    def from_csv(cls, csv):
        username,age = csv.split(',')
        return cls(username, int(age))

    def __init__(self, username, age):
        if username in User.banned_users:
            raise ValueError(f'User {username} is banned.')
        self.username = username
        self.age = age
        self.likes = 0
        User.active_users += 1

    def __repr__(self):
        return f'{self.username} has {self.likes} of likes.'

    def logout(self):
        User.active_users -= 1

    def add_like(self):
        self.likes += 1

    def change_username(self, username):
        self.username = username

    def ban_username(self, username):
        self.likes = 0
        User.active_users -= 1
        User.banned_users.append(username)

reverseBoomer1337 = User('reverseBoomer1337', 49)
print(reverseBoomer1337)
reverseBoomer1337.change_username('boomer1337')
reverseBoomer1337.add_like()
print(User.active_users)
print(reverseBoomer1337.active_users)
print(reverseBoomer1337)

x_freakinspreadsheets_x = User.from_csv('x_freakinspreadsheets_x,35')
print(x_freakinspreadsheets_x)