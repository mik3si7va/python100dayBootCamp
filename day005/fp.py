import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "_", "+", "=", "<", ">", "?"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_chars = []

for _ in range(nr_letters):
    password_chars.append(random.choice(letters))

for _ in range(nr_symbols):
    password_chars.insert(random.randint(0, len(password_chars)), random.choice(symbols))

for _ in range(nr_numbers):
    password_chars.insert(random.randint(0, len(password_chars)), random.choice(numbers))

print(f"Your password is: {''.join(map(str, password_chars))}")

random.shuffle(password_chars)

print(f"Your password is: {''.join(map(str, password_chars))}")