print ("Welcome to the rollercoaster!")

height = int(input("what is your height in cm?\n"))
age = int(input("what is your age?\n"))
amount = 0
if height >= 120:
    if  45 <= age <= 55:
        amount += 0
    elif age >= 18:
        amount += 12
    elif age < 12:
        amount += 5
    else:
        amount += 7
    photo = bool(input("Do you want a photo taken? answer with Yes or No\n") == "Yes" and True or False)
    if photo:
        amount += 3
    print(f"Your final bill is: ${amount}")
else:
    print("Sorry, you have to grow taller before you can ride.")