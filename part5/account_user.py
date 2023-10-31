import os

import requests as api

SHEETY_USERS_ENDPOINT = "https://api.sheety.co/041bc237af12575deefd9d8f485daa6f/flightDeals/users"
SHEETY_API_KEY = os.environ["SHEETY_API_KEY"]
SHEETY_APP_ID = os.environ["SHEETY_APP_ID"]

HEADERS = {
    "Authorization": f"Bearer {SHEETY_API_KEY}",
    "Content-Type": "application/json"
}


class User:
    def __init__(self):
        self.customer_data = None
        self.first_name = ""
        self.last_name = ""
        self.email = ""

    def user_register(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        user_data = {
            "user": {
                "firstName": self.first_name,
                "lastName": self.last_name,
                "email": self.email
            }
        }
        response = api.post(SHEETY_USERS_ENDPOINT, json=user_data, headers=HEADERS)
        response.raise_for_status()
        return response.text

    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = api.get(url=customers_endpoint, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        print(data)
        self.customer_data = data["users"]
        return self.customer_data