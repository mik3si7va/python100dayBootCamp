student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}

# Looping through dictionaries:
for key, value in student_dict.items():
    # Access key and value
    pass

import pandas
from os import path

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for index, row in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
phonetic_alphabet = {}
for index, row in pandas.read_csv(
    path.join(path.dirname(__file__), "nato_phonetic_alphabet.csv")
).iterrows():
    phonetic_alphabet[row.letter] = row.code

print(phonetic_alphabet)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
phonetical_word = [
    phonetic_alphabet[letter] for letter in word if letter in phonetic_alphabet
]
print(phonetical_word)
