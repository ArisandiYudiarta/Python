# List comprehension

# l1 = "arisandi"
# new_l2 = [n for n in l1]
# print(new_l2)

# doubled = [n * 2 for n in range(1, 5)]
# print(doubled)
import random

all_names = ["Alex", "Beth", "Caroline", "Dave", "Eleanore", "Freddie"]

# list comprehension
short_names = [name for name in all_names if len(name) < 5]
long_names_uppercase = [name.upper() for name in all_names if len(name) >= 5]

# dictionary comprehension
students_scores = {student: random.randint(40, 100) for student in all_names}
passed_students = {
    passed: score for (passed, score) in students_scores.items() if score > 60
}

# print(short_names)
# print(long_names_uppercase)
print(students_scores)
print(passed_students)

student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
