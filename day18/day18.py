# https://www.udemy.com/course/100-days-of-code/learn/lecture/20236706#overview

# Day 18 - Turtle graphics/Tuples

# https://docs.python.org/3/library/turtle.html
from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()
screen.colormode(255)
timmy.shape("turtle")
#timmy.color("blue")

# Drawing a 100*100 square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)

# Drawing a dashed line (10 by 10) for 15 times
# for i in range(15):
#     if i % 2 == 0:
#         timmy.pendown()
#     else:
#         timmy.penup()
#     timmy.forward(10)

# Drawing triangle to decagon, with randomized colors
def rand_color():
    rgb = []
    for i in range(3):
        color = random.randrange(255)
        rgb.append(color)
    return tuple(rgb)


# for i in range(3, 11):
#     cycle = 360
#     angle = cycle / i
#     rgb = rand_color()
#     timmy.pencolor(rgb)
#     for j in range(i):
#         timmy.left(angle)
#         timmy.forward(100)


# Random walk with randomized colors
# https://en.wikipedia.org/wiki/Random_walk
def rand_direction():
    angles = []
    for i in range(4):
        angles.append(i*90)

    return random.choice(angles)


# speed = 1
# width = 1
# for i in range(200):
#     direction = rand_direction()
#     rgb = rand_color()
#     timmy.pencolor(rgb)
#     timmy.left(direction)
#     timmy.forward(30)
#     timmy.width(width)
#     timmy.speed(speed)
#     if speed < 10 and speed != 0:
#         speed += 1
#         width += 1
#     elif speed == 10:
#         speed = 0


# Spirograph
def rotation_angle(i, j):
    angle = 360 / j
    angle *= i
    timmy.setheading(angle)

# timmy.hideturtle()
# x = 50
# speed = 10
# timmy.speed(speed)
# for i in range(x):
#     rotation_angle(i, x)
#     rgb = rand_color()
#     timmy.pencolor(rgb)
#     timmy.circle(100)


# Painting project
# pip install colorgram.py
# 10 * 10 dots sized 20 spaced by 50

x = 10
y = 10
space = 50
dot_size = 20
num_colors = 30
def paint(x, y, dot_size, space, num_colors):
    # Making the set of colors
    colors = []
    for i in range(num_colors):
        colors.append(rand_color())

    #print(colors)

    # Creating the canvas
    screen.setworldcoordinates(-dot_size, -dot_size, (dot_size*x+space*(x-1)), (dot_size*y+space*(y-1)))
    timmy.penup()
    timmy.hideturtle()

    # Painting the colored dots
    for i in range(y):
        timmy.setpos(0, i*50)
        for j in range(x):
            color = random.choice(colors)
            timmy.dot(dot_size, color)
            timmy.forward(space)

paint(x, y, dot_size, space, num_colors)

screen.exitonclick()