from pyfiglet import Figlet
from termcolor import colored
from random import randint
import requests

banner = Figlet().renderText('PappyJoke9000!')
banner = colored(banner, color='blue', on_color='on_green')
print(banner)

topic = input('Let me tell you a joke! Give me a topic: ')
url = 'https://icanhazdadjoke.com/search'

while True:
    if topic == 'q':
        break
    else:
        response = requests.get(
            url, 
            headers={'Accept': 'application/json'},
            params={'term': topic}
        )

        if response.status_code == 200:
            data = response.json()
            jokes = data['results']
            total_jokes = data['total_jokes']

            if total_jokes > 1:
                i = randint(0, total_jokes - 1)
                print(jokes[i]['joke'])
                break
            elif total_jokes == 1:
                print(jokes[0]['joke'])
                break
            else:
                topic = input(f"Sorry. I don't have a joke for that {topic}. Try again: ")
        else:
            print("Whoops. I'm cold feet and can't think of any jokes.")
            break
        

