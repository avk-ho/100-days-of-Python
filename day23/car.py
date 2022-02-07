import variables as var
from turtle import Turtle
import random

class Car(Turtle):
    def __init__(self) -> None:
        super().__init__()

        self.shape("square")
        self.resizemode("user")
        self.shapesize(1, 2)
        self.color(random.choice(var.CARS_COLORS))
        self.penup()
        self.setheading(180)
        self.setpos(var.SCREEN_WIDTH/2, random.randrange(var.CARS_SPAWNING_Y_RANGE["bottom_limit"], var.CARS_SPAWNING_Y_RANGE["top_limit"]))
        
    def move(self, level):
        distance = var.CARS_STARTING_MOVE_DISTANCE + (level - 1)*var.CARS_MOVE_INCREMENT
        self.forward(distance)