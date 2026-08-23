import os
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


ENDPOINT = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
ENV_FILE = Path(__file__).with_name(".env")

WEIGHT_KG = 90
HEIGHT_CM = 170
AGE = 32
GENDER = "male"
MAX_QUERY_LENGTH = 50

QUERY_GUIDE = """
Exercise Query Guidelines
-------------------------
Maximum: 50 characters. Enter one activity at a time.

Supported activities:
  - Running/Jogging: "ran for 30 minutes", "jogged 2 miles"
  - Swimming:        "swam for 1 hour", "swimming laps"
  - Walking:         "walked 3 miles", "brisk walk 45 min"
  - Cycling:         "biked for 1 hour", "rode bike 10 miles"
  - Weightlifting:   "lifted weights 45 min", "weight training"

Tip: Include a duration, such as "30 min" or "1 hour", for a more
accurate calorie estimate. Enter q when you are finished.
"""


def get_credentials():
    """Load the Nutrition API credentials without exposing them in the code."""
    load_dotenv(ENV_FILE)

    app_id = os.getenv("X_APP_ID")
    app_key = os.getenv("X_APP_KEY")

    if not app_id or not app_key:
        raise RuntimeError(
            "Missing X_APP_ID or X_APP_KEY. Add both values to the Day 38 .env file."
        )

    return app_id, app_key


def get_sheet_credentials():
    load_dotenv(ENV_FILE)
    sheet_endpoint = os.getenv("SHEETY")
    sheet_token = os.getenv("SHEETY_TOKEN")

    if not sheet_endpoint:
        raise RuntimeError("Missing SHEETY. Add your Sheety endpoint to the .env file.")
    if not sheet_token:
        raise RuntimeError(
            "Missing SHEETY_TOKEN. Add your Sheety bearer token to the .env file."
        )

    return sheet_endpoint, sheet_token


def get_exercise_data(exercise_description):
    app_id, app_key = get_credentials()

    headers = {
        "Content-Type": "application/json",
        "x-app-id": app_id,
        "x-app-key": app_key,
    }
    data = {
        "query": exercise_description,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE,
        "gender": GENDER,
    }

    response = requests.post(ENDPOINT, headers=headers, json=data, timeout=30)
    response.raise_for_status()
    return response.json()


def add_exercise_to_sheet(exercise):
    now = datetime.now()
    sheet_endpoint, sheet_token = get_sheet_credentials()
    resource_name = urlparse(sheet_endpoint).path.rstrip("/").split("/")[-1]
    sheet_row = {
        resource_name: {
            "date": now.strftime("%d/%m/%Y"),
            "time": now.strftime("%H:%M:%S"),
            "exercise": exercise.get("name", "Unknown exercise").title(),
            "duration": exercise.get("duration_min", 0),
            "calories": exercise.get("nf_calories", 0),
        }
    }

    response = requests.post(
        sheet_endpoint,
        headers={"Authorization": f"Bearer {sheet_token}"},
        json=sheet_row,
        timeout=30,
    )
    response.raise_for_status()
    return response.json()


def main():
    print(QUERY_GUIDE)

    while True:
        exercise_description = input("Which exercise did you do? ").strip()

        if exercise_description.lower() == "q":
            print("Workout tracking finished.")
            break

        if not exercise_description:
            print("Please enter an exercise, or q to quit.\n")
            continue

        if len(exercise_description) > MAX_QUERY_LENGTH:
            print(
                f"That description is {len(exercise_description)} characters. "
                f"Please keep it under {MAX_QUERY_LENGTH}.\n"
            )
            continue

        try:
            result = get_exercise_data(exercise_description)
        except requests.RequestException as error:
            print(f"The exercise API request failed: {error}\n")
            continue
        except RuntimeError as error:
            print(error)
            break

        exercises = result.get("exercises", [])
        if not exercises:
            print("No exercise recognized. Try describing it differently.\n")
            continue

        for exercise in exercises:
            name = exercise.get("name", "Unknown exercise").title()
            duration = exercise.get("duration_min", "unknown")
            calories = exercise.get("nf_calories", "unknown")
            print(f"{name}: {duration} minutes, {calories} calories")

            try:
                add_exercise_to_sheet(exercise)
            except requests.RequestException as error:
                print(f"Could not add {name} to Google Sheets: {error}")
            except RuntimeError as error:
                print(error)
                break
            else:
                print(f"Added {name} to Google Sheets.")
        print()


if __name__ == "__main__":
    main()
