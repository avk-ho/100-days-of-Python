from ast import arg
from turtle import Turtle
import variables as var

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.setpos(var.SCOREBOARD_POSITION)
        self.write_score()

    def write_score(self):
        # self.setpos(SCOREBOARD_POSITION)
        self.write(arg=f"Level {self.level}", align="left", font=var.SCORE_FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.setpos(0, 0)
        self.write(arg="GAME OVER", align="center", font=var.SCORE_FONT)