# https://www.udemy.com/course/100-days-of-code/learn/lecture/19658774#overview

# Day 10 - Functions with output

def format_name(f_name, l_name):
    formated_name = ""
    formated_name += f_name.title() + " " + l_name.title()
    
    return formated_name


# Exercice 1 - Days in month

# Starting state
# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         print("Leap year.")
#       else:
#         print("Not leap year.")
#     else:
#       print("Leap year.")
#   else:
#     print("Not leap year.")


# def days_in_month():
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Own code
# Modified from day3 code
def is_leap(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0:
        if year % 100 == 0:
            return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if is_leap(year) and month == 2:
        return month_days[month - 1] + 1
    
    return month_days[month - 1]

# Code verification
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

# Exercice project - Calculator

# Solo attempt

def calculator(n1, operation, n2):
    operations = ["+", "-", "*", "/"]

    print("+\n-\n*\n/")
    operation = input("Pick an operation: ")
    n2 = input("What's the next number? ")

    n1 = float(n1)
    n2 = float(n2)

    def add(n1, n2):
        return n1 + n2

    def sub(n1, n2):
        return n1 - n2

    def mult(n1, n2):
        return n1 * n2

    def div(n1, n2):
        return n1 / n2

    result = 0
    if operation == operations[0]:
        result = add(n1, n2)
        print(f"{n1} {operation} {n2} = {result}")
    elif operation == operations[1]:
        result = sub(n1, n2)
        print(f"{n1} {operation} {n2} = {result}")
    elif operation == operations[2]:
        result = mult(n1, n2)
        print(f"{n1} {operation} {n2} = {result}")
    elif operation == operations[3]:
        result = div(n1, n2)
        print(f"{n1} {operation} {n2} = {result}")

    while will_continue:
        will_continue_input = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if will_continue_input == "y":
            print("+\n-\n*\n/")
            operation = input("Pick an operation")
            n2 = input("What's the next number ?")
            calculator(result, operation, n2)
            break
        elif will_continue_input == "n":
            #clear()
            will_continue = False
            print("Screen cleared.")
        else:
            print("Wrong input.")

n1 = input("What's the first number? ")
print("+\n-\n*\n/")
operation = input("Pick an operation: ")
n2 = input("What's the next number? ")
calculator(n1, operation, n2)

# Correction
def calculator_correction():
    def add(n1, n2):
            return n1 + n2

    def sub(n1, n2):
        return n1 - n2

    def mult(n1, n2):
        return n1 * n2

    def div(n1, n2):
        return n1 / n2

    operations = {
        "+": add,
        "-": sub,
        "*": mult,
        "/": div,
    }

    num1 = float(input("What's the first number? "))

    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        calculation_function = operations[operation_symbol]

        num2 = float(input("What's the next number? "))
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue with {answer}, or type 'n' to exit: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()