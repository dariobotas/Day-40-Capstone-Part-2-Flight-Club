from datetime import datetime, timedelta

from part4.account_user import User
from part4.data_manager import DataManager
from part4.flight_search import FlightSearch
from part4.notification_manager import NotificationManager


def run():
  data_manager = DataManager()
  sheet_data = data_manager.get_destination_data
  flight_search = FlightSearch()
  notification_manager = NotificationManager()
  
  ORIGIN_CITY_IATA = "LON"

  print("Welcome to Dario's Flight Club.\nWe find the best flight deals and email you.")
  wrong_email = input("Do you want to add your email to our database? (y/n) ")
  if wrong_email == "y" or wrong_email == "Y":
    wrong_email = True
    first_name = input("What is you first name?\n")
    last_name = input("What is your last name?\n")  
    while wrong_email:
      email=input("What is your email address?\n")
      verify_email=input("Type your email again.\n")

      if email == verify_email:
        user = User(first_name, last_name, email)
        user.user_register()
        print("You're in the club!")
        wrong_email = False
      else:
        print("The emails aren't the same. Re-type the emails.")
  
  if sheet_data[0]["iataCode"] == "":
      for row in sheet_data:
          row["iataCode"] = flight_search.get_destination_code(row["city"])
      data_manager.destination_data = sheet_data
      data_manager.update_destination_codes()
  
  tomorrow = datetime.now() + timedelta(days=1)
  six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
  
  for destination in sheet_data:
    flight = flight_search.check_flights(
          ORIGIN_CITY_IATA,
          destination["iataCode"],
          from_time=tomorrow,
          to_time=six_month_from_today
    )

    if flight is None:
      continue
      
    if flight.price < destination["lowestPrice"]:
      message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

      if flight.stop_overs > 0:
        message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
        print(message)
        
      notification_manager.send_sms(message)
  