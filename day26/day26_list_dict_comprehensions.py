# https://www.udemy.com/course/100-days-of-code/learn/lecture/20761314#overview

# Day 26 - List and dictionnary comprehensions

import random

# List comprehensions
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
# print(new_numbers)

name = "Angela"
letters_list = [letter for letter in name]
# print(letters_list)

range_list = [n * 2 for n in range(1, 5)]
# print(range_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
modified_names = [name.upper() for name in names if len(name) > 4]
# print(modified_names)


# Dictionary comprehensions

# starting with a list
students_scores = {student:random.randint(0, 100) for student in names}
# print(students_scores)

# starting with a dict
passed_students = {student:score
                   for (student, score) in students_scores.items() if score > 59}
# print(passed_students)

# Exercice
# weather_c = {}
# weather_f = {day:(temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
