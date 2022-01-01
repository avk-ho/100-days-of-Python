# https://www.udemy.com/course/100-days-of-code/learn/lecture/18011837#overview

# Day 4
# Randomness / Lists

# Exercice: Heads or tails

# Own code
import random

rand_int = random.randint(0, 1)
if rand_int == 1:
    print("Heads")
else:
    print("Tails")

# Exercice: Banker roulette

# reimporting random unnecessary

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# Own code
len_names = len(names)
rand_int = random.randint(0, (len_names-1))
rand_name = names[rand_int]
print(f"{rand_name} is going to buy the meal today!")

# same thing can be done with random.choice(names)

# Exercice: Treasure map

row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# Own code
x_column = int(position[0])-1
x_row = int(position[1])-1

map[x_row][x_column] = "X"

# End own code
print(f"{row1}\n{row2}\n{row3}")

# input, turned into int between 11 and 33

# Exercice Project: Rock-Paper-Scissors game

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Own code
# 0 Rock // 1 Paper // 2 Scissors
images = [rock, paper, scissors]# Added post "correction"
player_input = input("What do you choose ? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n")
if player_input != "0" and player_input != "1" and player_input != "2":
    print("You typed an invalid number.")
else:
    player_choice = int(player_input)
    com_choice = random.randint(0, 2)
    draw = False
    if player_choice == com_choice:
        draw = True

    # if player_choice == 0:
    #     print(rock)
    # elif player_choice == 1:
    #     print(paper)
    # elif player_choice == 2:
    #     print(scissors)
    print(images[player_choice]) # Added post "correction"

    print("Computer chose:")

    # if com_choice == 0:
    #     print(rock)
    # elif com_choice == 1:
    #     print(paper)
    # elif com_choice == 2:
    #     print(scissors)
    print(images[com_choice]) # Added post "correction"

    if draw:
        print("\nIt's a draw.")
    else:
        if com_choice == 2:
            if player_choice == 0:
                print("\nYou win.")
            else:
                print("\nYou lose.")
        elif com_choice == 0 and player_choice == 2:
            print("\nYou lose.")
        else:
            if com_choice == player_choice + 1:
                print("\nYou lose.")
            else:
                print("\nYou win.")