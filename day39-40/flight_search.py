# tequila doc https://tequila.kiwi.com/portal/docs/tequila_api/search_api

import requests
from datetime import datetime, timedelta
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "API_KEY"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        locations_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        params = {
            "term": city_name,
            "location_types": "city",
        }
        headers = {
            "apikey": TEQUILA_API_KEY
        }
        response = requests.get(url=locations_endpoint, headers=headers, params=params)
        data = response.json()["locations"]
        code = data[0]["code"]
        return code

    def search_flight(self, departure_location_code, destination_code):
        # managing dates
        current_date = datetime.now()
        from_departure_date = current_date + timedelta(days=1)
        to_departure_date = current_date + timedelta(days=(6*30))

        formatted_from_date = from_departure_date.strftime("%d/%m/%Y")
        formatted_to_date = to_departure_date.strftime("%d/%m/%Y")
        # print(formatted_from_date)
        # print(formatted_to_date)

        search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"

        headers = {
            "apikey": TEQUILA_API_KEY
        }
        currency = "EUR"

        params = {
            "fly_from": departure_location_code,
            "fly_to": destination_code,
            "date_from": formatted_from_date,
            "date_to": formatted_to_date,
            "curr": currency,
        }

        response = requests.get(
            url=search_endpoint, 
            headers=headers, 
            params=params
        )
        try:
            data = response.json()["data"][0]
            # print(data)
            
        except IndexError:
            print(f"No flight for {destination_code}.")
            params["max_stopovers"] = 1
            response = requests.get(
                url=search_endpoint,
                headers=headers,
                params=params
            )

            data = response.json()["data"][0]
            # print(data)

            flight_data = FlightData(
                price=data["price"],
                origin_city=data["cityFrom"],
                origin_airport=data["flyFrom"],
                destination_city=data["cityTo"],
                destination_airport=data["flyTo"],
                out_date=data["utc_departure"].split("T")[0],
                return_date=data["utc_arrival"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            
            return flight_data

        else:

            flight_data = FlightData(
                price=data["price"],
                origin_city=data["cityFrom"],
                origin_airport=data["flyFrom"],
                destination_city=data["cityTo"],
                destination_airport=data["flyTo"],
                out_date=data["utc_departure"].split("T")[0],
                return_date=data["utc_arrival"].split("T")[0],
            )

            # print(f"{flight_data.destination_city}: {flight_data.price}€")
            return flight_data


fs = FlightSearch()
fs.search_flight("LON", "BER")
