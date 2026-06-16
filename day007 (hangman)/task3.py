import random
word_list = ["any", "word", "possibly", "available"]

chosen = random.choice(word_list)

print(chosen)

placeholder = ""
for position in range(len(chosen)):
    placeholder += '_'

print(placeholder)

display = placeholder
found =[]

while '_' in display:
    g_letter = input("Guess a letter: ").lower()
    
    display = ''
    for i in range(len(chosen)):
        if chosen[i] == g_letter:
            display += chosen[i]
            found.append(i)
        elif i in found:
            display += chosen[i]
        else:
            display += '_'

    print(display)