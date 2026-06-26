from os import path

directory = path.dirname(__file__)

# TODO: Create a letter using starting_letter.txt
letter = open(path.join(directory, "Input/Letters/starting_letter.txt"), "r")

# for each name in invited_names.txt
names = []
with open(path.join(directory, "Input/Names/invited_names.txt"), "r") as names_file:
    for name in names_file:
        names.append(name.strip())
# Replace the [name] placeholder with the actual name.
letters = []
for name in names:
    letter.seek(0)
    letters.append(letter.read().replace("[name]", name))
# Save the letters in the folder "ReadyToSend".
for i, name in enumerate(names):
    with open(
        path.join(
            directory, f"Output/ReadyToSend/letter_for_{name.replace(' ', '_')}.txt"
        ),
        "w",
    ) as completed_letter:
        completed_letter.write(letters[i])

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
