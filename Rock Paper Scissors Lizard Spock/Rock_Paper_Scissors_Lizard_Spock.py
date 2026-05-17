'''Rules
Scissors cuts Paper
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock
Rock crushes Scissors'''

from random import choice
print("================ Rules ================")
print("1.Scissors cuts Paper ")
print("2.Paper covers Rock ")
print("3.Rock crushes Lizard ")
print("4.Lizard poisons Spock ")
print("5.Spock smashes Scissors ")
print("6.Scissors decapitates Lizard ")
print("7.Lizard eats Paper ")
print("8.Paper disproves Spock ")
print("9.Spock vaporizes Rock ")
print("10.Rock crushes Scissors")
print("=======================================\n")

rules = {
    "scissors": ["paper", "lizard"],
    "paper": ["rock", "spock"],
    "rock": ["lizard", "scissors"],
    "lizard": ["spock", "paper"],
    "spock": ["scissors", "rock"]
}
options =('scissors','paper','rock','lizard','spock')
user_score = 0
computer_score = 0
def referee(player,computer):
    global user_score, computer_score
    if player == computer:
        print('tie')
    elif computer in rules[player]:
        print(f"You win! {player} beats {computer}.")
        user_score +=1

    else:
        print(f'You lost! {computer} beats {player}')
        computer_score += 1         
  

while True:
    player_choice = input('choose rock/paper/scissors/spock/lizard or "end" to end the game: ').lower()
    if player_choice == 'end':
        print("Thanks for playing!")
        break
    
    if player_choice not in options:
        print("Invalid choice, try again.")
        continue
    computer_choice = choice(options)
    print(f'You choosed {player_choice},Computer choosed {computer_choice}')
    referee(player_choice,computer_choice)
    print(f'YOUR score is {user_score} and computer score is {computer_score}\n')



# you can make it more fun ;> just give it your own touch


