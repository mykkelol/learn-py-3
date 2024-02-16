from random import choice

winning_score = 3
player_wins = 0
bot_wins = 0
choices = ['rock', 'paper', 'scissors']
player = 'Player'
bot = 'NotSmarterChild'
result = None

while player_wins < winning_score and bot_wins < winning_score:
    print(f'{player} Score: {player_wins} {bot} Score: {bot_wins}')
    print('...rock...')
    print('...rock...')
    print('...paper...')
    print('...scissors...')
    player_choice = input("(enter Player's choice): ").lower()
    bot_choice = choice(choices)

    if player_choice in ['q', 'quit']:
        print('What a loseeeeeer!')
        break
    if player_choice in choices:
        if player_choice == bot_choice:
            result = 'Draw'
        elif player_choice == 'rock' and bot_choice == 'scissors':
            result = f'{player} wins'
            player_wins += 1
        elif player_choice == 'paper' and bot_choice == 'rock':
            result = f'{player} wins'
            player_wins += 1
        elif player_choice == 'scissors' and bot_choice == 'paper':
            result = f'{player} wins'
            player_wins += 1
        else:
            result = f'{bot} wins'
            bot_wins += 1
    else:
        raise f'{player_choice} is not a valid option'

    print('SHOOT!')
    print(f'{player} chose {player_choice}')
    print(f'{bot} chose {bot_choice}')
    print(f'{result}!')
    
print(f'FINAL SCORES... {player} Score: {player_wins} {bot} Score: {bot_wins}')