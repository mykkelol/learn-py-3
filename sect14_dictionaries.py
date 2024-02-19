""" 
Dictionary
    - dict can also be created using the dict function
    - syntax: dict(key = 'value')
        - example: my_dict = dict(long='phoking',small='side')
        - example: my_dict = dict(['str1', 'str2])

Dictionary Comprehension
    - dict comphrension is similar to list comprehension wherein it's syntax that creates a copy of a dict with manipulated/tweaked values
    - syntax: {key:value for record in records}
        - example: {key: value ** 2 for key,value in records.items()}
        - example: {num: num ** 2 for num in range(6)}

Common Dict functions
    - .values() - access all values in dict (similar to JS for key in obj { obj[key] })
    - .keys() - access all keys in dict (similar to JS object.keys(obj))
    - .items() - access all keys and valuesm
        - example: for key, value in my_dict.items()

Common Dict methods
    - .get() - returns value of a key if key exist and returns None or a default otherwise without erroring
    - .clear() - empty dict entirely
    - .copy() - creates a dict copy
    - .fromkeys(iteratable, values) - creates key-value pairs with comma seperator
        - example: {}.fromkeys('n', [1,3,3,7]) = {'n':[1,3,3,7]}
        - can be useful to create dict with default values
        - example: {}.fromkeys(['first','last','manager','age'], None) returns a dict with all keys set to None
    - .pop(key) - unlike list, dict requires a key to pop and will error otherwise of if key doesn't exist. Once popped, it'll return the value
    - .popitem() - pops a random kv pair return the kv pair popped
    - .update(dict) - takes a kv pair or dict to update an existing dict. It will only update a dict with pairs but never remove anything

"""

# create total_donations that is the sum of all donations
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
total_donations = sum(donations.values())

# set initial state value of 0 for all game properties
game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"] 
initial_game_state = {}.fromkeys(game_properties, 0)

# create a spotify playlist
playlist = {
    'title': 'favorites', 
    'author': 'mykkelol', 
    'songs': [
        {
            'title': 'Malibu',
            'artists': ['Miley', 'DJ Khaled'],
            'duration': 2.5,
        },
        {
            'title': '22',
            'artists': ['Tay Tay', 'Mahomes'],
            'duration': 3,
        }
    ]
}

total_length = 0
for song in playlist['songs']:
    total_length += song['duration']
playlist.update({'total_duration': total_length})

# given str1 and str2, create a dict with str1 as key and str2 as corresponding values
str1 = 'ABC'
str2 = '123'
my_dict = {str1[i]: str2[i] for i in range(len(str1))}

# given list of nums, create a dict where nums are keys and values to indicate if num is odd or even
nums = range(1,6)
my_dict = {n: 'even' if n % 2 == 0 else 'odd' for n in nums}

# given dict of instructor, update key "color" and its value to uppercase
my_dict = {'name': 'Blue', 'city': 'San Francisco', 'color': 'purple'}
my_dict = {(k.upper() if k == 'color' else k): (v.upper() if k == 'color' else v) for k,v in my_dict.items()}

# given two lists, create dict with list1 as keys and list2 as corresponding values without using zip()
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
my_dict = {list1[i]:list2[i] for i in range(len(list1))}

# given person, a list of lists with two indices of key and value, convert into a single dict
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]  
my_dict = dict(person)
my_dict = {k:v for k,v in person}

# create a vowel dict with each vowel as key and value default to 0
my_dict = {}.fromkeys('aeiou',0)

# create a dict of all ASCII wherein the key is the number of ASCII and value is the alphabet. only need capital A-Z
my_dict = {n:chr(n) for n in range(65,91)}