""" 
    Modules
        - python files that keep files small and enable code resuse
        - hundreds of built-in python modules available for use (requests, base64, random, etc.)
        - syntax is: from MODULE import some methods
            - example: from random import choice as c, randint
            - example: import keyword
        - every file has a __name__ variable and if the file being run on is the main, its value is __main__ otherwise the actual filename
            - example to prevent block of code on import: if __name__ == "__main__": ...

    External modules
        - PyPi - python package index is a collection of external python packages similar to npm
        - pip - package installer for python
            - example in termminal: python3 -m pip install NAME_OF_PACKAGE
            - example in termminal: python3 -m pip install autopep8 ... autopep8 --in-place SOME_FILE.py
"""


# create a function that accepts variable number of arguments and returns true if of the argument exist as python keywords
def contain_keywords(*args):
    from keyword import iskeyword
    return any(iskeyword(s) for s in args)

# create a function get_interwoven() that uses interleave(str1, str2) function from sect20_lmabdas.py
def get_interwoven(str1, str2):
    from sect20_lambdas import interleave
    return interleave(str1, str2)

# use pip to download and import pyfiglet to print messages in ASCII!
def print_art(message, color):
    # python3 -m pip install pyfiglet
    # python3 -m pip install termcolor
    from pyfiglet import Figlet
    from termcolor import colored

    ascii_art = Figlet(font='slant').renderText(message)
    colored_ascii = colored(ascii_art, color=color, on_color='on_green', attrs=['blink'])

    print(colored_ascii)
    return None

message = input('give me message to print ')
color = input('what is your fav color? ')
print_art(message, color)