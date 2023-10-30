import os
from pprint import pprint

import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/041bc237af12575deefd9d8f485daa6f/flightDeals/prices"
SHEETY_API_KEY = os.environ["SHEETY_API_KEY"]
SHEETY_APP_ID = os.environ["SHEETY_APP_ID"]

HEADERS = {
  "Authorization": f"Bearer {SHEETY_API_KEY}",
  "Content-Type": "application/json"
}

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=HEADERS)
        data = response.json()
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
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data, 
              headers=HEADERS
            )
            print(response.text)
