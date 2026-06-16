import random

hangman_stages = [
r"""
 +---+
 |   |
     |
     |
     |
     |
=========
""",
r"""
 +---+
 |   |
 O   |
     |
     |
     |
=========
""",
r"""
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
""",
r"""
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
""",
r"""
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========
""",
r"""
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========
""",
r"""
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========
"""
]

banner = (r"""
          
██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
            the game..
          
          """)

easy_words = [
    "apple",
    "house",
    "river",
    "chair",
    "table",
    "tiger",
    "pizza",
    "cloud",
    "beach",
    "train",
    "plant",
    "bread",
    "water",
    "horse",
    "music",
    "phone",
    "light",
    "mouse",
    "smile",
    "dream",
    "stone"
]

medium_words = [
    "python",
    "castle",
    "rocket",
    "planet",
    "silver",
    "window",
    "forest",
    "pirate",
    "dragon",
    "button",
    "guitar",
    "garden",
    "laptop",
    "bridge",
    "puzzle",
    "thunder",
    "journey",
    "captain",
    "monster",
    "treasure",
    "library"
]

hard_words = [
    "counterproductive",
    "misinterpretation",
    "institutionalized",
    "characteristically",
    "intercontinental",
    "electromagnetic",
    "extraordinary",
    "unpredictability",
    "incomprehensible",
    "disproportionate",
    "unconditionality",
    "multidimensional",
    "hyperconnectivity",
    "interdependency",
    "transformation",
    "individualistic",
    "miscommunication",
    "overcomplicated",
    "responsibility",
    "determination",
    "underestimated"
]

print(banner)

print ("Welcome to Hangman! pick a difficulty level and have a good game...")
print ("1. Easy")
print ("2. Medium")
print ("3. Hard")
level = input("Enter your choice (1/2/3):\n>>> ")

word_list = []

if level == "1":
    word_list = easy_words
    print("You picked EASY level... good luck!")
elif level == "2":
    word_list = medium_words
    print("You picked MEDIUM level... good luck!")
elif level == "3":
    word_list = hard_words
    print("You picked HARD level... good luck!")
else:
    print("Invalid choice. Defaulting to HARD AS FUCK level... good luck!")
    word_list = hard_words
    
word_pick = random.choice(word_list)
word_size = len(word_pick)

display = ["_"] * len(word_pick)

print(f"{hangman_stages[0]}")

current_stage = 0
print(f"Guess this word with {word_size} letters! : {' '.join(display)}")
guesses = []
while current_stage < len(hangman_stages) - 1:
    lives = len(hangman_stages) - 1 - current_stage
    print (f"\n-------------- {lives} {lives == 1 and 'life' or 'lives'} left --------------\n")
    print(f"Letters tried so far: {' | '.join(guesses)}")
    letter_guess = input("Guess a letter:\n>>> ").lower()
    if letter_guess.upper() in guesses:
        print("You've already tried that letter!")
        continue
       
    guesses.append(letter_guess.upper())

    if letter_guess in word_pick:
        counter = 0
        for i in range(len(word_pick)):
            if word_pick[i] == letter_guess:
                display[i] = letter_guess.upper()
                counter +=1
        print(f"Good guess! You found {counter} {counter == 1 and 'letter' or 'letters'}.")
        if "_" not in display:
            print("Congratulations! You correctly guessed the word!")
            print (f"It was: {word_pick.upper()}!")
            print("That's the GAME! 🥳")
            break
    else:
        print("Letter not in word!")
        current_stage += 1

    print(f"{hangman_stages[current_stage]}")
    print(f"Current progress: {' '.join(display)}")

if current_stage == len(hangman_stages) - 1:
    print(f"Game Over! Shame on you! 🤣 The word was: {word_pick.upper()} 😜")