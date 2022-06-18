class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_notification(self, flight_data):
        message = f"""Low price alert! Only {flight_data.price}€ to fly from {flight_data.origin_city}-{flight_data.origin_airport} to {flight_data.destination_city}-{flight_data.destination_airport}, from {flight_data.out_date} to {flight_data.return_date}."""
        print(message)
        return message
