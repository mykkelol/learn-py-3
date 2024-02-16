""" 

range(start, end, step)
    - range has three args
        - start is default to 0 if not provided e.g. (8) counts from 0..7
        - end is exclusive e.g. (1, 8) will count to 7
        - step means how many to skip e.g. (0, 8, 2) counts 0, 2, 4...
        - step also means way to count up/down with +/- e.g. (7, 1, -1) counts 7, 6, 5.. 2
    - when printing range, it doesn't print the count and we'd need to iterate
    - e.g. nums = range(x,y) and print(nums) will equal range(x, y)
    - list(nums) will iterate and print each num

"""


""" 
times = input('How many times do I have to tell you? ')
times = int(times)

for time in range(times):
    print(f'time {time}: CLEAN YOUR ROOM!!!')
"""

""" 
for n in range(1, 21):
    if n == 4 or n == 13:
        state = 'UNLUCKY!'
    elif n % 2 == 0:
        state = 'even'
    else:
        state = 'odd'
    print(f'{n} is {state}')
"""

""" 
pw = input('What is the password? ')
stored_pw = 'strawberry chocolate'
tries = 1
max_tries = 5

while pw != stored_pw:
    if tries == max_tries:
        print('You are DONE! Too many tries.')
        break
    tries += 1
    pw = input('What is the password? ')
print('You are IN!')
"""

""" 
smile = '\U0001f600'
smilies = 1
while smilies < 20:
    print(smile * smilies)
    smilies += 2

for army in range(3):
    for smiley in range(10):
        print(smile * smiley)
"""

msg = input('Hey are you doing? ')
msg.lower()

while msg != 'stop copying me':
    msg = input(f'{msg}\n')
print('UGH FINE YOU WIN')