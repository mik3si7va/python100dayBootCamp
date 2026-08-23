import os
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
from dotenv import load_dotenv
from twilio.rest import Client

ALPHA_VANTAGE_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
ENV_FILE = Path(__file__).with_name(".env")

# Add more companies later. Each one costs one Alpha Vantage request per run.
WATCHLIST = {
    "TSLA": "Tesla Inc",
    "NVDA": "NVIDIA Corporation",
    "AAPL": "Apple Inc",
}

load_dotenv(ENV_FILE)

STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
ALERT_THRESHOLD = float(os.getenv("ALERT_THRESHOLD", "5"))
DRY_RUN = os.getenv("DRY_RUN", "true").lower() == "true"


def check_required_settings():
    """Fail early with a helpful message when a setting is missing."""
    required = {"STOCK_API_KEY": STOCK_API_KEY, "NEWS_API_KEY": NEWS_API_KEY}

    if not DRY_RUN:
        required.update(
            {
                "TWILIO_ACCOUNT_SID": os.getenv("TWILIO_ACCOUNT_SID"),
                "TWILIO_AUTH_TOKEN": os.getenv("TWILIO_AUTH_TOKEN"),
                "TWILIO_MESSAGING_SERVICE_SID": os.getenv(
                    "TWILIO_MESSAGING_SERVICE_SID"
                ),
                "TWILIO_TO_NUMBER": os.getenv("TWILIO_TO_NUMBER"),
            }
        )
    missing = [name for name, value in required.items() if not value]

    if missing:
        raise RuntimeError(f"Missing settings in .env: {', '.join(missing)}")


def get_price_change(symbol):
    """Return the two latest trading closes and their percentage change."""
    response = requests.get(
        ALPHA_VANTAGE_ENDPOINT,
        params={
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "outputsize": "compact",
            "apikey": STOCK_API_KEY,
        },
        timeout=20,
    )
    response.raise_for_status()
    data = response.json()

    if "Time Series (Daily)" not in data:
        api_message = (
            data.get("Note") or data.get("Information") or data.get("Error Message")
        )
        raise RuntimeError(
            f"Alpha Vantage could not return {symbol}: {api_message or data}"
        )

    daily_prices = data["Time Series (Daily)"]
    latest_dates = sorted(daily_prices, reverse=True)[:2]
    if len(latest_dates) < 2:
        raise RuntimeError(f"Not enough trading data returned for {symbol}")

    latest_date, previous_date = latest_dates
    latest_close = float(daily_prices[latest_date]["4. close"])
    previous_close = float(daily_prices[previous_date]["4. close"])
    percentage_change = ((latest_close - previous_close) / previous_close) * 100

    return {
        "latest_date": latest_date,
        "previous_date": previous_date,
        "latest_close": latest_close,
        "previous_close": previous_close,
        "percentage_change": percentage_change,
    }


def get_drama_level(percentage_change):
    change = abs(percentage_change)
    if change >= 10:
        return "🤯 WHAT HAPPENED?!"
    if change >= 5:
        return "🚨 Market drama!"
    if change >= 2:
        return "👀 Something is stirring"
    return "😴 Nothing to see here"


def get_company_news(company_name, oldest_date, newest_date):
    """Get three relevant English articles from the price-change window."""
    response = requests.get(
        NEWS_ENDPOINT,
        headers={"X-Api-Key": NEWS_API_KEY},
        params={
            "q": f'"{company_name}"',
            "searchIn": "title,description",
            "from": oldest_date,
            "to": newest_date,
            "language": "en",
            "sortBy": "relevancy",
            "pageSize": 3,
        },
        timeout=20,
    )
    response.raise_for_status()
    data = response.json()

    if data.get("status") != "ok":
        raise RuntimeError(f"NewsAPI error: {data.get('message', 'unknown error')}")

    return data["articles"]


def build_message(symbol, price_data, article):
    change = price_data["percentage_change"]
    arrow = "🔺" if change >= 0 else "🔻"
    source = article.get("source", {}).get("name", "Unknown source")
    brief = article.get("description") or "No description available."

    return (
        f"{get_drama_level(change)}\n\n"
        f"{symbol} {arrow} {abs(change):.2f}%\n"
        f"${price_data['previous_close']:.2f} → ${price_data['latest_close']:.2f}\n\n"
        f"📰 {article['title']}\n"
        f"{source}\n\n"
        f"Brief: {brief}\n"
        f"Link: {article['url']}"
    )


def deliver_message(message):
    """Print during development; send through Twilio when DRY_RUN is false."""
    if DRY_RUN:
        print(f"\n{'=' * 60}\n{message}")
        return

    client = Client(
        os.getenv("TWILIO_ACCOUNT_SID"),
        os.getenv("TWILIO_AUTH_TOKEN"),
    )
    sent_message = client.messages.create(
        messaging_service_sid=os.getenv("TWILIO_MESSAGING_SERVICE_SID"),
        body=message,
        to=os.getenv("TWILIO_TO_NUMBER"),
    )
    print(f"Sent Twilio message {sent_message.sid}")


def run_drama_detector():
    check_required_settings()
    print(f"Stock Drama Detector — {datetime.now(timezone.utc):%Y-%m-%d %H:%M UTC}")

    for position, (symbol, company_name) in enumerate(WATCHLIST.items()):
        # Alpha Vantage's free tier allows one request per second.
        if position > 0:
            time.sleep(1.1)

        price_data = get_price_change(symbol)
        change = price_data["percentage_change"]
        print(f"{symbol}: {change:+.2f}% — {get_drama_level(change)}")

        if abs(change) < ALERT_THRESHOLD:
            continue

        articles = get_company_news(
            company_name,
            price_data["previous_date"],
            price_data["latest_date"],
        )

        if not articles:
            deliver_message(
                f"{symbol} moved {change:+.2f}%, but no matching news was found."
            )
            continue

        for article in articles:
            deliver_message(build_message(symbol, price_data, article))


if __name__ == "__main__":
    try:
        run_drama_detector()
    except (requests.RequestException, RuntimeError) as error:
        print(f"Drama Detector error: {error}")
