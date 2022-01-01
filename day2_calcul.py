# https://www.udemy.com/course/100-days-of-code/learn/lecture/17841340#overview

# Day 2
# Datatypes

# Exercice sum of the digits of a two digit number

two_digit_number = input("Type a two digit number: ")

# Own code
# two_digit_number is a string type as a result of input
result = int(two_digit_number[0]) + int(two_digit_number[1])
print(result)

# Should add some security tests to verify that 1 < len(two_digit_number) < 3


# Exercice calculate BMI

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# Own code
float_weight = float(weight)
float_height = float(height)
bmi = int(float_weight/float_height**2) # Directly a whole number, does not round up or down
print(bmi)

# Exercice calculate remaining life time

age = input("What is your current age?")

# Own code
age_int = int(age)
end_of_life = 90
years_remaining = end_of_life - age_int
months_remaining = years_remaining*12
weeks_remaining = years_remaining*52
days_remaining = years_remaining*365

print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")

# Project exercice

#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator")
total_bill = float(input("What is the total bill? €"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip_multiplier = 1 + tip_percentage/100
people_nb = int(input("How many people to split the bill? "))
bill_divided = round(total_bill * tip_multiplier / people_nb, 2)
bill_final = "{:.2f}".format(total_bill) # added at the correction, 2 decimal printed
print(f"Each person should pay: €{bill_final}")