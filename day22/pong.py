# https://www.udemy.com/course/100-days-of-code/learn/lecture/20414753#overview

# Day 22

# Pong game project

import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import variables as var

# Setting up the screen
screen = Screen()
screen.setup(width=var.SCREEN_WIDTH, height=var.SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

p1_paddle = Paddle(var.P1_STARTING_POS) # left
p2_paddle = Paddle(var.P2_STARTING_POS) # right

screen.listen()
screen.onkeypress(p1_paddle.up, "z")
screen.onkeypress(p1_paddle.down, "s")

screen.onkeypress(p2_paddle.up, "Up")
screen.onkeypress(p2_paddle.down, "Down")

ball = Ball()
scoreboard = Scoreboard()

game_over = False
while not game_over:
    screen.update()
    time.sleep(0.05)
    ball.move()

    # Collision of the ball with the top and bottom wall
    if ball.ycor() > var.SCREEN_HEIGHT/2 - 20 or ball.ycor() < (var.SCREEN_HEIGHT/2 - 20) * -1:
        ball.bounce()

    # Collision of the ball with the paddles
    if (ball.xcor() < var.P1_STARTING_POS[0] + 20 and ball.distance(p1_paddle) < 50) or (ball.xcor() > var.P2_STARTING_POS[0] - 20 and ball.distance(p2_paddle) < 50):
        ball.paddle_bounce()

    # Detection if the ball leaves the left or right borders
    if ball.xcor() > var.SCREEN_WIDTH/2 - 10 or ball.xcor() < (var.SCREEN_WIDTH/2 - 10) * -1:
        x_coor = ball.xcor()
        ball.reset_position(x_coor)
        scoreboard.update_score(x_coor)

screen.exitonclick()