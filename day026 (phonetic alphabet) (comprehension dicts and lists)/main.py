import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_numbers = [num * 2 for num in numbers]

print(new_numbers)  # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

doubles = [num * 2 for num in range(1, 5)]
print(doubles)  # Output: [2, 4, 6, 8]

phonetical_alphabet = {
    "A": "Alpha",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliett",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-ray",
    "Y": "Yankee",
    "Z": "Zulu",
}

name = input("Enter your name: ").upper()
phonetical_name = [
    phonetical_alphabet[letter] for letter in name if letter in phonetical_alphabet
]
print("Phonetical representation of your name:", " ".join(phonetical_name))

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

new_student_scores = {
    student: score + 5 for student, score in student_scores.items() if score > 80
}
print(new_student_scores)  # Output: {'Harry': 86, 'Hermione': 104}

student_names = [student for student, score in student_scores.items()]

print(student_names)  # Output: ['Harry', 'Ron', 'Hermione', 'Draco', 'Neville']

new_student_scores = {student: random.randint(0, 200) for student in student_names}

print(new_student_scores)  # Output: Random scores for each student

import pandas as pd

student_data = pd.DataFrame(new_student_scores.items(), columns=["Student", "Score"])
print(student_data)  # Output: DataFrame with student names and their random scores

for index, row in student_data.iterrows():
    print(
        f"{row['Student']} at index {index}, scored {row['Score']}"
    )  # Output: Each student's name and score
