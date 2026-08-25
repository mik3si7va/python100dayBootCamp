import os

import requests
from dotenv import load_dotenv

load_dotenv()


class DataManager:
    """Read and update destination prices through the Sheety API."""

    def __init__(self):
        self._endpoint = os.getenv("SHEETY_ENDPOINT") or os.environ["SHEETY"]
        endpoint_name = self._endpoint.rstrip("/").split("/")[-1]
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
        response = requests.get(
            url=self._endpoint,
            timeout=20,
            **self._request_options(),
        )
        response.raise_for_status()
        data = response.json()

        # The worksheet name determines Sheety's top-level response key.
        return next(value for value in data.values() if isinstance(value, list))

    def update_lowest_price(self, row_id, new_price):
        response = requests.put(
            url=f"{self._endpoint}/{row_id}",
            json={self._row_name: {"lowestPrice": new_price}},
            timeout=20,
            **self._request_options(),
        )
        if response.status_code == 403:
            raise RuntimeError(
                "Sheety refused the update. Enable PUT for the prices endpoint "
                "in the Sheety dashboard and check its authentication settings."
            )
        response.raise_for_status()
