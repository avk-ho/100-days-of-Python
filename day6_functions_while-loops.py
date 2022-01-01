# https://www.udemy.com/course/100-days-of-code/learn/lecture/19110416#overview

# Day 6
# Functions

# Exercice 1
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# Own code
# def move_left():
#     turn_left()
#     move()


# def move_right():
#     turn_left()
#     turn_left()
#     turn_left()
#     move()


# def jump():
#     move()
#     move_left()
#     move_right()
#     move_right()
#     turn_left()


# for i in range(6):
#     jump()


# While loops

# Exercice 2
# Hurdle 2

# while not at_goal():
#     jump()


# Exercice 3
# Hurdle 3

# def jump():
#     move_left()
#     move_right()
#     move_right()
#     turn_left()


# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()

# Exercice 4
# Hurdle 4

# def jump():
#     move_left()
#     while wall_on_right():
#         move()
#     move_right()
#     move_right()
#     while front_is_clear():
#         move()
#     turn_left()


# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()

# Exercice Project : Escape the maze
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# This version becomes stuck in some infinite loop case

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# def move_left():
#     turn_left()
#     move()


# def move_right():
#     turn_right()
#     move()


# while not at_goal():
#     while wall_on_right():
#         if front_is_clear():
#             move()
#         else:
#             turn_left()
#     if not at_goal():
#         move_right()

# This version has solved the infinite loop case encountered

# x = 0
# while not at_goal():
#     while wall_on_right():
#         x = 0
#         if front_is_clear():
#             move()
#         else:
#             turn_left()
#     if x > 4: # After moving right 4 times in succession, we can confirm being in a loop (?)
#         if front_is_clear():
#             move()
#         else:
#             turn_left()
#             if front_is_clear():
#                 move()
#             else:
#                 turn_left()
#     if not at_goal() and right_is_clear():
#         move_right()
#         x += 1

# Solution given in correction :
# adding a while loop before the code
# while front_is_clear():
#     move()
# turn_left()
# guarantees that the robot find a right wall that it can then follow