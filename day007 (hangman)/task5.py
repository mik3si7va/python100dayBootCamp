import random
import art_module as am
import words_module as wm

print(am.logo)

lives = 6

chosen = random.choice(wm.words)

print(chosen)

placeholder = ""
for position in range(len(chosen)):
    placeholder += '_'

print(placeholder)

display = placeholder
guessed = []
found =[]

while '_' in display:
    print(f"{am.stages[-(lives+1)]}")
    if lives == 0:
        print("GAME OVER! U LOOOOSE 😜!")
        print(f"BTW, the word was: {chosen}")
        break
   
    g_letter = input("Guess a letter: ").lower()
    if not g_letter in guessed:
        guessed.append(g_letter)
        display = ''
        if not g_letter in chosen:
            print(f"The letter '{g_letter}' is not part of the word ... a life was lost on that one..")
            lives -= 1
        for i in range(len(chosen)):
            if chosen[i] == g_letter:
                display += chosen[i]
                found.append(i)
            elif i in found:
                display += chosen[i]
            else:
                display += '_'
    else:
        print(f"you alredy said the letter '{g_letter}'... that one doesn't count..")
    print(f"-------------- {lives} lives left --------------")
    print(f"current progress: {display}")