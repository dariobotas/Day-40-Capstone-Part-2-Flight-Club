import os

import requests as api

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/041bc237af12575deefd9d8f485daa6f/flightDeals/users"
SHEETY_API_KEY = os.environ["SHEETY_API_KEY"]
SHEETY_APP_ID = os.environ["SHEETY_APP_ID"]

HEADERS = {
  "Authorization": f"Bearer {SHEETY_API_KEY}",
  "Content-Type": "application/json"
}

class User:
  def __init__(self, first_name, last_name, email):
    self.first_name=first_name
    self.last_name=last_name
    self.email=email

  def user_register(self):
    user_data = {
      "user" : {
        "firstName": self.first_name,
        "lastName": self.last_name,
        "email": self.email
      }
    }
    response = api.post(SHEETY_PRICES_ENDPOINT, json=user_data, headers=HEADERS)
    response.raise_for_status()
    return response.text