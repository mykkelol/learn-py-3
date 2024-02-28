""" 
    "import re" module
        - access to regex methods directly in py
        - re.compile(r'some_regex') - accepts regex expression to create regex expression object with methods we can leverage
        - pattern.search(some_string) - scan through string with pattern for a match. If found, returns first match found as object else none
            - this is where https://pythex.org/ is useful, it helps us extract the match
            - syntax without re.compile: re.search(r'some_regex', string)
        - search.group(group_number?)
            - returns matched string within the match object returned from search()
            - alternative to retrieiving with group_number is syntax key-value pair: ?P<some_label>some_regex (see example C)
        - search.groups()
            - returns group matched as tuple of multiple groups
        - pattern.fullmatch(some_string) - return match object, works similarly to having ^ and $ to indiciate mandatory start/end without these characters in pattern (see example A)
        - pattern.findall(some_string) - scan through string with pattern for a match. If found, returns all matches found as list else none  (see example B)
        - pattern.sub(replacement_string, some_string) - replaces match found with replacement_string (see example D)

    Compilation flags
        - use multiple flags with or pipe operator
        - re.VERBOSE or re.X - allows breaking of regex pattern into multiple lines in py
        - re.IGNORECASE or re.I - ignores case in regex pattern that way we can don't have to do [A-Za-z] and just [a-z]

"""

import re

# example A: create function that validates if a string argument is a phone number and a boolean argument to use fullmatch or search
def validate_phone(string, use_fullmatch=False):
    try:
        if use_fullmatch:
            pattern = re.compile(r'\d{3}(\s|-?)\d{3}(\s|-?)\d{4}')
            match = pattern.fullmatch(string)
            return match.group()
        return re.search(r'^\d{3}(\s|-?)\d{3}(\s|-?)\d{4}$', string).group()
    except AttributeError:
        return None
    
print(validate_phone('303 333-3333', True))
print(validate_phone('303 333-3333asdasdasd', True))
print(validate_phone('303 333-3333'))
print(validate_phone('asdsad303 333-3333'))

# example B: create parse_bytes function that accepts a string and returns a list of the binary bytes
def parse_bytes(string):
    return re.findall(r'\b[01]{8}\b', string)

print(parse_bytes("11010101 101 323"))
print(parse_bytes("my data is: 10101010 11100010"))
print(parse_bytes("asdsa"))

# example C: create parse_date function that accepts a DMY date string and returns a dict of the date and date must be exact match
def parse_date(string):
    match = re.fullmatch(r'(?P<d>\d\d)[,./](?P<m>\d\d)[,./](?P<y>\d{4})', string)
    if match:
        return {
            'd': match.group('d'),
            'm': match.group('m'),
            'y': match.group('y'),
        }
    return None

print(parse_date('01/22/1999'))
print(parse_date('12.11.2003dsadsad'))
print(parse_date('12.11.2003'))

# example D: create rename_and_sort_books function that accepts list of books and returns a sorted list by year
def rename_and_sort_books(books):
    pattern = re.compile(r"""
        (^[a-z* ]+)
        \s
        \((\d{4})\)
    """, re.X | re.I)
    books = [pattern.sub('\g<2> \g<1>', book) for book in books] # g<1> references the group sub's find, allowing reuse of existing matched groups
    return books

print(rename_and_sort_books([
    "Significant Others (1987)",
    "Tales of the City (1978)",
    "The Days of Anna Madrigal (2014)",
    "Mary Ann in Autumn (2010)",
    "Further Tales of the City (1982)",
    "Babycakes (1984)",
    "More Tales of the City (1980)",
    "Sure of You (1989)",
    "Michael Tolliver Lives (2007)"
]))
