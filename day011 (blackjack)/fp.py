import math
import random
import cards_module

def print_welcome():
    print(r"""

       .------.
       |A_  _ |     ██████╗ ██╗      █████╗  ██████╗██╗  ██╗     ██╗ █████╗  ██████╗██╗  ██╗
       |( \/ )|     ██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝     ██║██╔══██╗██╔════╝██║ ██╔╝
 .------.\  / |     ██████╔╝██║     ███████║██║     █████╔╝      ██║███████║██║     █████╔╝
 |K_  _ | \/ A|     ██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██   ██║██╔══██║██║     ██╔═██╗
 |( \/ )|-----'     ██████╔╝███████╗██║  ██║╚██████╗██║  ██╗╚█████╔╝██║  ██║╚██████╗██║  ██╗
 | \  / |           ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
 |  \/ K|
 `------'                            ♠  Hit me, dealer..  ♠

        """)




cards = [
    "A", "2", "3", "4", "5", "6", "7",
    "8", "9", "10", "J", "Q", "K"
]

suits = [
    "♠",  # Spades
    "♥",  # Hearts
    "♦",  # Diamonds
    "♣"   # Clubs
]

def score_of (cards):
    score = 0
    
    for card in cards:
        if card[0] == 'A':
            score += 11
        elif (card[0] in 'JQK') or card[0:2] == '10':
            score += 10
        else:
            score += int(card[0])
    
    if score > 21:
        for card in cards:
            if card[0] == 'A' and score > 21:
                score -= 10
        
    return score
    
def print_cards(cards, dealer=False):

    # Convert each card into a list of lines
    card_assignment = {
        "A": 0,
        "2": 1,
        "3": 2,
        "4": 3,
        "5": 4,
        "6": 5,
        "7": 6,
        "8": 7,
        "9": 8,
        "10": 9,
        "J": 10,
        "Q": 11,
        "K": 12
    }
    suits_assignment = {
        "♠": 0,
        "♥": 1,
        "♦": 2,
        "♣": 3
    }
    
    formated_cards = []
    
    for i in range(len(cards)):
        card = cards[i]
        if card == '?':
            formated_cards.append(cards_module.mystery_card)
            continue
        if card[0:2] == '10':
            card_value = card_assignment['10']
        else:
            card_value = card_assignment[card[0]]
        card_suit = suits_assignment[card[-1]]
        formated_cards.append(cards_module.cards[card_value][card_suit])
    
    split_cards = []

    for card in formated_cards:
        split_cards.append(card.splitlines())

    # Number of lines in a card
    num_lines = len(split_cards[0])

    # Print one row of all cards at a time
    for line_index in range(num_lines):
        
        if dealer:
            row = "     "
        else:
            row = ""

        for card in split_cards:
            row += card[line_index] + "    "

        print(row)
        
deck = []

for suit in suits:
    for card in cards:
        deck.append(f"{card}{suit}")


print_welcome()
first_time = True
while True:
    keep_playing = input(f"\nWanna {'play' if first_time else 'keep playing'} {'a' if first_time else 'another'} round of BLACKJACK? (y/N)\n>>> ").lower() == 'y' and True or False            
    if first_time:
        first_time = False
    if not keep_playing:
        break
    if not first_time:
        print_welcome()
    temp = deck.copy()
    yours = []
    dealers = []

    for i in range(6):
        card = random.choice(temp)
        temp.remove(card)
        if i % 2 == 0:
            yours.append(card)
        else:
            dealers.append(card)
    numcards = 2
    dealcards = 1
    print(f"\nYour Cards: SCORE of {score_of(yours[0:numcards])}")
    print_cards(yours[0:numcards])
    print(f"\n   AGAINST Dealer's Cards: SCORE of {score_of(dealers[0:dealcards])} + ?")
    print_cards(dealers[0:dealcards] + ["?"], dealer=True)
    hit = input("\nHIT it or STAND it? (y for HIT)\n>>> ").lower() == 'y' and True or False
    skip = False
    while hit:
        numcards += 1
        if numcards > 3:
            newcard = random.choice(temp)
            temp.remove(newcard)
            yours.append(newcard)
        
        print(f"\nYour Cards: SCORE of {score_of(yours[0:numcards])}")
        print_cards(yours[0:numcards])
        print(f"\n   AGAINST Dealer's Cards: SCORE of {score_of(dealers[0:dealcards])} + ?")
        print_cards(dealers[0:dealcards] + ["?"], dealer=True)
        if score_of(yours[0:numcards]) > 21:
            print(cards_module.bust_flag)
            print("BUSTED! You lose.. ☠️  ☠️  ☠️")
            skip = True
            break
        else:
            hit = input("\nHIT it or STAND it? (y for HIT)\n>>> ").lower() == 'y' and True or False
    if skip:
        continue
    input("Dealer's about to reveal his second card... press Enter to continue..") 
    dealcards += 1
    print(f"\nYour Cards: SCORE of {score_of(yours[0:numcards])}")
    print_cards(yours[0:numcards])
    print(f"\n   AGAINST Dealer's Cards: SCORE of {score_of(dealers[0:dealcards])}")
    print_cards(dealers[0:dealcards], dealer=True)
    if score_of(dealers[0:dealcards]) > 21:
        print(cards_module.u_win)
        print("Dealer BUSTED! You win.. 🏆  🏆  🏆")
        continue
    elif score_of(yours[0:numcards]) < score_of(dealers[0:dealcards]):
        print(cards_module.u_lost)
        print("You lose.. ☠️  ☠️  ☠️")
        continue
    elif score_of(yours[0:numcards]) == score_of(dealers[0:dealcards]):
        print(cards_module.u_draw)
        print("It's a TIE! No one wins..")
        continue
    elif score_of(yours[0:numcards]) >= score_of(dealers[0:dealcards]) and score_of(dealers[0:dealcards]) < 17:
        input("Dealer HITS and is about to reveal a third card... press Enter to continue..") 
        dealcards += 1
        print(f"\nYour Cards: SCORE of {score_of(yours[0:numcards])}")
        print_cards(yours[0:numcards])
        print(f"\n   AGAINST Dealer's Cards: SCORE of {score_of(dealers[0:dealcards])}")
        print_cards(dealers[0:dealcards], dealer=True)
        if score_of(dealers[0:dealcards]) > 21:
            print(cards_module.u_win)
            print("Dealer BUSTED! You win.. 🏆  🏆  🏆")
            continue
        elif score_of(yours[0:numcards]) < score_of(dealers[0:dealcards]):
            print(cards_module.u_lost)
            print("You lose.. ☠️  ☠️  ☠️")
            continue
        elif score_of(yours[0:numcards]) == score_of(dealers[0:dealcards]):
            print(cards_module.u_draw)
            print("It's a TIE! No one wins..")
            continue
        else:
            print(cards_module.u_win)
            print("You win.. 🏆  🏆  🏆")
            continue
    else:
        print(cards_module.u_win)
        print("You win.. 🏆  🏆  🏆")
        continue
