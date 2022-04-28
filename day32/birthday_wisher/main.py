##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
import smtplib
import pandas
import datetime as dt
import random

def get_birthdays_data():
    global birthdays_data
    try:
        birthdays_data = pandas.read_csv("day32/birthday_wisher/birthdays.csv")
    except FileNotFoundError:
        print("No birthday file found.")

def create_new_birthday():
    # TO DO : add mistake checks to each input
    name_input = input("Please input the name of the recipient: ")
    mail_input = input("Please input the email address of the person: ")
    year_input = int(input("Please input the year of birth of the recipient: "))
    month_input = int(input("Please input the month of birth of the recipient: "))
    day_input = int(input("Please input the day of birth of the recipient: "))
    
    new_data = {
        "name": name_input,
        "email": mail_input,
        "year": year_input,
        "month": month_input,
        "day": day_input,
    }
    new_birthday = pandas.DataFrame(new_data, index=[0])
    new_birthday.to_csv("day32/birthday_wisher/birthdays.csv", mode="a", index=False, header=False)

    continue_input = input("Type 'stop' if you want to stop adding new recipient to the birthday list: ")
    if continue_input == "stop":
        return get_birthdays_data()
    else:
        return create_new_birthday()


add_new_birthday = input("If you want to add new birthdays, type 'y', else type 'n': ")
if add_new_birthday == "y":
    create_new_birthday()
else:
    get_birthdays_data()

# 2. Check if today matches a birthday in the birthdays.csv

def birthday_check():
    # Returns True if today matches a birthday in the csv, else returns False
    now = dt.datetime.now()
    current_date = (now.month, now.day)

    all_months = birthdays_data.month
    all_days = birthdays_data.day
    all_birthdays = zip(all_months, all_days)

    if current_date in all_birthdays:
        return True
    else:
        return False


def find_matching_birthday():
    now = dt.datetime.now()
    current_date = {
        "month": now.month, 
        "day": now.day
    }
    matching_birthday = birthdays_data.loc[(birthdays_data["month"] == current_date["month"]) & (
        birthdays_data["day"] == current_date["day"])]
    return matching_birthday

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

def pick_letter(name):
    num = random.randint(1, 3)

    with open(f"day32/birthday_wisher/letter_templates/letter_{num}.txt", "r") as letter:
        text = letter.read()
        # print(letter_text)
        new_text = text.replace("[NAME]", name)
        new_text = new_text.replace("Angela", "Avk")
        # print(new_text)

    return new_text

# 4. Send the letter generated in step 3 to that person's email address.

def send_mail(my_email, my_password, recipient_mail, text):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=recipient_mail,
                            msg=f"Subject: Happy Birthday !\n\n{text}")

if birthday_check():
    matching_birthday = find_matching_birthday()
    matching_name = matching_birthday["name"].values[0]
    matching_email = matching_birthday["email"].values[0]
    # print("name: " + matching_name)
    # print("mail: " + matching_email)
    
    new_txt = pick_letter(matching_name)

    my_email = "mail@mail.fr"
    my_password = "password"
    send_mail(my_email, my_password, matching_email, new_txt)