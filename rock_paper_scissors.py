from random import randint

user_wins = 0
computer_wins = 0
options = ['rock', 'paper', 'scissors']

while True:
    user_input = input('Type Rock/Scissors/Paper or Q to exit: ').lower()
    if user_input == 'q':
        break
    
    if user_input not in options:
        continue

    # 0 = rock, 1 = paper, 2 = scissors
    computer_pick = options[randint(0, 2)]
    print('computer picked %s.' % computer_pick)

    if user_input == computer_pick:
        print('You have selected both %s' % user_input.capitalize())

    elif user_input == 'rock' and computer_pick == 'scissors':
        print('You won')
        user_wins += 1

    elif user_input == 'paper' and computer_pick == 'rock':
        print('You won')
        user_wins += 1

    elif user_input == 'scissors' and computer_pick == 'paper':
        print('You won')
        user_wins += 1

    else:
        print('You lost!')
        computer_wins += 1

print(f'You won {user_wins} times.')
print(f'The computer won {computer_wins} times.')