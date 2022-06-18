# https://sheety.co/
# doc https://sheety.co/docs/requests.html

import requests
SHEETY_API_ENDPOINT = "https://api.sheety.co/9909a027cda3ba53a56abf70da4bbc6b/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

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
