import os
from pathlib import Path

import requests_cache
from dotenv import load_dotenv


load_dotenv()

SERPAPI_ENDPOINT = "https://serpapi.com/search"


class FlightSearch:
    """Talk to the SerpAPI Google Flights API."""

    def __init__(self):
        # FLIGHT_API_KEY keeps the freestyle .env compatible with this version.
        self._api_key = os.getenv("SERPAPI_API_KEY") or os.environ["FLIGHT_API_KEY"]
        cache_path = Path(__file__).resolve().parent / "flight_cache"
        self._session = requests_cache.CachedSession(
            cache_path,
            expire_after=3600,
        )

    def check_flights(
        self,
        origin_city_code,
        destination_city_code,
        from_time,
        to_time,
        is_direct=True,
    ):
        parameters = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time,
            "return_date": to_time,
            "type": "1",
            "adults": "1",
            "currency": os.getenv("CURRENCY", "GBP"),
            # SerpAPI: 1 means nonstop; 0 allows any number of stops.
            "stops": "1" if is_direct else "0",
            "api_key": self._api_key,
        }
        response = self._session.get(
            SERPAPI_ENDPOINT,
            params=parameters,
            timeout=30,
        )
        response.raise_for_status()
        data = response.json()

        if "error" in data:
            print(f"SerpAPI error: {data['error']}")

        return data
