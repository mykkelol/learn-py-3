""" 
List Comphrehension
    - list shorthand syntax  that creates list copies that are tweaked and manipulated
    - syntax: [record manipulation expressopn for record in records]
        - example: [num * 2 for num in range(1,6)]
    - syntax with if condition: [record manipulation expressopn for record in records if expression] 
        - example: [num * 2 for num in range(1,6) if num % 2 == 0]
    - syntax with else condition: [IF record manipulation expressopn if expression else record manipulation expression for record in records]
        - example: [num * 2 if num % 2 == 0 else num / 2 for num in range(1,6)]

"""

# return list of all names
names = ["Elie", "Tim", "Matt"]
[name[0] for name in names]

# return all even numbers between 1 to 6
numbers = [n for n in range(1,7) if n % 2 == 0]

# find intersection between two lists
list_a = [1,2,3,4]
list_b = [3,4,5,6]
[num for num in list_a if num in list_b]

# reverse and lowercase all names
names = ["Elie", "Tim", "Matt"]
[name[::-1].lower() for name in names]

# numbers between 1 and 100, return list with all numbers that are divisible by 12
[n for n in range(1, 101) if n % 12 == 0]

# convert string "amazing to list containing all letters but not vowels
word = 'amazing'
[char for char in word if char not in 'aeiou']

# in list of locations' coordindates, print list of all coordinates
locations = [[10.423, 9.123], [37.212, -14.092], [21.367, 32.572]]
[[print(coord) for coord in loc] for loc in locations]

# return a 3x3 matrix of stars
[['*' * 3 for j in range(1,4)] for i in range(1,10)]

# return nested lists of [1,2,3] 3 times
[[n for n in range(3)] for g in range(3)]