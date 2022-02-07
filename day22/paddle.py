from turtle import Turtle
import variables as var

class Paddle(Turtle):
    def __init__(self, position) -> None:
        super().__init__()

        self.shape("square")
        self.color("white")
        self.penup()
        self.resizemode("user")
        self.shapesize(5, 1)
        self.setpos(position)

    # Move the paddle up
    def up(self):
        new_y = self.ycor() + var.PADDLE_MOV_DISTANCE
        self.sety(new_y)

    # Move the paddle down
    def down(self):
        new_y = self.ycor() - var.PADDLE_MOV_DISTANCE
        self.sety(new_y)
