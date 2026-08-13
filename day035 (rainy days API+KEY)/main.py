import requests
from dotenv import load_dotenv
import os
from pathlib import Path

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
ENV_FILE = Path(__file__).with_name(".env")

load_dotenv(ENV_FILE)

api_key = os.getenv("WEATHER_API_KEY")

# print(api_key)

weather_params = {
    "lat": os.getenv("MY_LAT"),
    "lon": os.getenv("MY_LON"),
    "appid": api_key,
    "units": "metric",
    "cnt": 12,
}

res = requests.get(OWM_ENDPOINT, params=weather_params)

res.raise_for_status()

# print(res.request.url)

# print(res.status_code)
# print(res.json())

list = res.json()["list"]

rainy = False

for item in list:
    weather_list = item["weather"]
    for weather in weather_list:
        print(weather["id"])
        if weather["id"] < 700:
            rainy = True
            break

print(rainy)


def send_sms():
    from twilio.rest import Client

    account_sid = os.getenv("MY_ACCOUNT")
    auth_token = os.getenv("MY_AUTH")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        messaging_service_sid=os.getenv("MY_SID"),
        body="It is going to rain today. Remember to bring an umbrella ☔️",
        to=os.getenv("MY_PERSONAL_NUMBER"),
    )
    print(message.sid)


if rainy:
    send_sms()
