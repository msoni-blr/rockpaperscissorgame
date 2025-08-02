import random

ROCK = 'r'
PAPER = 'p'
SCISSOR = 's'

# game_selection = ['r', 'p', 's']
emojis = {ROCK: '🪨', PAPER: '📃', SCISSOR: '✄'}
game_selection = tuple(emojis.keys())

def play_game():
    while True:
        computer_choice = random.choice(game_selection)
        user_choice = get_user_choice()
        display_selection(user_choice, computer_choice)
        result(user_choice, computer_choice)
        playmore = input("Press any key to continue, or n to exit: ").lower()
        if playmore == 'n':
            print("Thanks for playing!")
            break

def get_user_choice():
    while True:
        user_choice = input(f"Rock, paper, scissors? ({ROCK}/{PAPER}/{SCISSOR}): ").lower()
        if user_choice in game_selection:
            return user_choice
        else:
            print("Invalid choice!")
            continue

def display_selection(user_choice, computer_choice):
    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")

def result(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a tie")
    elif ((user_choice == ROCK and computer_choice == SCISSOR) 
        or (user_choice == SCISSOR and computer_choice == PAPER) 
        or (user_choice == PAPER and computer_choice == ROCK)):
        print("You win")
    else:
        print("You lose")
    
play_game()

# if __name__ == "__main__":
#     play_game()