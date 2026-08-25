import os

import requests
from dotenv import load_dotenv

load_dotenv()


class DataManager:
    """Read and update destination prices through the Sheety API."""

    def __init__(self):
        self._prices_endpoint = (
            os.getenv("SHEETY_PRICES_ENDPOINT")
            or os.getenv("SHEETY_ENDPOINT")
            or os.getenv("SHEETY")
        )
        if not self._prices_endpoint:
            raise RuntimeError("Add SHEETY_PRICES_ENDPOINT to your .env file.")

        self._users_endpoint = os.getenv("SHEETY_USERS_ENDPOINT")
        if not self._users_endpoint:
            # A Sheety project's worksheet endpoints are siblings.
            prices_base = self._prices_endpoint.rstrip("/").rsplit("/", 1)[0]
            self._users_endpoint = f"{prices_base}/users"

        endpoint_name = self._prices_endpoint.rstrip("/").split("/")[-1]
        self._row_name = (
            endpoint_name[:-1] if endpoint_name.endswith("s") else endpoint_name
        )
        self._username = os.getenv("SHEETY_USERNAME")
        self._password = os.getenv("SHEETY_PASSWORD")
        self._token = os.getenv("SHEETY_TOKEN")

    def _request_options(self):
        if self._username and self._password:
            return {"auth": (self._username, self._password)}
        if self._token:
            return {"headers": {"Authorization": f"Bearer {self._token}"}}
        return {}

    def get_destination_data(self):
        return self._get_rows(self._prices_endpoint)

    def get_customer_emails(self):
        """Return all customer rows from the project's users worksheet."""
        return self._get_rows(self._users_endpoint)

    def _get_rows(self, endpoint):
        response = requests.get(url=endpoint, timeout=20, **self._request_options())
        response.raise_for_status()
        data = response.json()

        # The worksheet name determines Sheety's top-level response key.
        return next(value for value in data.values() if isinstance(value, list))

    def update_lowest_price(self, row_id, new_price):
        self._update_destination(row_id, {"lowestPrice": new_price})

    def update_stops(self, row_id, stops):
        """Store the number of stops for the selected cheapest flight."""
        self._update_destination(row_id, {"stops": stops})

    def _update_destination(self, row_id, fields):
        response = requests.put(
            url=f"{self._prices_endpoint}/{row_id}",
            json={self._row_name: fields},
            timeout=20,
            **self._request_options(),
        )
        if response.status_code == 403:
            raise RuntimeError(
                "Sheety refused the update. Enable PUT for the prices endpoint "
                "in the Sheety dashboard and check its authentication settings."
            )
        response.raise_for_status()
