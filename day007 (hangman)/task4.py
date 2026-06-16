import random
word_list = ["any", "word", "possibly", "available"]

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
lives = 6

chosen = random.choice(word_list)

print(chosen)

placeholder = ""
for position in range(len(chosen)):
    placeholder += '_'

print(placeholder)

display = placeholder
found =[]

while '_' in display:
    print(f"{hangman_stages[-(lives+1)]}")
    if lives == 0:
        print("GAME OVER! U LOOOOSE 😜!")
        print(f"BTW, the word was: {chosen}")
        break
   
    g_letter = input("Guess a letter: ").lower()
    
    display = ''
    if not g_letter in chosen:
        lives -= 1
    for i in range(len(chosen)):
        if chosen[i] == g_letter:
            display += chosen[i]
            found.append(i)
        elif i in found:
            display += chosen[i]
        else:
            display += '_'

    print(f"current progress: {display}")