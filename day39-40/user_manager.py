import requests

SHEETY_API_KEY = "API_KEY"
SHEETY_USERS_ENDPOINT = f"https://api.sheety.co/{SHEETY_API_KEY}/flightDeals/users"

class UserManager:
    def registerUser(self):
        print("Welcome to the Flight Club.\nWe find the best flight deals and email you.\n")
        first_name = input("What is your first name? ")
        last_name = input("What is your last name? ")
        email = input("What is your email? ")
        is_right_email = False
        
        while not is_right_email:
            repeat_email = input("Type your email again: ")
            is_right_email = email == repeat_email

        params = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
            }
        }

        response = requests.post(url=SHEETY_USERS_ENDPOINT, json=params)
        response.raise_for_status()
        # print(response)

        print("You're in the club!")