from tkinter import font
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0

        self.write_score()

    def write_score(self):
        # Writing the p1 score
        self.setpos(-100, 200)
        self.write(self.p1_score, align="center",
                   font=("Courier", 60, "normal"))

        # Writing the p2 score
        self.setpos(100, 200)
        self.write(self.p2_score, align="center",
                   font=("Courier", 60, "normal"))

    def update_score(self, x_coor):
        self.clear()

        if x_coor < 0:
            self.p2_score += 1
        else:
            self.p1_score += 1
        
        self.write_score()
        
