# https://www.udemy.com/course/100-days-of-code/learn/lecture/19140872#overview

# Day 7
# Hangman project

# Steps

# Game select a random word in a list / generate a random word
# User is shown numbers of letters of the selected word as "_"
# As long as the word isn't completed, or the user hasn't run out of "lives", 
# the user inputs a letter
# If the letter input is present in the word, replace the corresponding "_" with it
# If not, take out one live (draw a part of the hanged man)
# Repeat input process


# Solo attempt
import random
word_list = ["alpha", "beta", "gamma", "delta"]
chosen_word = random.choice(word_list)
chosen_word = list(chosen_word)
# print(chosen_word)

blank_word = ""
for i in range(0, len(chosen_word)):
    blank_word += "_"
blank_word = list(blank_word)
# print(blank_word)

def stringify_blankword():
    str_blank_word = "".join(blank_word)
    print(str_blank_word)

# 6 lives for only the body, 11 with the gallows
# lives = int(input("How many attempts would you like to have ? Pick 6 or 11\n"))
lives = 6 # could be variable, maybe ask the user between multiple choices ?

while lives > 0 and "_" in blank_word:
    stringify_blankword()
    user_guess = input("Please guess a letter: ")
    if user_guess in chosen_word:
        #print("present")
        while user_guess in chosen_word:
            guess_index = chosen_word.index(user_guess)
            #print(guess_index)
            blank_word[guess_index] = user_guess
            chosen_word[guess_index] = "-"
            # print(blank_word)
            # print(chosen_word)
    else:
        #print("not present")
        lives -= 1
        print(lives)
stringify_blankword()
if lives == 0:
    print("You lost.")
if not "_" in blank_word:
    print("You win.")

# Fonctionnal, no ascii art
# Clean code :

word_list = ["alpha", "baton", "croissant", "difficile", "electrique", "fenouille", "grenier", "heros", "illusion", "joueur", "kiosque", "lamentin",
             "marquis", "nonobstant", "oxygene", "polka", "quartz", "rythmique", "surprenant", "topaze", "uchronique", "vapeur", "wagon", "xenophile", "zombie"]
chosen_word = random.choice(word_list)
chosen_word = list(chosen_word)

blank_word = ""
for i in range(0, len(chosen_word)):
    blank_word += "_"
blank_word = list(blank_word)

def stringify_blankword():
    str_blank_word = "".join(blank_word)
    print(str_blank_word)

# lives = int(input("How many attempts would you like to have ? Pick 6 or 11\n"))
lives = 6

while lives > 0 and "_" in blank_word:
    stringify_blankword()
    user_guess = input("Please guess a letter: ")
    if user_guess in chosen_word:
        while user_guess in chosen_word:
            guess_index = chosen_word.index(user_guess)
            blank_word[guess_index] = user_guess
            chosen_word[guess_index] = "-"
    else:
        lives -= 1
        if lives == 1 or lives == 0:
            print(f"You have {lives} attempt remaining.")
        else:
            print(f"You have {lives} attempts remaining.")
stringify_blankword()
if lives == 0:
    print("You lost.")
if not "_" in blank_word:
    print("You win.")

# Improvement post "correction"

import day7_hangman_art
from day7_hangman_words import word_list # imported words list

logo = day7_hangman_art.logo
stages = day7_hangman_art.stages
 
chosen_word = random.choice(word_list)
chosen_word_list = list(chosen_word)

blank_word = ""
for i in range(0, len(chosen_word_list)):
    blank_word += "_"
blank_word = list(blank_word)


def stringify_blankword():
    str_blank_word = "".join(blank_word)
    print(str_blank_word)

lives = 6
already_guessed_list = []
alphabet = list("azertyuiopqsdfghjklmwxcvbn")

print(logo) # imported logo
while lives > 0 and "_" in blank_word:
    print(stages[lives]) # imported ascii art
    print(already_guessed_list) # list of already guessed letters
    stringify_blankword()

    user_guess = input("Please guess a letter: ").lower() # safety mesure

    if len(user_guess) > 1 or user_guess not in alphabet:  # safety mesures
        print("Input not a letter.")
    elif user_guess in already_guessed_list:
      print(f"You've already guessed {user_guess}.")
    elif user_guess in chosen_word_list:
        while user_guess in chosen_word_list:
            guess_index = chosen_word_list.index(user_guess)
            blank_word[guess_index] = user_guess
            chosen_word_list[guess_index] = "-"
        already_guessed_list.append(user_guess)
    else:
        lives -= 1
        if lives == 1 or lives == 0:
            print(f"You have {lives} attempt remaining.")
        else:
            print(f"You have {lives} attempts remaining.")
        already_guessed_list.append(user_guess)

stringify_blankword()
if lives == 0:
    print(f"The word was : {chosen_word}")
    print("You lost.")
if not "_" in blank_word:
    print("You win.")