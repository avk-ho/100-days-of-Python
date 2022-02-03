# https://www.udemy.com/course/100-days-of-code/learn/lecture/19846870#overview

# Day 15 - 

print("Hello World")

# Coffee Machine project

# Espresso - 1.50$ - 50ml Water, 18g coffee
# Latte - 2.50$ - 200ml Water, 24g coffee, 50g milk
# Cappuccino - 3.00$ - 250ml water, 24g coffee, 100ml milk

# 4 types of coins : 1 cent (penny), 5 cents (nickel), 10 cents (dime), 25 cents (quarter)

# Able to print a report with the command "report", printing the amount of ressources and money stocked

# Doesn't "store" coins, has infinite amount of coins to give back change. Does store the quantity of money given.

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def coffee_machine():

    def format_report():
        # Format the report function of the machine
        water_quantity = resources["water"]
        milk_quantity = resources["milk"]
        coffee_quantity = resources["coffee"]
        money_quantity = resources["money"]
        print(f"Water: {water_quantity}ml")
        print(f"Milk: {milk_quantity}ml")
        print(f"Coffee: {coffee_quantity}g")
        print(f"Money: ${money_quantity}")

    def calculate_total(quarters, dimes, nickels, cents):
        # Calculate the total monetary value given the number of each type of coins
        total = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (cents * 0.01)
        return total

    def recalculate_resources(command):
        # Substract the ingredients of the resources of the machine given the command
        # Also add the money from the command.
        resources["money"] += MENU[command]["cost"]

        for ingredient in MENU[command]["ingredients"]:
            resources[ingredient] -= MENU[command]["ingredients"][ingredient]
    
    has_ingredients = True
    check_command = False

    # Processing the command
    while not check_command:
        command = input("What would you like ? (espresso ($1.50)/latte ($2.50)/cappuccino ($3.00)): ")
        if command == "report":
            format_report()
        elif command == "off":
            return
        elif command in MENU:
            for ingredient in MENU[command]["ingredients"]:
                if resources[ingredient] < MENU[command]["ingredients"][ingredient]:
                    has_ingredients = False
                    print(f"Sorry, not enough {ingredient}.")
                    break
                check_command = True
        else:
            print("Wrong input.")

    # Processing the payment
    if has_ingredients:
        print("Please insert coins.")

        quarter_input = int(input("How many quarters (25 cents) ? "))
        dime_input = int(input("How many dimes (10 cents) ? "))
        nickel_input = int(input("How many nickels (5 cents) ? "))
        cent_input = int(input("How many cents (1 cent) ? "))

        total = calculate_total(quarter_input, dime_input, nickel_input, cent_input)
        if MENU[command]["cost"] > total:
            print("Sorry, that's not enough money. Money refunded.")
        else:
            change = round(total - MENU[command]["cost"], 2)
            if change != 0:
                print(f"Here is ${change} in change.")
            recalculate_resources(command)
            print(f"Here is your {command}. Enjoy !")
            #format_report()
    
    coffee_machine()
            

coffee_machine()
