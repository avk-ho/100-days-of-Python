# https://www.udemy.com/course/100-days-of-code/learn/lecture/21096092#overview

# Day 32
# Email SMTP / Datetime module

import random
import datetime as dt
import smtplib

my_email = "email@address.com"
temp_pw = "password"

# connection = smtplib.SMTP("smtp.gmail.com") # varies depending on the email provider
# connection.starttls() # safety encryption
# connection.login(user=my_email, password=temp_pw)
# connection.sendmail(from_addr=my_email, to_addrs=my_email, msg="Subject:Hello\n\nWorld")
# connection.close()

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()  # safety encryption
#     connection.login(user=my_email, password=temp_pw)
#     connection.sendmail(from_addr=my_email,
#         to_addrs=my_email,
#         msg="Subject:Hello\n\nWorld")


# now = dt.datetime.now()
# year = now.year

# new_date = dt.datetime(year=1494, month=6, day=25)

# Exercice
# Send a mail on current day of the week (thursday)

now = dt.datetime.now()
current_day = now.weekday()
if current_day == 3:
    try:
        with open("day32/quotes.txt", "r") as quote_file:
            # quotes = quote_file.read()
            # quotes_list = quotes.split("\n")
            # print(quotes_list)
            quotes_list = quote_file.readlines()  # more efficient
    except FileNotFoundError:
        print("file not found")

    rand_quote = random.choice(quotes_list)
    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()  # safety encryption
    #     connection.login(user=my_email, password=temp_pw)
    #     connection.sendmail(from_addr=my_email,
    #                         to_addrs=my_email,
    #         msg=f"Subject:Motivational quote\n\n{rand_quote}")
