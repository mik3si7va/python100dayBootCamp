print(r"""
                              _.--.
                         _.-'_:-'||
                     _.-'_.-::::'||
                _.-:'_.-::::::'  ||
              .'`-.-:::::::'     ||
             /.'`;|:::::::'      ||_
            ||   ||::::::'     _.;._'-._
            ||   ||:::::'  _.-!oo @.!-._'-.
            \'.  ||:::::.-!()oo @!()@.-'_.|
             '.'-;|:.-'.&$@.& ()$%-'o.'\U||
               `>'-.!@%()@'@_%-'_.-o _.|'||
                ||-._'-.@.-'_.-' _.-o  |'||
                ||=[ '-._.-\U/.-'    o |'||
                || '-.]=|| |'|      o  |'||
                ||      || |'|        _| ';
                ||      || |'|    _.-'_.-'
                |'-._   || |'|_.-'_.-'
                 '-._'-.|| |' `_.-'
                      '-.||_/.-'
             .________________________________.
            /__________________________________\
           /____________________________________\
          /______________________________________\
         /________________________________________\
         |__|__|__|__|__|__|__|__|__|__|__|__|__|__|
         |__|__|__|__|__|__|__|__|__|__|__|__|__|__|
         
         
welcome to the treasure island game!
Your mission is to find the treasure... Good luck!
""")

print ("You're at a crossroad. Where do you want to go? Type 'left' or 'right'")
choice1 = input(">>> ").lower()
if choice1 == "left":
     print ("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.")
     choice2 = input(">>> ").lower()
     if choice2 == "wait":
          print ("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
          choice3 = input(">>> ").lower()
          if choice3 == "red":
               print ("It's a room full of fire. GAME OVER.")
          elif choice3 == "yellow":
               print ("You found the treasure! YOU WIN!\n🥳🥳🥳\nTREASURE is ALL YOURS!\n🪙 ☠️ 🪙 ☠️ 🪙")
          elif choice3 == "blue":
               print ("You enter a room filed with beasts. GAME OVER.")
          else:
            print ("You chose a door that doesn't exist. GAME OVER.")
     else:
        print ("You get attacked by an angry trout. GAME OVER.")
else:
     print ("You fell into a hole. GAME OVER.")

