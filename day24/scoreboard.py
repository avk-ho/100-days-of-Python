# from tkinter import font
from turtle import Turtle

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setpos(0, SCREEN_HEIGHT/2-30)
        self.score = 0
        with open("day24\data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.display_score()

    # Write and display the score
    def display_score(self):
        self.write(arg=f"Score : {self.score} | High Score : {self.high_score}", move=False,
                   align=ALIGNMENT, font=FONT)

    # Refresh the display
    def update_score(self):
        self.clear()
        self.display_score()

    # Increase the score then refresh the display
    def increase_score(self):
        self.score += 1
        self.update_score()
    
    # Display the game over
    # def game_over(self):
    #     self.setpos(0, 0)
    #     self.color("red")
    #     self.write(arg=f"GAME OVER", move=False,
    #                align=ALIGNMENT, font=FONT)
        
    # Update the high score and save it on data.txt, then update the display
    def reset_score(self):
        if self.score > self.high_score:
            with open("day24\data.txt", mode="w") as data:
                data.write(str(self.score))
            self.high_score = self.score
        
        self.score = 0
        self.update_score()