from turtle import Turtle
import variables as var
import random

class Ball(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.acceleration = 0


        self.direction = var.BALL_STARTING_DIRECTION
        # top_right_edge = self.towards(var.SCREEN_WIDTH/2, var.SCREEN_HEIGHT/2)


    def move(self):
        self.setheading(self.direction)
        self.forward(10 + self.acceleration)

    def bounce(self):
        self.direction = 360 - self.direction

    def paddle_bounce(self):
        # # Right paddle collision
        # if self.direction < 90:
        #     self.direction = 180 - self.direction
        # elif self.direction > 270:
        #     self.direction = 180 + (360 - self.direction)

        # # Left paddle collision
        # elif self.direction > 90 and self.direction < 180:
        #     self.direction = 180 - self.direction
        # elif self.direction < 180 and self.direction > 270:
        #     self.direction = 360 - (self.direction - 180)

        if self.direction < 180:
            self.direction = 180 - self.direction
        elif self.direction > 180:
            self.direction = 180 + 360 - self.direction

        self.acceleration += 5

    def reset_position(self, x_coor):
        if x_coor > 0:
            self.direction = random.randrange(91, 269)
        else:
            self.direction = random.choice((random.randrange(1, 89), random.randrange(271, 359)))
        
        self.setpos(0, 0)
        self.acceleration = 0
