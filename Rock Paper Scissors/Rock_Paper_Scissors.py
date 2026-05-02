from random import choice
options = ('rock','paper','scissors')
print("================ Rules ================")
print("1. Rock crushes Scissors")
print("2. Scissors cuts Paper")
print("3. Paper covers Rock")
print("=======================================\n")
user_score = 0
computer_score = 0
#rules
def check(user_choice,computer_choice):
    global user_score, computer_score
    if user_choice == computer_choice:
        print('tie')
    elif user_choice =='rock' and computer_choice =='scissors':
        print("You win! Rock beats Scissors.")
        user_score += 1
    elif user_choice =='scissors' and computer_choice =='paper':
        print("You win! scissors beats paper.")
        user_score += 1
    elif user_choice =='paper' and computer_choice =='rock':
        print("You win! paper beats rock.")
        user_score += 1
    else:
        print(f'You loosed! {computer_choice} beats {user_choice}  ')
        computer_score += 1

while True:
    user_choice = input('choose rock/paper/scissors or "end" to end the game: ').lower()
    if user_choice == 'end':
        print("Thanks for playing!")
        break
    
    if user_choice not in options:
        print("Invalid choice, try again.")
        continue

    computer_choice = choice(options)
    print(f'You choosed {user_choice},Computer choosed {computer_choice}')
    check(user_choice,computer_choice)
    print(f'YOUR score is {user_score} and computer score is {computer_score}\n')

