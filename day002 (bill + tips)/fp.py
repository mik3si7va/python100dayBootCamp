print("welcome to the tip calculator!\n")
total = float(input("what was the total bill?\n$"))
percent = int(input("what percentage tip would you like to give? 10, 12, or 15?\n"))
people = int(input("how many people are splitting the bill?\n"))
tip = total * percent / 100
totality = total + tip
bill_per_person = totality / people
print(f"each person should pay: ${round(bill_per_person, 2)}")