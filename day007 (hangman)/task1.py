import random
word_list = ["any", "word", "possibly", "available"]

chosen = random.choice(word_list)

print(chosen)

g_letter = input("Guess a letter: ").lower()

for letter in chosen:
    if letter == g_letter:
        print(True)
    else:
        print(False)
