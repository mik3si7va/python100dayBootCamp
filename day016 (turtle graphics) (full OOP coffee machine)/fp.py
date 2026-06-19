import art_mod
import data_mod

rainbow_print = art_mod.rainbow_print
red_print = art_mod.print_red_text
blue_print = art_mod.print_blue_text
green_print = art_mod.print_green_text
refill = data_mod.refill_machine
report_machine = data_mod.report_machine
make_coffee = data_mod.make_coffee
calculate_change = data_mod.calculate_change
recipes = data_mod.recipes
money = art_mod.money_back

rainbow_print(art_mod.banner)
machine = data_mod.machine.copy()
green_print("Welcome to the Coffee Machine!..") 
while True:
    blue_print("What would you like? (espresso/latte/cappuccino/report/refill/off)")

    decision = input(">>> ").lower()

    if decision == "report":
        report_machine(machine)
    elif decision == "off":
        red_print("Turning off the machine... Goodbye! 🫡")
        break
    elif decision == "refill":
        refill(machine)
    elif decision in ["espresso", "latte", "cappuccino"]:
        recipe = recipes[decision]
        resources_ok = data_mod.check_resources(machine, recipe)
        if not resources_ok:
            continue
        total_inserted = data_mod.process_coins()
        success = data_mod.process_payment(total_inserted, recipe["cost"])
        if not success:
            continue
        make_coffee(machine, recipe)
        change = calculate_change(total_inserted, recipe["cost"])
        if change > 0:
            data_mod.change(change)
    else:
        red_print("❌ Invalid choice! Please select a valid option.")