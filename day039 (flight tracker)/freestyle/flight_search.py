import requests

from flight_data import FlightData


class FlightSearch:
    ENDPOINT = "https://serpapi.com/search.json"

    def __init__(self, api_key, origin="FAO", currency="EUR"):
        self.api_key = api_key
        self.origin = origin
        self.currency = currency

    def search_weekend(self, destination, outbound_date, return_date):
        response = requests.get(
            self.ENDPOINT,
            params={"engine": "google_flights", "api_key": self.api_key,
                    "departure_id": self.origin, "arrival_id": destination,
                    "outbound_date": outbound_date.isoformat(), "return_date": return_date.isoformat(),
                    "type": "1", "currency": self.currency, "hl": "en", "gl": "pt",
                    "adults": 1, "sort_by": 2},
            timeout=30,
        )
        response.raise_for_status()
        payload = response.json()
        if payload.get("error"):
            raise RuntimeError(f"SerpApi: {payload['error']}")
        return self._parse(payload, destination, outbound_date, return_date)

    def _parse(self, payload, destination, outbound_date, return_date):
        insights = payload.get("price_insights", {})
        typical = insights.get("typical_price_range") or []
        results = payload.get("best_flights", []) + payload.get("other_flights", [])
        flights = []
        for result in results:
            legs = result.get("flights") or []
            if not legs or result.get("price") is None:
                continue
            airlines = tuple(dict.fromkeys(leg.get("airline", "Unknown") for leg in legs))
            flights.append(FlightData(
                origin=self.origin, destination=destination, outbound_date=outbound_date,
                return_date=return_date, price=float(result["price"]), currency=self.currency,
                duration_minutes=int(result.get("total_duration", 0)), stops=max(0, len(legs) - 1),
                airlines=airlines, price_level=insights.get("price_level"),
                typical_low=float(typical[0]) if typical else None,
                booking_token=result.get("booking_token"),
            ))
        return flights
