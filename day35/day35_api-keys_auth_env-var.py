# https://www.udemy.com/course/100-days-of-code/learn/lecture/21305194#overview

# Day 35
# API Keys / Authentification / Environment variables

import requests
import os

open_weather_api_url = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = os.environ.get("OWM_API_KEY")
weather_params = {
    "lat": 48.852825,
    "lon": 2.348562,
    "appid": API_KEY,
    "exclude": "current,minutely,daily,alerts",
    "units": "metric"
}

response = requests.get(url=open_weather_api_url, params=weather_params)
print(response.status_code)
response.raise_for_status()

weather_data = response.json()

# print(weather_data)

# list of weather condition codes
# https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2


# hourly_weather_data = weather_data["hourly"]
# for i in range(12):
#     current_hourly_data = hourly_weather_data[i]
#     current_hourly_weather_code = current_hourly_data["weather"][0]["id"]
#     print(current_hourly_weather_code)
#     if current_hourly_weather_code < 700:
#         print("Bring an umbrella.")
#         break

will_rain = False

weather_hourly_slice = weather_data["hourly"][:12]
for hourly_data in weather_hourly_slice:
    condition_code = hourly_data["weather"][0]["id"]
    print(condition_code)
    if condition_code < 700:
        will_rain = True
        break

if will_rain:
    print("Bring an umbrella.")

# checking environment variable
print(os.environ)