# https://www.udemy.com/course/100-days-of-code/learn/lecture/17878014#overview

# Day 3
# if/elif/else

# Exercice: is even or odd

number = int(input("Which number do you want to check? "))

# Own code
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# Exercice: BMI 2.0

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

# Own code
bmi = round(weight/height**2)

if bmi > 35:
    print(f"Your BMI is {bmi}, you are clinically obese.")
elif bmi > 30:
    print(f"Your BMI is {bmi}, you are obese.")
elif bmi > 25:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi > 18.5:
    print(f"Your BMI is {bmi}, you have a normal weight.")
else:
    print(f"Your BMI is {bmi}, you are underweight.")


# Exercice: leap year calculator
# A leap year is evenly divisible by 4, 
# except if also evenly divisible by 100, 
# unless also evenly divisible by 400

year = int(input("Which year do you want to check? "))

# Own code
# Unsure which version is the clearest
# Version 1
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

# Version 2
if year % 400 == 0:
    print("Leap year.")
elif year % 4 == 0:
    if year % 100 == 0:
        print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

# Version 3
if year % 400 == 0:
    print("Leap year.")
elif year % 4 != 0:
    print("Not leap year.")
else:
    if year % 100 == 0:
        print("Not leap year.")
    else:
        print("Leap year.")


# Exercice: Pizza delivery bill calculator

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# Own code
bill = 0
if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
else:
    if size == "M":
        bill += 20
    else: # L
        bill += 25
    if add_pepperoni == "Y":
        bill += 3
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}.")

# Maybe a way to have less redundancy with the add_pepperoni variable

# Exercice: "Love calculator"

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Own code
combined_names = name1 + name2
combined_names = combined_names.lower()

true_counter = combined_names.count(
    "t") + combined_names.count("r") + combined_names.count("u") + combined_names.count("e")
love_counter = combined_names.count(
    "l") + combined_names.count("o") + combined_names.count("v") + combined_names.count("e")

true_counter = str(true_counter)
love_counter = str(love_counter)
score = true_counter + love_counter
score = int(score)

if score < 10 or 90 < score:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
