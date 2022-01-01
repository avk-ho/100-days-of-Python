# https://www.udemy.com/course/100-days-of-code/learn/lecture/18085727#overview

# Day 5
# For loops

# Exercice : Average height
# Restrictions : no use of sum() and len()

import random
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# Own code
num_students = 0
sum_of_heights = 0

for height in student_heights:
    num_students += 1
    sum_of_heights += height

average_height = round(sum_of_heights / num_students)
print(average_height)

# Exercice : Highest score
# Restrictions : no use of max()
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

# Own code
max_score = 0

for score in student_scores:
    if score > max_score:
        max_score = score

print(f"The highest score in the class is: {max_score}")

# Exercice : Calculate sum of all even numbers from 1 to 100
sum_of_evens = 0

for num in range(0, 101, 2): # be careful that the range do not end at 100
    sum_of_evens += num

print(sum_of_evens)

# Exercice : FizzBuzz

for num in range(1, 101):
    to_print = ""
    if num % 3 == 0:
        to_print += "Fizz"
    if num % 5 == 0:
        to_print += "Buzz"

    if to_print == "":
        print(num)
    else:
        print(to_print)


# Exercice Project : password generator

#Password Generator Project
#import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# Own code
letters_len = len(letters)
numbers_len = len(numbers)
symbols_len = len(symbols)

password = ""

# After correction : random.choice(letters) would have worked
for i in range(0, nr_letters):
    password += letters[random.randint(0, (letters_len-1))]

for i in range(0, nr_symbols):
    password += symbols[random.randint(0, (symbols_len-1))]

for i in range(0, nr_numbers):
    password += numbers[random.randint(0, (numbers_len-1))]

#print(f"Here is your password: {password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# Own code
password = list(password)
random.shuffle(password)
randomised_pw = "".join(password)
print(f"Here is your password: {randomised_pw}")