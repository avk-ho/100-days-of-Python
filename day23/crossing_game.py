# https://www.udemy.com/course/100-days-of-code/learn/lecture/20396023#overview

# Day 23 - Turtle crossing game project

# 1. A turtle moves forwards when you press the "Up" key. It can only move forwards, 
# not back, left or right.

# 2. Cars are randomly generated along the y-axis and 
# will move from the right edge of the screen to the left edge.

# 3. When the turtle hits the top edge of the screen, 
# it moves back to the original position and the player levels up. 
# On the next level, the car speed increases.

# 4. When the turtle collides with a car, it's game over and everything stops.


# Solo attempt with the base code

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import variables as var
import random

screen = Screen()
screen.setup(width=var.SCREEN_WIDTH, height=var.SCREEN_HEIGHT)
screen.tracer(0)

player = Player()

scoreboard = Scoreboard()

car_manager = CarManager()

screen.listen()
screen.onkeypress(player.move, "z")

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    # Random car generation
    if random.randrange(var.CARS_SPAWNING_RATE) == 0:
        car_manager.add_car()

    # Cars
    for car in car_manager.cars_list:
        car.move(scoreboard.level)

        # Detection with the player
        if car.distance(player) < 27:
            game_is_on = False
            scoreboard.game_over()
            break
        
        # Removing cars going off-screen
        if car.xcor() < (var.SCREEN_WIDTH/2 + 20)*-1:
            car_manager.remove_car(car)

    # Level up
    if player.ycor() >= var.FINISH_LINE_Y:
        player.level_up()
        scoreboard.level_up()

    screen.update()

screen.exitonclick()