import random


print("Welcome to Rock, Paper, Scissors!")

rock = (r"""

ROCK..        
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

        """)

paper = (r"""
    
PAPER..    
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

        """)

scissors = (r"""
            
SCISSORS..  
    _______
---'    ____)____
           ______)
        __________)
      (____)
---.__(___)

            """)
continue_game = True
pc_score = 0
player_score = 0

while continue_game:
    choice = input("Choose your Weapon! Type R for Rock, P for Paper or S for Scissors.\n>>> ")

    pc = random.choice(["R", "P", "S"])
    
    choice = choice.upper()

    printer_choice = {
        "R": rock,
        "P": paper,
        "S": scissors
    }

    print(f"You chose:{printer_choice[choice]}\nand the computer chose {printer_choice[pc]}.")

    if choice == pc:
        print("It's a draw!")
    elif (choice == "R" and pc == "S") or (choice == "P" and pc == "R") or (choice == "S" and pc == "P"):
        print("You win!")
        player_score += 1
    else:
        print("You lose!")
        pc_score += 1

    print(f"Score - You: {player_score}, Computer: {pc_score}")
    if player_score == 3:
        print("Congratulations! You won the game!")
        break
    elif pc_score == 3:
        print("Sorry! The computer won the game!") 
        break
    print("That's the GAME! Would you like to play again? Type Y for Yes or N for No.")
    play_again = input(">>> ").upper()
    if play_again == "N":
        continue_game = False

print("Thanks for playing! Goodbye!")