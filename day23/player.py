from turtle import Turtle
import variables as var

class Player(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setpos(var.PLAYER_STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(var.PLAYER_MOVE_DISTANCE)

    def level_up(self):
        self.setpos(var.PLAYER_STARTING_POSITION)
