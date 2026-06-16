import random
word_list = ["any", "word", "possibly", "available"]

chosen = random.choice(word_list)

print(chosen)

placeholder = ""
for position in range(len(chosen)):
    placeholder += '_'

print(placeholder)

g_letter = input("Guess a letter: ").lower()

display = ''

for letter in chosen:
    if letter == g_letter:
        display += letter
    else:
        display += '_'

print(display)