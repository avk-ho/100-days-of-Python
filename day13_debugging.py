# https://www.udemy.com/course/100-days-of-code/learn/lecture/19846328#overview

# Day 13 - Debugging tips

# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# It's a simple for loop, the problem is that in python, range(1, 20)
# goes from 1 to 19 (20 not inclusive), so the variable "i" will never be equal to 20

# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()
# changing the if statement is also a possible fix

#####

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# # dice_num will generate a number from 1 to 6 both included, 
# # however, dice_imgs is a list, so its indexes are starting from 0

# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = 6 #dice_num = randint(0, 5) is the fix
# print(dice_imgs[dice_num])
# Will always return an error

#####

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# Both if statements check for over or under 1994 but do not have a statement for
# the year 1994 itself, also for under 1981

# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")

#####

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# Indentation mistake caught by the editor for the print statement
# also input returns a string, string cannot be compared to an int

# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")

#####

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# the second word_per_page line is a comparison so will return a boolean

# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

#####

# #Use a Debugger
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#     b_list.append(new_item)
#     print(b_list)

# mutate([1,2,3,5,8,13])

# the list is only appended once since the line isn't indented to be within the loop

# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#     print(b_list)

# mutate([1,2,3,5,8,13])

# Exercice 1 - Odd or even fix

# number = int(input("Which number do you want to check?"))

# if number % 2 = 0: # mistake here
#   print("This is an even number.")
# else:
#   print("This is an odd number.")

# if number % 2 == 0:
#   print("This is an even number.")
# else:
#   print("This is an odd number.")

# Exercice 2 - Leap year or not fix

# year = input("Which year do you want to check?") # type error here, str when we need an int

# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")

# year = int(input("Which year do you want to check?"))

# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")

# Exercice 3 - Fizz Buzz fix

# for number in range(1, 101):
#   if number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print([number])


for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)