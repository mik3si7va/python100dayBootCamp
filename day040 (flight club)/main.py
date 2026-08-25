import os
from datetime import datetime, timedelta

from dotenv import load_dotenv

from data_manager import DataManager
from flight_data import find_cheapest_flight
from flight_search import FlightSearch
from notification_manager import NotificationManager

load_dotenv()

ORIGIN_CITY_CODE = os.getenv("ORIGIN_CITY_CODE") or os.getenv("ORIGIN", "LHR")
CURRENCY = os.getenv("CURRENCY", "GBP")

# The API expects dates in YYYY-MM-DD format.
tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
six_months_from_today = (datetime.now() + timedelta(days=6 * 30)).strftime("%Y-%m-%d")

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
sheet_data = data_manager.get_destination_data()
customer_data = data_manager.get_customer_emails()
customer_emails = [
    customer.get("eMail") or customer.get("email") or customer.get("e-mail")
    for customer in customer_data
]

for destination in sheet_data:
    print(f"Getting direct flights for {destination['city']}...")
    flight_data = flight_search.check_flights(
        origin_city_code=ORIGIN_CITY_CODE,
        destination_city_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_today,
    )
    cheapest_flight = find_cheapest_flight(flight_data, six_months_from_today)

    if cheapest_flight.price == "N/A":
        print(
            f"No direct flight to {destination['city']}. "
            "Looking for indirect flights..."
        )
        flight_data = flight_search.check_flights(
            origin_city_code=ORIGIN_CITY_CODE,
            destination_city_code=destination["iataCode"],
            from_time=tomorrow,
            to_time=six_months_from_today,
            is_direct=False,
        )
        cheapest_flight = find_cheapest_flight(flight_data, six_months_from_today)

        if cheapest_flight.price == "N/A":
            print(f"No flights found for {destination['city']}.")
            continue

    print(f"{destination['city']}: {CURRENCY} {cheapest_flight.price}")
    data_manager.update_stops(destination["id"], cheapest_flight.stops)

    if cheapest_flight.price < destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['city']}!")
        data_manager.update_lowest_price(destination["id"], cheapest_flight.price)

        route = (
            "This is a direct flight."
            if cheapest_flight.stops == 0
            else f"This flight has {cheapest_flight.stops} stopover(s)."
        )
        message = (
            f"Low price alert! Only {CURRENCY} {cheapest_flight.price} to fly "
            f"from {cheapest_flight.origin_airport} to "
            f"{cheapest_flight.destination_airport}, from "
            f"{cheapest_flight.out_date} until {cheapest_flight.return_date}.\n"
            f"{route}"
        )
        notification_manager.send_emails(customer_emails, message)
