age = input('How old is Spongebob?')
if age:
    age = int(age)
    if age >= 21:
        print('Drink away because this is Cantina of Krusty Krab and you are 21!')
    elif age >= 18:
        print('You can enter Krusty Krab Cantina but cannot drink!')
    else:
        print('Little one, you need to visit Krusty Krab mid edition.')
else:
    print("Enter an age or I'll call Plankton!")