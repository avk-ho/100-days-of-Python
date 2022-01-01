# https://www.udemy.com/course/100-days-of-code/learn/lecture/19279090#overview

# Day 8 - Dictionaries / Nesting

# Exercice 1 - Grading program

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

# Own code
student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score <= 70:
        student_grades[student] = "Fail"
    elif score < 81:
        student_grades[student] = "Acceptable"
    elif score < 91:
        student_grades[student] = "Exceeds Expectations"
    else:
        student_grades[student] = "Outstanding"

# Exercice 2 - Adding a entry to a list of dictionaries

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(country, visits, cities):
    new_country = {
        "country": country,
        "visits": visits,
        "cities": cities
    }
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

# Exercice project : Blind auction program
# See in the day9 project folder