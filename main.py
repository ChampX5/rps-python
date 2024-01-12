import random

def convert(integer):
    match integer:
        case '1':
            return 'Rock'

        case '2':
            return 'Paper'
        
        case '3':
            return 'Scissors'

def check_win(user_choice, computer_choice):
    if (user_choice == computer_choice):
        return 'draw'
    
    winner = "TBD"

    if user_choice == 'Rock':
        if computer_choice == 'Paper':
            winner = 'computer' # player loses
        if computer_choice == 'Scissors':
            winner = 'player' # player wins

    if user_choice == 'Paper':
        if computer_choice == 'Rock':
            winner = 'player' # player wins
        if computer_choice == 'Scissors':
            winner = 'computer' # player loses

    if user_choice == 'Scissors':
        if computer_choice == 'Rock':
            winner = 'computer' # player loses
        if computer_choice == 'Paper':
            winner = 'player' # player wins
    
    return winner

while True:
    print('You can enter (Q) to quit.')
    user_input = input("Enter:\n(1): Rock\n(2): Paper\n(3): Scissors\n\nYOUR CHOICE: ")

    if user_input.lower() not in ['q', '1', '2', '3']:
        print('Invalid input. Please try again.')
        continue

    if user_input.lower() == 'q':
        print('Thanks for playing! See you soon.')
        break

    # LOGIC
    computer_input = str(random.randint(1, 3))

    user_choice = convert(user_input)
    computer_choice = convert(computer_input)

    winner = check_win(user_choice, computer_choice)

    if winner == 'draw':
        print(f'The game was a draw! Both picked {user_choice.upper()}.')
    
    elif winner == 'computer':
        print(f'The computer has won! It chose {computer_choice.upper()} while you chose {user_choice.upper()}.')
    
    elif winner == 'player':
        print(f'You have won! You chose {user_choice.upper()} while the computer chose {computer_choice.upper()}.')
