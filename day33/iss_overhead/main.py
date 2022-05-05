import requests
from datetime import datetime
import smtplib

MY_LAT = 48.857394  # Your latitude
MY_LONG = 2.351549  # Your longitude
MY_EMAIL = "my@mail.com"
MY_PASSWORD = "password"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def is_in_range():
    iss_lat_in_range = iss_latitude <= (MY_LAT + 5) and iss_latitude >= (MY_LAT - 5)
    iss_long_in_range = iss_longitude <= (MY_LONG + 5) and iss_longitude >= (MY_LONG - 5)
    in_range = iss_lat_in_range and iss_long_in_range
    return in_range


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

def is_night():
    current_hour = time_now.hour
    return current_hour <= sunrise or current_hour >= sunset
# print(current_hour)

message = "Subject:ISS overhead!\n\nLook up! ISS is currently overhead."

if is_in_range() and is_night():
    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    #     connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=message)
    pass