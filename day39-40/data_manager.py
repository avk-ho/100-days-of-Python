# https://sheety.co/
# doc https://sheety.co/docs/requests.html

import requests
from flight_search import FlightSearch

SHEETY_API_KEY = "API_KEY"
SHEETY_API_ENDPOINT = f"https://api.sheety.co/{SHEETY_API_KEY}/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    # def add_destination_data(self, city_name, lowest_price):
    #     flight_search = FlightSearch()
    #     iata_code = flight_search.get_destination_code(city_name)
    #     params = {
    #         "price": {
    #             "city": city_name,
    #             "iataCode": iata_code,
    #             "lowestPrice": str(lowest_price)
    #         }
    #     }
    #     response = requests.post(url=SHEETY_API_ENDPOINT, json=params)
        


    def get_destination_data(self):
        response = requests.get(url=SHEETY_API_ENDPOINT)
        data = response.json()
        # print(data)
        self.destination_data = data["prices"]

        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_API_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
