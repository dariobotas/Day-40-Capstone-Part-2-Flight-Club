from datetime import datetime, timedelta

from part5.account_user import User
from part5.data_manager import DataManager
from part5.flight_search import FlightSearch
from part5.notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LON"

def run():
    global user
    data_manager = DataManager()
    flight_search = FlightSearch()
    notification_manager = NotificationManager()

    sheet_data = data_manager.get_destination_data()

    print("Welcome to Dario's Flight Club.\nWe find the best flight deals and email you.")
    wrong_email = input("Do you want to add your email to our database? (y/n) ")
    if wrong_email == "y" or wrong_email == "Y":
        wrong_email = True
        first_name = input("What is you first name?\n")
        last_name = input("What is your last name?\n")
        while wrong_email:
            email = input("What is your email address?\n")
            verify_email = input("Type your email again.\n")

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

    destinations = {
        data["iataCode"]: {
            "id": data["id"],
            "city": data["city"],
            "price": data["lowestPrice"]
        } for data in sheet_data}

    tomorrow = datetime.now() + timedelta(days=1)
    six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

    for destination_code in destinations:
        flight = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination_code,
            from_time=tomorrow,
            to_time=six_month_from_today
        )

        if flight is None:
            continue

        if flight.price < destinations[destination_code]["price"]:
            users = user.get_customer_emails()
            emails = [row["email"] for row in users]

            message = (
                f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} "
                f"to {flight.destination_city}-{flight.destination_airport}, "
                f"from {flight.out_date} to {flight.return_date}.")

            if flight.stop_overs > 0:
                message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
                print(message)

            notification_manager.send_emails(emails, message)