import random

guess_num = r"""
  ___ _   _ ___ ___ ___
 / __| | | | __/ __/ __|
| (_ | |_| | _|\__ \__ \
 \___|\___/|___|___/___/

        .. THE ..
     _  _ _   _ __  __
    | \| | | | |  \/  |
    | .` | |_| | |\/| |  __
    |_|\_|\___/|_|  |_| |__|

    THE NUMBER GUESSING GAME.. 📉  #️⃣   📈
     
"""

u_win = r"""
     _   _   __        _____ _   _    __
    | | | |  \ \      / /_ _| \ | |  |  |
    | | | |   \ \ /\ / / | ||  \| |  |  |
    | |_| |    \ V  V /  | || |\  |  |==|
     \___/      \_/\_/  |___|_| \_|  |__|
"""

u_lost = r"""
     _   _    _       ___  ____ _____    __
    | | | |  | |     / _ \/ ___|_   _|  |  |
    | | | |  | |    | | | \___ \ | |    |  |
    | |_| |  | |___ | |_| |___) || |    |==|
     \___/   |_____| \___/|____/ |_|    |__|
"""

first_time = True

while True:
    if not first_time:
        if input("Press Enter to play again or type 'exit' to quit: ").lower() == "exit":
            print("Thanks for playing! Goodbye! 👋")
            break
    if first_time:
        print(guess_num)
        first_time = False
    
    print("\nWelcome to the Number Guessing Game! 🎉\n")

    difficulty = input("do you want it EASY or HARD? (type 'easy' or 'hard') (type 'exit' to exit) ").lower()
    attempts = 0
    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    elif difficulty == "exit":
        break
    else:
        print("Invalid input. Please type 'easy' or 'hard'.")
        continue

    print("\nI'm thinking of a number between 1 and 100. Can you guess it? 🤔")
    number = random.randint(1, 100)
    #print(f"Pssst, the correct answer is {number}")  # For testing purposes
    print(f"\nYou have {attempts} attempts to guess the number. Good luck! 🍀\n")
    while attempts > 0:
        guess = int(input("Make a guess:\n>>> "))
        
        if guess < number:
            print("Too low! 📉")
        elif guess > number:
            print("Too high! 📈")
        else:
            print(u_win)
            print(f"Congratulations! You've guessed the number {number}! 🎉")
            break
        
        attempts -= 1
        print(f"\nYou have {attempts} attempts remaining. ⏳\n")
        if attempts == 0:
            print(u_lost)
            print(f"Sorry, you've run out of attempts. The number was {number}. 😢")