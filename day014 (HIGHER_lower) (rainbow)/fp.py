import random

import art_mod
import data_mod


art_mod.rainbow_print(art_mod.banner)

person1 = person2 = ()
keep_at_it = True
while keep_at_it:    
    score = 0
    while True:
        if score == 0:
            person1 = person2 = random.choice(data_mod.famous_people)
        while True:
            if person1 == person2 or person2 == ():
                person2 = random.choice(data_mod.famous_people)
            if person1 != person2:
                break
        print("\nWho has more followers???\n")
             
        display_score = ' - '.join(["⭐" for _ in range(score)])
        
        art_mod.print_blue_text("-----------------------------")
        art_mod.print_green_text('1: ' + person1[0])
        art_mod.rainbow_print(art_mod.vs_tag)
        art_mod.print_red_text('2: ' + person2[0])
        art_mod.print_blue_text("-----------------------------")
        
        if display_score != '':
            art_mod.print_blue_text(f"{display_score}\n")
            
        choice = input("\n1 or 2?\n>>> ")
        if choice == "1":
            if person1[1] > person2[1]:
                art_mod.print_green_text("You are correct! 🎉")
                score += 1
                person1 = person2
                continue
            else:
                art_mod.print_red_text("You are wrong! 😢")
                break
        elif choice == "2":
            if person2[1] > person1[1]:
                art_mod.print_green_text("You are correct! 🎉")
                score += 1
                person1 = person2
                continue
            else:
                art_mod.print_red_text("You are wrong! 😢")
                break
        else:
            art_mod.print_red_text("Invalid choice! Please choose 1 or 2.")
            continue
            
            
    art_mod.print_blue_text(f"\nYour final score is: {score}")

    keep_at_it = input("wanna keep playing? (y for yes)\n>>> ").lower() == "y" and True or False
