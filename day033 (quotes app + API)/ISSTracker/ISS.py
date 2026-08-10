import math
import os
import smtplib
import time
from datetime import datetime, timezone
from email.message import EmailMessage
from pathlib import Path

import requests
from dotenv import load_dotenv

# Fixed location: Lisbon. UTC is used explicitly so a web server's timezone
# cannot change the tracker's behaviour.
MY_LATITUDE = 38.7223
MY_LONGITUDE = -9.1393
SEARCH_RADIUS_KM = 1_600
CHECK_INTERVAL_SECONDS = 5

ISS_API_URL = "http://api.open-notify.org/iss-now.json"
SUN_API_URL = "https://api.sunrise-sunset.org/v2"
ENV_FILE = Path(__file__).with_name(".env")

load_dotenv(ENV_FILE)


def distance_in_km(lat_1, lon_1, lat_2, lon_2):
    """Return the great-circle distance between two coordinates."""
    earth_radius_km = 6_371.0
    lat_1, lon_1, lat_2, lon_2 = map(math.radians, (lat_1, lon_1, lat_2, lon_2))
    lat_difference = lat_2 - lat_1
    lon_difference = lon_2 - lon_1

    haversine = (
        math.sin(lat_difference / 2) ** 2
        + math.cos(lat_1) * math.cos(lat_2) * math.sin(lon_difference / 2) ** 2
    )
    return 2 * earth_radius_km * math.asin(math.sqrt(haversine))


def get_iss_position():
    """Get the point on Earth directly below the ISS."""
    response = requests.get(ISS_API_URL, timeout=10)
    response.raise_for_status()
    data = response.json()
    position = data["iss_position"]
    return float(position["latitude"]), float(position["longitude"])


class SunTimes:
    """Fetch Lisbon sunrise/sunset once per UTC date and reuse the result."""

    def __init__(self):
        self.date = None
        self.sunrise = None
        self.sunset = None

    def refresh_if_needed(self, now_utc):
        if self.date == now_utc.date():
            return

        response = requests.get(
            SUN_API_URL,
            params={
                "lat": MY_LATITUDE,
                "lng": MY_LONGITUDE,
                "date": now_utc.date().isoformat(),
                "tz": "Etc/UTC",
            },
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()
        self.sunrise = datetime.fromisoformat(data["sunrise"])
        self.sunset = datetime.fromisoformat(data["sunset"])
        self.date = now_utc.date()

    def is_night(self, now_utc):
        self.refresh_if_needed(now_utc)
        return now_utc < self.sunrise or now_utc > self.sunset


def send_iss_email(distance_km, iss_latitude, iss_longitude):
    gmail_email = os.getenv("GMAIL_EMAIL")
    gmail_password = os.getenv("GMAIL_APP_PASSWORD")
    app_name = os.getenv("GMAIL_APP_NAME", "ISS Tracker")

    if not gmail_email or not gmail_password:
        raise RuntimeError(f"Missing GMAIL_EMAIL or GMAIL_APP_PASSWORD in {ENV_FILE}.")

    message = EmailMessage()
    message["Subject"] = "Look up! The ISS is near Lisbon 🛰️"
    message["From"] = gmail_email
    message["To"] = gmail_email
    message.set_content(
        f"The ISS is approximately {distance_km:.0f} km from Lisbon's coordinates "
        "and it is currently nighttime.\n\n"
        f"ISS position: {iss_latitude:.4f}, {iss_longitude:.4f}\n"
        f"Sent by {app_name}."
    )

    with smtplib.SMTP("smtp.gmail.com", port=587, timeout=30) as server:
        server.starttls()
        server.login(gmail_email, gmail_password)
        server.send_message(message)


def run_tracker():
    sun_times = SunTimes()
    alert_sent_for_current_pass = False
    print(
        f"Watching for the ISS within {SEARCH_RADIUS_KM:,} km of Lisbon "
        f"every {CHECK_INTERVAL_SECONDS} seconds. Press Ctrl+C to stop."
    )

    while True:
        try:
            now_utc = datetime.now(timezone.utc)
            iss_latitude, iss_longitude = get_iss_position()
            distance_km = distance_in_km(
                MY_LATITUDE,
                MY_LONGITUDE,
                iss_latitude,
                iss_longitude,
            )
            night = sun_times.is_night(now_utc)
            visible_area = distance_km <= SEARCH_RADIUS_KM

            print(
                f"[{now_utc:%Y-%m-%d %H:%M:%S} UTC] "
                f"ISS distance: {distance_km:,.0f} km | "
                f"Night: {'yes' if night else 'no'}"
            )

            if night and visible_area and not alert_sent_for_current_pass:
                send_iss_email(distance_km, iss_latitude, iss_longitude)
                alert_sent_for_current_pass = True
                print("ISS alert email sent!")
            elif not (night and visible_area):
                alert_sent_for_current_pass = False

        except (requests.RequestException, KeyError, TypeError, ValueError) as error:
            print(f"API check failed: {error}")
        except (smtplib.SMTPException, OSError, RuntimeError) as error:
            print(f"Email could not be sent: {error}")

        time.sleep(CHECK_INTERVAL_SECONDS)


if __name__ == "__main__":
    try:
        run_tracker()
    except KeyboardInterrupt:
        print("\nISS tracker stopped.")
