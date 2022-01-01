# https://www.udemy.com/course/100-days-of-code/learn/lecture/17825914#overview

# Day 1
# Printing

# Version 1
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

# Version 2 - triple quotes for multilines prints
print('''Day 1 - Python Print Function
The function is declared like this:
print('what to print')
''')

# Version 3 - \n to start on a new line
print("Day 1 - Python Print Function\nThe function is declared like this:\nprint('what to print')")

# String concatenation
print("Hello " + "World")

# Error fixing

#print(Day 1 - String Manipulation") // missing " at the start
#print("String Concatenation is done with the "+" sign.") // should use ' ' for the print since we want the "+" to be printed
#  print('e.g. print("Hello " + "world")') // indentation mistake at the start of line
#print(("New lines can be created with a backslash and n.") // 2 "(" after the print

# Input
print("Hello " + input("What is your name?"))

# Exercice name character length
print(len(input("What is your name?")))

# Variable exercice
a = input("a: ")
b = input("b: ")
c = b
b = a
a = c

# Project exercice
#1. Create a greeting for your program.
print("Welcome to the band name generator")
#2. Ask the user for the city that they grew up in.
city_name = input("What is the name of the city you grew up in?\n")
#3. Ask the user for the name of a pet.
pet_name = input("What is the name of your pet, or that you think would be a good pet name?\n")
#4. Combine the name of their city and pet and show them their band name.
print("Your band name could be " + city_name + " " + pet_name)
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://replit.com/@appbrewery/band-name-generator-end