prizes = [
    "A Pirate's Treasure Chest",
    "A Dragon Egg",
    "A Golden Crown",
    "A Mystery Box",
    "An Ancient Spell Book",
    "A Diamond Sword",
    "A Luxury Yacht",
    "A Private Island",
    "A Bag of Gold Coins",
    "A Time Machine",
    "A Flying Carpet",
    "A Pet Dragon",
    "A Space Shuttle",
    "A Castle in Scotland",
    "A Vintage Ferrari",
    "A Robot Butler",
    "A Unicorn",
    "A Lightsaber",
    "A Giant Ruby",
    "A Secret Treasure Map",
    "A Golden Ticket",
    "A Crystal Skull",
    "A Legendary Hammer",
    "A Treasure Vault Key",
    "A Lifetime Supply of Pizza",
    "A Gaming PC",
    "A Magic Wand",
    "A Sapphire Necklace",
    "A Moon Rock",
    "A King's Throne",
    "A Viking Longship",
    "A T-Rex Fossil",
    "A Lost Atlantis Artifact",
    "A Hoverboard",
    "A Potion of Immortality",
    "A Phoenix Feather",
    "A Billion Dollars",
    "A Dragon's Hoard",
    "The Holy Grail",
    "An Alien Spaceship",
    "A Golden Goose",
    "A Mechanical Dragon",
    "A Giant Emerald",
    "A Pirate Ship",
    "The Infinity Gauntlet",
    "A Secret Government File",
    "An Enchanted Mirror"
]

print(r"""
        _______
       /       \
      (=========)
       | |   | |\
       | |   | |{===}==/===]===o===<>===o=={===}====\
       | |___| |{===}==\===]===o===<>===o=={===}====/
       |_______|/
      (=========)
  \\   \_______/   //
     
     BANG!
              BANG!
       _________
      /| | | | |\       Bidding Time!!
========================================================
                           Highest Bid Wins the Auction!
                           
      bring on the bills! ... hehehe!!
                            
""")
import random

bidders = {}

prize = random.choice(prizes)

someone_else = True

while someone_else:
    print(f"Today's auction item is:\n   🏆 {prize}")
    name = input("wanna bid?? whats ur name?\n >>> ")
    amount = int(input("how much tho??\n >>> $"))
    if amount < 0:
        print("the most we can do is give it for free .. but never pay u to take it home... next time bid higher!!")
    else:
        bidders[name] = amount
    someone_else = input("anyone else bidding today?? (y/N)\n>>> ").lower() == 'y' and True or False
    print("\n"*77)

print(r"""
        _______
       /       \
  A   (=========)
  | |  | |   | |\
  | |  | |   | |{===}==/===]===o===<>===o=={===}====\
  | |  | |___| |{===}==\===]===o===<>===o=={===}====/
  V V  |_______|/
      (=========)
   **\ \_______/ /**
      /| | | | |\       BANG BANG!!
========================================================
                        AND THE WINNER OF THE ACTION IS...
                            
                            roll the drums 🥁🥁🥁 ...
                            
""")

max = 0
name = ''

for key in bidders:
    if bidders[key] > max:
        max = bidders[key]
        name = key
        
print(f"It's {name}!! congratulations!!! 🥳🥳\nYou are the new proud owner of {prize}!!\nAnd for a mear price of ${bidders[name]}!!\nA remarcable purchase indeed!")