import random

def play_rps(user_choice, user_name):
    vals = ['stone', 'paper', 'scissor']
    ind = random.randint(0, len(vals) - 1)
    cpu = str(vals[ind])
    
    user_choice = user_choice.lower()
    
    if user_choice == cpu:
        print("IT'S A DRAWWWW!!!")
    elif user_choice == 'stone' and cpu == 'paper':
        print(f"CPU wins :-( ! CPU's choice was {cpu}...")
    elif user_choice == 'stone' and cpu == 'scissor':
        print(f"{user_name} wins :-D ! CPU's choice was {cpu}...")
    elif user_choice == 'paper' and cpu == 'scissor':
        print(f"CPU wins :-( ! CPU's choice was {cpu}...")
    elif user_choice == 'paper' and cpu == 'stone':
        print(f"{user_name} wins :-D ! CPU's choice was {cpu}...")
    elif user_choice == 'scissor' and cpu == 'stone':
        print(f"CPU wins :-( ! CPU's choice was {cpu}...")
    elif user_choice == 'scissor' and cpu == 'paper':
        print(f"{user_name} wins :-D ! CPU's choice was {cpu}...")
    else:
        print("Invalid input!")

def start_game():
    print("Welcome to Stone, Paper, Scissor!")
    choice = input('Enter your choice (stone/paper/scissor): ')
    name = input("What's your name mate? ")
    play_rps(choice, name)

if __name__ == "__main__":
    start_game()
