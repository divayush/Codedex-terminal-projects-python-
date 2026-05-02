from random import randint

while True:
    ask = input("Type roll to roll the dice and stop to end: ").lower()

    if ask == 'roll':
        roll = randint(1, 6)
        print("You rolled:", roll)

    elif ask == 'stop':
        print("Thanks for playing!")
        break

    else:
        print("Wrong input, please type roll/stop")