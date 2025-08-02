import random

game_selection = ['r', 'p', 's']
emojis = {'r': '🪨', 'p': '📃', 's': '✄'}

def play_game():
    while True:
        computer_choice = random.choice(game_selection)
        user_choice = get_user_choice()
        display_selection(user_choice, computer_choice)
        result(user_choice, computer_choice)
        playmore = input("Continue? (y/n): ").lower()
        if playmore == 'n':
            break

def get_user_choice():
    while True:
        user_choice = input("Rock, paper, scissors? (r/p/s): ").lower()
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
    elif ((user_choice == 'r' and computer_choice == 's') 
        or (user_choice == 's' and computer_choice == 'p') 
        or (user_choice == 'p' and computer_choice == 'r')):
        print("You win")
    else:
        print("You lose")
    
play_game()

# if __name__ == "__main__":
#     play_game()