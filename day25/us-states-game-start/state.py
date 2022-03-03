from turtle import Turtle

class State(Turtle):
    def __init__(self, state_name, x, y) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.name = state_name

        self.setpos(x, y)
        self.write(f"{self.name}", False, "center")
    #     self.move(x, y)
    #     self.display_name()

    # def move(self, x, y):
    #     self.setpos(x, y)
        
    # def display_name(self):
    #     self.write(f"{self.name}")