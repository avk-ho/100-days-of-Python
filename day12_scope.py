# https://www.udemy.com/course/100-days-of-code/learn/lecture/19845970#content

# Day 12 - Scope

# Exercice project - Number guessing game

import random

def guessingGame():
    number = random.randrange(1, 101)
    lives = 10

    print("Welcome to the number guessing game.")
    print("I'm thinking of a number between 1 and 100 included.")

    input_check = False
    while not input_check:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if difficulty == "hard":
            lives = 5
            input_check = True
        elif difficulty == "easy":
            input_check = True
        else:
            print("Wrong input.")
    
    game_over = False
    while not game_over:
        print(f"You have {lives} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if user_guess == number:
            game_over = True
            print(f"You got it! The answer was {number}.")
            return
        elif user_guess > number:
            print("Too high.")
        elif user_guess < number:
            print("Too low.")
        
        lives -= 1
        if lives == 0:
            game_over = True

    print(f"You ran out of lives. You lose. The answer was {number}.")
    
    