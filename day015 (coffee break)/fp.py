from time import sleep

import art_mod
import data_mod

rainbow_print = art_mod.rainbow_print
red_print = art_mod.print_red_text
blue_print = art_mod.print_blue_text
green_print = art_mod.print_green_text
refill = data_mod.refill_machine
recipes = data_mod.recipes
money = art_mod.money_back

rainbow_print(art_mod.banner)
# rainbow_print(art_mod.espresso,gradient=2)
# rainbow_print(art_mod.latte,gradient=2)
# rainbow_print(art_mod.capuccino,gradient=2)
machine = data_mod.machine.copy()
green_print("Welcome to the Coffee Machine!..") 
while True:
    blue_print("What would you like? (espresso/latte/cappuccino/report/refill/off)")

    decision = input(">>> ").lower()

    if decision == "report":
        print(f"Water: {machine['water']}ml")
        print(f"Milk: {machine['milk']}ml")
        print(f"Coffee: {machine['coffee']}g")
        print(f"Money: ${machine['money']}")
    elif decision == "off":
        red_print("Turning off the machine... Goodbye! 🫡")
        break
    elif decision == "refill":
        refill(machine)
        green_print("✅ Machine refilled successfully!")
    elif decision in ["espresso", "latte", "cappuccino"]:
        if recipes[decision]["water"] > machine["water"]:
            red_print("❌ Not enough water! Please refill the machine.")
            continue
        if recipes[decision]["milk"] > machine["milk"]:
            red_print("❌ Not enough milk! Please refill the machine.")
            continue
        if recipes[decision]["coffee"] > machine["coffee"]:
            red_print("❌ Not enough coffee! Please refill the machine.")
            continue
        blue_print(f"You selected {decision}. Please insert ${recipes[decision]['cost']:.2f}.")
        red_print("BTW we don't want your pennies .. 💰 Insert these coins (quarters, dimes, nickels):")
        quarters = int(input("# of quarters?\n>>> "))
        dimes = int(input("# of dimes?\n>>> "))
        nickels = int(input("# of nickels?\n>>> "))
        total_inserted = quarters * 0.25 + dimes * 0.10 + nickels * 0.05
        if total_inserted < recipes[decision]["cost"]:
            red_print("❌ Not enough money! Here is your refund.")
            continue
        machine["water"] -= recipes[decision]["water"]
        machine["milk"] -= recipes[decision]["milk"]
        machine["coffee"] -= recipes[decision]["coffee"]
        machine["money"] += recipes[decision]["cost"]
        green_print(f"☕ Preparing your {decision}...")
        sleep(1)
        rainbow_print("Brewing...",gradient=2)
        sleep(1)
        rainbow_print("Pouring...",gradient=2)
        sleep(1)
        rainbow_print("HERE's your ..",gradient=2)
        rainbow_print(getattr(art_mod, decision),gradient=2)
        sleep(1)
        rainbow_print("Enjoy your coffee! ☕\n",gradient=2)
        change = total_inserted - recipes[decision]["cost"]
        if change > 0:
            green_print(f"💵 Here is ${change:.2f} in change.")
            rainbow_print(money,gradient=2)
        
    else:
        red_print("❌ Invalid choice! Please select a valid option.")