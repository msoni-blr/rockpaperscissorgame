import random

game_selection = ['r', 'p', 's']
emojis = {'r': '🪨', 'p': '📃', 's': '✄'}

def playgame():
    while True:
        computer_chose = random.choice(game_selection)
        print(computer_chose)
        command = input("Rock, paper, scissors? (r/p/s): ").lower()
        if command not in game_selection:
            print("Invalid choice!")
            continue
        print(f"You chose {emojis[command]}")
        print(f"Computer chose {emojis[computer_chose]}")
        print(result(command, computer_chose))
        playmore = input("Continue? (y/n): ").lower()
        if playmore == 'n':
            break

def result(command, computer_chose):
    if command == computer_chose:
        return "It's a tie"
    elif ((command == 'r' and computer_chose == 's') 
        or (command == 's' and computer_chose == 'p') 
        or (command == 'p' and computer_chose == 'r')):
        return "You win"
    else:
        return "You lose"
    
if __name__ == "__main__":
    playgame()