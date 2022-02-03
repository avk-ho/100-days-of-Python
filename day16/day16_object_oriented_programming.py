# https://www.udemy.com/course/100-days-of-code/learn/lecture/19911792#overview

# Day 16 - Object oriented programming

# import turtle # from turtle import Turtle

# timmy = turtle.Turtle() # Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("blue")
# timmy.forward(100)

# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# python -m pip install prettytable # in console
# from prettytable import PrettyTable

# table = PrettyTable()
# table.add_column("Pokémon Name", ["Pikachu", "Charmander", "Squirtle"])
# table.add_column("Type", ["Electric", "Fire", "Water"])
# table.align = "l"
# print(table)

# Coffee Machine project - OOP version

# Espresso - 1.50$ - 50ml Water, 18g coffee
# Latte - 2.50$ - 200ml Water, 24g coffee, 50g milk
# Cappuccino - 3.00$ - 250ml water, 24g coffee, 100ml milk

from tabnanny import check
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def coffee_machine():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    is_on = True
    while is_on:
        command_input = input(
            f"What would you like ? {menu.get_items()}: ")
        if command_input == "report":
            coffee_maker.report()
            money_machine.report()
        elif command_input == "off":
            is_on = False
            return
        else:
            menu.find_drink(command_input)
            command = menu.find_drink(command_input)
            if coffee_maker.is_resource_sufficient(command):
                if money_machine.make_payment(command.cost):
                    coffee_maker.make_coffee(command)

coffee_machine()