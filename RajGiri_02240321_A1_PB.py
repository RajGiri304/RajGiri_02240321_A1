import random

def play_guessing_game():
    """Number guessing game where the user tries to guess a randomly chosen number."""
    print("\nGuess the Number (1-100)")
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Higher!")
            elif guess > secret_number:
                print("Lower!")
            else:
                print(f"Correct! You guessed it in {attempts} tries!")
                break
        except ValueError:
            print("Please enter a valid number.")

def play_rps():
    """Rock-Paper-Scissors game where the user plays against the computer."""
    print("\nRock-Paper-Scissors")
    choices = {'1': 'rock', '2': 'paper', '3': 'scissors'}
    win_conditions = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }

    print("Choose: 1. Rock  2. Paper  3. Scissors")
    user_choice = choices.get(input("Your choice (1-3): "), 'invalid')

    if user_choice == 'invalid':
        print("Invalid choice. Please enter 1-3.")
        return

    computer_choice = random.choice(list(choices.values()))
    print(f"You chose {user_choice}, Computer chose {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif win_conditions[user_choice] == computer_choice:
        print("You win!")
    else:
        print("Computer wins!")

def show_menu():
    """Displays the menu and lets the user select a game."""
    menu_options = {
        '1': ("Guess Number Game", play_guessing_game),
        '2': ("Rock-Paper-Scissors", play_rps)
    }

    while True:
        print("\nMENU")
        for key, (label, _) in menu_options.items():
            print(f"{key}. {label}")
        print("3. Exit")

        choice = input("\nEnter option: ")

        if choice == '3':
            print("Thanks for playing!")
            break
        elif choice in menu_options:
            menu_options[choice][1]()  # Calls the selected function
        else:
            print("Invalid option! Please choose 1-3.")

if __name__ == "__main__":
    print("Game Collection")
    show_menu()
