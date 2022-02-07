from turtle import Turtle
import variables as var
from car import Car

class CarManager(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.cars_list = []

    def add_car(self):
        new_car = Car()
        self.cars_list.append(new_car)

    def remove_car(self, car):
        self.cars_list.remove(car)