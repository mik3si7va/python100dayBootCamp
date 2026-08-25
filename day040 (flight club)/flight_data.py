class FlightData:
    """A single cheapest round-trip flight returned by the search API."""

    def __init__(
        self, price, origin_airport, destination_airport, out_date, return_date, stops=0
    ):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops


def find_cheapest_flight(data, return_date):
    """Combine SerpAPI's result groups and return their cheapest valid flight."""
    flight_results = data.get("best_flights", []) + data.get("other_flights", [])

    if not flight_results:
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    cheapest_flight = None
    for flight in flight_results:
        try:
            price = flight["price"]
            legs = flight["flights"]
            candidate = FlightData(
                price=price,
                origin_airport=legs[0]["departure_airport"]["id"],
                destination_airport=legs[-1]["arrival_airport"]["id"],
                out_date=legs[0]["departure_airport"]["time"].split(" ")[0],
                return_date=return_date,
                stops=len(legs) - 1,
            )
        except (KeyError, IndexError, TypeError):
            continue

        if cheapest_flight is None or candidate.price < cheapest_flight.price:
            cheapest_flight = candidate

    return cheapest_flight or FlightData("N/A", "N/A", "N/A", "N/A", "N/A")
