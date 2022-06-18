# https://www.udemy.com/course/100-days-of-code/learn/lecture/21927934#overview

# Day 39

# Flight prices tracker

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
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
    if flight.price < destination_city["lowestPrice"]:
        notification_manager.send_notification(flight)
