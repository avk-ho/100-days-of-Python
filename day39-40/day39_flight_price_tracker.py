# https://www.udemy.com/course/100-days-of-code/learn/lecture/21927934#overview

# Day 39

# Flight prices tracker

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
from user_manager import UserManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
user_manager = UserManager()
sheet_data = data_manager.get_destination_data()

ORIGIN_CITY_CODE = "LON"

if sheet_data[0]["iataCode"] == "":
    
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    # print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

# print(sheet_data)
for destination_city in sheet_data:
    flight = flight_search.search_flight(ORIGIN_CITY_CODE, destination_city["iataCode"])
    if flight is None:
        continue
    
    if flight.price < destination_city["lowestPrice"]:
        notification_manager.send_notification(flight)

do_register_user = input("Do you want to register a new user? Type 'yes'/'no': ")
if do_register_user == "yes":
    continue_register = True
else:
    continue_register = False
while continue_register:
    user_manager.registerUser()
    continue_input = input("Do you want to add another user? Type 'no' to stop: ")
    if continue_input == "no":
        continue_register = False

# data_manager.add_destination_data("Bali", "501")