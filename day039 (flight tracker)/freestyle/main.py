import os
from datetime import date, timedelta
from pathlib import Path

import requests
from dotenv import load_dotenv

from data_manager import AlertHistory, DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

BASE_DIR = Path(__file__).parent
load_dotenv(BASE_DIR / ".env")


def upcoming_weekends(count, nights=3):
    today = date.today()
    days_to_friday = (4 - today.weekday()) % 7
    first_friday = today + timedelta(days=days_to_friday or 7)
    return [(first_friday + timedelta(weeks=i),
             first_friday + timedelta(weeks=i, days=nights)) for i in range(count)]


def csv_setting(name, default):
    return tuple(v.strip().upper() for v in os.getenv(name, default).split(",") if v.strip())


def run():
    api_key = os.getenv("FLIGHT_API_KEY")
    if not api_key:
        raise RuntimeError("FLIGHT_API_KEY is missing from .env")
    dry_run = os.getenv("DRY_RUN", "true").lower() == "true"
    max_searches = int(os.getenv("MAX_SEARCHES_PER_RUN", "4"))
    max_price = float(os.getenv("MAX_PRICE_EUR", "180"))
    minimum_score = float(os.getenv("MIN_DEAL_SCORE", "0"))
    manager = DataManager(os.getenv("SHEETY"), os.getenv("SHEETY_TOKEN"),
                          csv_setting("DESTINATIONS", "BCN,MAD,FCO,CDG"))
    search = FlightSearch(api_key, os.getenv("ORIGIN", "FAO"), "EUR")
    history = AlertHistory(BASE_DIR / ".alert_history.json")
    notifier = NotificationManager(
        dry_run, os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"),
        os.getenv("TWILIO_MESSAGING_SERVICE_SID"), os.getenv("TWILIO_TO_NUMBER"))

    destinations = manager.destinations()
    all_queries = [(destination, outbound, returning)
                   for outbound, returning in upcoming_weekends(int(os.getenv("WEEKENDS_AHEAD", "4")))
                   for destination in destinations]
    queries = all_queries[:max_searches]
    print(f"FAO Weekend Escape Radar: checking {len(queries)} of {len(all_queries)} possible searches")
    candidates = []
    for destination, outbound, returning in queries:
        print(f"Checking FAO -> {destination}, {outbound} to {returning}...")
        candidates.extend(search.search_weekend(destination, outbound, returning))

    deals = sorted((f for f in candidates if f.price <= max_price and f.score >= minimum_score),
                   key=lambda f: (-f.score, f.price))
    cheapest = sorted(candidates, key=lambda f: f.price)
    if cheapest:
        print("\nCheapest fares seen:")
        for flight in cheapest[:3]:
            print(f"  {flight.origin} -> {flight.destination}: {flight.price:.0f} EUR, "
                  f"{flight.duration_label}, score {flight.score:.1f}")
    for flight in deals[:int(os.getenv("MAX_ALERTS", "3"))]:
        if history.is_new(flight):
            delivered = notifier.send(flight.alert_message())
            if delivered:
                history.remember(flight)
    if not deals:
        print(f"No deals at or below {max_price:.0f} EUR passed the score threshold.")


if __name__ == "__main__":
    try:
        run()
    except requests.RequestException:
        # Request exception strings can contain query parameters such as API keys.
        print("Flight radar error: an external service request failed")
    except (RuntimeError, ValueError) as error:
        print(f"Flight radar error: {error}")
