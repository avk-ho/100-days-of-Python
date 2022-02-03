# https://www.udemy.com/course/100-days-of-code/learn/lecture/20336493#overview

# Day 19 - Event listeners / Object instances

from turtle import Turtle, Screen, shape, width
import random

tim = Turtle()
tim.hideturtle()
screen = Screen()

# Event listeners

# def move_forwards():
#     tim.forward(10)

# screen.listen()
# screen.onkey(key="space", fun=move_forwards)

# Etch a sketch project
# Commands : Z forwards, S backwards, Q counter clockwise, D clockwise, C clear screen & recenter

# def move_forwards():
#     tim.forward(5)

# def move_backwards():
#     tim.backward(5)

# def turn_clockwise():
#     tim.left(5)

# def turn_counterclockwise():
#     tim.right(5)

# def reset():
#     screen.reset()
#     tim.reset()

# speed = 10
# width = 3
# tim.width(width)
# tim.speed(speed)

# screen.listen()
# screen.onkey(key="c", fun=reset)
# screen.onkeypress(key="z", fun=move_forwards)
# screen.onkeypress(key="s", fun=move_backwards)
# screen.onkeypress(key="q", fun=turn_clockwise)
# screen.onkeypress(key="d", fun=turn_counterclockwise)


# Turtle race project

# Colors list
colors = ["red", "blue", "green", "yellow", "orange", "purple"]

# Creating the screen
screen.setup(width=500, height=400)

# Getting the user imput
colors_str = "/".join(colors)
user_bet = screen.textinput(title="Make your bet.", prompt=f"Which turtle will win the race ? ({colors_str})")

# Creating and placing the turtles (40*40)
start_x = -230
start_y = -150
turtles = {}
for i in range(len(colors)):
    turtles[colors[i]] = Turtle(shape="turtle")
    turtles[colors[i]].penup()
    turtles[colors[i]].setpos(x=-230, y=-130+i*50)
    turtles[colors[i]].color(colors[i])
    turtles[colors[i]].speed(10)

# Creating the race
if user_bet:
    is_race_on = True

winner = ""

while is_race_on:
    for turtle in turtles:
        distance = random.randrange(10)
        turtles[turtle].forward(distance)
        if turtles[turtle].xcor() >= 230:
            is_race_on = False
            winner = turtle
            # break

if user_bet == winner:
    print(f"The {winner} turtle crossed the line. You win.")
else:
    print(f"The {winner} turtle crossed the line. You lose.")

screen.exitonclick()