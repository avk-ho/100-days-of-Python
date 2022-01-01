# https://www.udemy.com/course/100-days-of-code/learn/lecture/19211026#overview

# Day 8
# Functions with input

import random

# No input
def greet():
    greetings = ["Hello", "Salutations", "Greetings"]
    picked_greetings = random.choice(greetings)
    print(picked_greetings)

greet()

# With input
def greet_with_name(name):
    greetings = ["Hello", "Salutations", "Greetings"]
    picked_greetings = random.choice(greetings)
    print(picked_greetings + " " + name)


greet_with_name("Angela")

# With multiples inputs
def greet_with(name, location):
    greetings = ["Hello", "Salutations", "Greetings"]
    picked_greetings = random.choice(greetings)
    print(picked_greetings + " " + name)
    print("How is it in " + location + " ?")


greet_with("Angela", "London")
greet_with(location="London", name="Angela")


# Exercice 1 - Paint Area calculator

# Own code
def paint_calc(height, width, cover):
    surface = height*width
    nb_cans = surface / cover
    if nb_cans > int(nb_cans):
        nb_cans += 1
    nb_cans = int(nb_cans)
    print(f"You'll need {nb_cans} cans of paint.")

# import math
# math.ceil(nb_cans)

# Exercice 2 - Prime number checker

# Own code
def prime_checker(number):
    divisors = []
    if number == 2:
        print("It's a prime number.")
    elif number % 2 == 0:
        print("It's not a prime number.")
    else:
        for i in range(1, number, 2):
            if number % i == 0:
                divisors.append(i)
        if len(divisors) > 2:
            print("It's not a prime number.")
        else:
            print("It's a prime number.")

# Confirming for 2 is important because it is the exception for the loop
# It also allows us to then cut all even numbers saving half the operations

# Correction
# A better function that stops once the number is confirmed not a prime number
# Hybrid of the correction

# Own code
def prime_checker(number):
    is_prime = True
    if number != 2 and number % 2 == 0:
        is_prime = False
    else:
        for i in range(3, number, 2):
            if number % i == 0:
                is_prime = False
                break
    if is_prime and number != 1:
        print("It's a prime number.")
    else:
        print("It's not a prime number.") 

# Exercice - Project Caesar Cipher
# https://en.wikipedia.org/wiki/Caesar_cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Solo attempt
def caesar_cipher(direction, text, shift):
    text_len = len(text)
    text_list = list(text)

    if direction == "decode":
        shift = shift * (-1)

    for i in range(0, text_len):
        if text_list[i] in alphabet:
            i_index = alphabet.index(text_list[i])
            shifted_index = i_index + shift
            text_list[i] = alphabet[shifted_index]
    #print(text_list)
    shifted_text = "".join(text_list)
    print(f"Here's the encoded result: {shifted_text}")
caesar_cipher(direction, text, shift)

# missed a few cases, including index error out of range 
# if letters are close to the end of the alphabet

# Post "correction"
def caesar_cipher(direction, text, shift):
    text_len = len(text)
    text_list = list(text)

    if direction == "decode":
        shift *= -1
    
    for i in range(0, text_len):
        if text_list[i] in alphabet:
            alphabet_index = alphabet.index(text_list[i])
            shifted_index = (alphabet_index + shift) % 26 # Solve index out of range error
            text_list[i] = alphabet[shifted_index]
    shifted_text = "".join(text_list)
    print(f"Here's the {direction}d result: {shifted_text}")

should_continue = True # Allow the code to keep going

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == "encode" or direction == "decode": # Security
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        shift = shift % 26 # Security

        caesar_cipher(direction, text, shift)

        repeat = input("Type 'stop' if you want to stop. Else enter any key.\n")
        if repeat == "stop":
            should_continue = False
            print("Goodbye.")
    else:
        print("Wrong input.")
