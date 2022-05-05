# https://www.udemy.com/course/100-days-of-code/learn/lecture/21198560#overview

# Day 33
# Application Programming Interface (API)

import requests
from datetime import datetime

# iss_api = "http://api.open-notify.org/iss-now.json"

# response = requests.get(url=iss_api)
# response.raise_for_status()

# data = response.json()
# iss_position = data["iss_position"]
# print(data)

sunrise_sunset_api_url = "https://api.sunrise-sunset.org/json"

# https://www.latlong.net/
LAT = 48.857394
LNG = 2.351549

parameters = {
    "lat": LAT,
    "lng": LNG,
    "formatted": 0,
}

response = requests.get(url=sunrise_sunset_api_url, params=parameters)
response.raise_for_status()
data = response.json()
# print(data)
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

# print(sunrise.split("T")[1].split(":"))

sunrise_hour = sunrise.split("T")[1].split(":")[0]
sunset_hour = sunset.split("T")[1].split(":")[0]
