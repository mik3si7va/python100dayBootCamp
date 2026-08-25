import json
from pathlib import Path

import requests


class DataManager:
    def __init__(self, sheety_url=None, sheety_token=None, fallback_destinations=()):
        self.sheety_url = sheety_url
        self.sheety_token = sheety_token
        self.fallback_destinations = fallback_destinations

    def destinations(self):
        if not self.sheety_url:
            return list(self.fallback_destinations)
        headers = {"Authorization": f"Bearer {self.sheety_token}"} if self.sheety_token else {}
        try:
            response = requests.get(self.sheety_url, headers=headers, timeout=20)
            response.raise_for_status()
        except requests.RequestException:
            print("Sheety is unavailable; using DESTINATIONS from .env instead.")
            return list(self.fallback_destinations)
        rows = next((v for v in response.json().values() if isinstance(v, list)), [])
        codes = [str(row.get("iataCode") or row.get("iata") or "").upper() for row in rows]
        return [code for code in codes if len(code) == 3] or list(self.fallback_destinations)


class AlertHistory:
    def __init__(self, path):
        self.path = Path(path)
        try:
            self.sent = set(json.loads(self.path.read_text()))
        except (FileNotFoundError, json.JSONDecodeError):
            self.sent = set()

    def is_new(self, flight):
        return f"{flight.route_key}-{flight.price:.2f}" not in self.sent

    def remember(self, flight):
        self.sent.add(f"{flight.route_key}-{flight.price:.2f}")
        self.path.write_text(json.dumps(sorted(self.sent), indent=2))
