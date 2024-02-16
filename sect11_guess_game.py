from random import randint

num = randint(1, 10)
guess = None

while True:
    guess = input('Pick a number from 1 to 10: ')
    guess = int(guess)
    if guess > num:
        print('Too high!')
    elif guess < num:
        print('Too low!')
    else:
        print('YOU WON!')
        play_again = input('Would you like to play again? (Y/N): ')
        if play_again.lower() == 'y':
            num = randint(1, 10)
            guess = None
        else:
            print('thanks for palying come again!')
            break
