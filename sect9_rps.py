from random import choice

choices = ['rock', 'paper', 'scissors']
player = 'Player'
bot = 'NotSmarterChild'
result = None

print('...rock...')
print('...paper...')
print('...scissors...')
player_choice = input("(enter Player's choice): ").lower()
print('**** Thinking ****\n' * 20)
bot_choice = choice(choices)

if (player_choice in choices):
    if player_choice == bot_choice:
        result = 'Draw'
    elif player_choice == 'rock' and bot_choice == 'scissors':
        result = f'{player} wins'
    elif player_choice == 'paper' and bot_choice == 'rock':
        result = f'{player} wins'
    elif player_choice == 'scissors' and bot_choice == 'paper':
        result = f'{player} wins'
    else:
        result = f'{bot} wins'
else:
    raise f'{player_choice} is not a valid option'

print('SHOOT!')
print(f'{player} chose {player_choice}')
print(f'{bot} chose {bot_choice}')
print(f'{result}!')