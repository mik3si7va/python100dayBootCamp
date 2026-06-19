from time import sleep
import art_mod

machine = {
    "water": 600,
    "milk": 400,
    "coffee": 200,
    "money": 0
}

recipes = {
    "espresso": {
        "name": "espresso",
        "water": 50,
        "milk": 0,
        "coffee": 18,
        "cost": 1.5
    },
    
    "latte": {
        "name": "latte",
        "water": 200,
        "milk": 150,
        "coffee": 24,
        "cost": 2.5
    },
    "cappuccino": {
        "name": "cappuccino",
        "water": 250,
        "milk": 100,
        "coffee": 24,
        "cost": 3.0
    }
}

def refill_machine(machine):
    machine["water"] = 600
    machine["milk"] = 400
    machine["coffee"] = 200
    art_mod.print_green_text("✅ Machine refilled successfully!")

def make_coffee(machine, recipe):
    machine["water"] -= recipe["water"]
    machine["milk"] -= recipe["milk"]
    machine["coffee"] -= recipe["coffee"]
    machine["money"] += recipe["cost"]
    art_mod.print_green_text(f"☕ Preparing your {recipe['name'].lower()}...")
    sleep(1)
    art_mod.rainbow_print("Brewing...",gradient=2)
    sleep(1)
    art_mod.rainbow_print("Pouring...",gradient=2)
    sleep(1)
    art_mod.rainbow_print("HERE's your ..",gradient=2)
    art_mod.rainbow_print(getattr(art_mod, recipe['name'].lower()),gradient=2)
    sleep(1)
    art_mod.rainbow_print("Enjoy your coffee! ☕\n",gradient=2)
    
def report_machine(machine):
    print(f"Water: {machine['water']}ml")
    print(f"Milk: {machine['milk']}ml")
    print(f"Coffee: {machine['coffee']}g")
    print(f"Money: ${machine['money']}")

def check_resources(machine, recipe):
    if recipe["water"] > machine["water"]:
        art_mod.print_red_text("❌ Not enough water! Please refill the machine.")
        return False
    if recipe["milk"] > machine["milk"]:
        art_mod.print_red_text("❌ Not enough milk! Please refill the machine.")
        return False
    if recipe["coffee"] > machine["coffee"]:
        art_mod.print_red_text("❌ Not enough coffee! Please refill the machine.")
        return False
    return True

def calculate_change(total_inserted, cost):
    return total_inserted - cost

def process_coins():
    art_mod.print_red_text("BTW we don't want your pennies .. 💰 Insert these coins (quarters, dimes, nickels):")
    quarters = input("# of quarters?\n>>> ")
    quarters = int(quarters) if quarters.isdigit() else 0
    dimes = input("# of dimes?\n>>> ")
    dimes = int(dimes) if dimes.isdigit() else 0
    nickels = input("# of nickels?\n>>> ")
    nickels = int(nickels) if nickels.isdigit() else 0
    total_inserted = quarters * 0.25 + dimes * 0.10 + nickels * 0.05
    return total_inserted

def process_payment(total_inserted, cost):
    if total_inserted == 0:
        art_mod.print_red_text("❌ No coins inserted! Please insert coins to proceed.")
        return False
    if total_inserted < cost:
        art_mod.print_red_text("❌ Not enough money! Here is your refund.")
        return False
    return True

def change(change):
    art_mod.print_green_text(f"💵 Here is ${change:.2f} in change back..")
    art_mod.rainbow_print(art_mod.money_back)