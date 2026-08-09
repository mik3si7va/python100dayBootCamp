import os
import random
import smtplib
from pathlib import Path

from dotenv import load_dotenv

ENV_FILE = Path(__file__).with_name(".env")
load_dotenv(ENV_FILE)

gmail_email = os.getenv("GMAIL_EMAIL")
gmail_app_password = os.getenv("GMAIL_APP_PASSWORD")
gmail_app_name = os.getenv("GMAIL_APP_NAME", "birthdayEmailApp")

if not gmail_email or not gmail_app_password:
    raise RuntimeError(
        f"Missing Gmail credentials. Add GMAIL_EMAIL and GMAIL_APP_PASSWORD to {ENV_FILE}."
    )

# with smtplib.SMTP("smtp.gmail.com", port=587) as server:
#     server.starttls()
#     server.login(user=gmail_email, password=gmail_app_password)
#     server.sendmail(
#         gmail_email, gmail_email, "Subject: Birthday Wishes\n\nHappy birthday!"
#     )
# print(f"Connected to Gmail for {gmail_app_name}.")


import datetime as dt

now = dt.datetime.now()
# print(now)
# print(now.year)
# print(now.month)
# print(now.day)
from pathlib import Path

# load quotes.txt (one quote per line) into a dict using absolute path
quotes_path = Path(__file__).with_name("quotes.txt").resolve()
quotes_dict = {}
with open(quotes_path, "r") as f:
    quotes_dict = {i: line.strip() for i, line in enumerate(f.readlines())}

# print(f"Loaded {len(quotes_dict)} quotes from {quotes_path}.")
# print(quotes_dict)


from email.message import EmailMessage

# quote = random.choice(list(quotes_dict.values()))
# message = EmailMessage()
# message["Subject"] = "Have a great day!"
# message["From"] = gmail_email
# message["To"] = gmail_email
# message.set_content(f"Quote of the day: {quote}")

# today = now.weekday()

# if now.weekday() == today:  # today
#     print(f"Quote of the day: {quote}")
#     with smtplib.SMTP("smtp.gmail.com", port=587) as server:
#         server.starttls()
#         server.login(user=gmail_email, password=gmail_app_password)
#         server.sendmail(
#             gmail_email,
#             gmail_email,
#             message.as_string(),
#         )


import pandas as pd

df = pd.read_csv(Path(__file__).with_name("birthdays.csv").resolve())
# extract dataframe rows into dictionaries for easy lookup
# by name and by (month, day)
birthdays_dict_by_name = {}
birthdays_by_date = {}  # (month, day) -> list of entries
for _, row in df.iterrows():
    entry = {
        "name": row.get("name") if "name" in row.index else None,
        "email": row.get("email") if "email" in row.index else None,
        "year": (
            int(row.get("year"))
            if "year" in row.index and not pd.isna(row.get("year"))
            else None
        ),
        "month": (
            int(row.get("month"))
            if "month" in row.index and not pd.isna(row.get("month"))
            else None
        ),
        "day": (
            int(row.get("day"))
            if "day" in row.index and not pd.isna(row.get("day"))
            else None
        ),
    }
    name = entry["name"]
    if name:
        birthdays_dict_by_name[name] = entry
    key = (entry["month"], entry["day"])
    birthdays_by_date.setdefault(key, []).append(entry)

# example variables available for later use:
# birthdays_dict_by_name, birthdays_by_date

# print(birthdays_dict_by_name)
# print(birthdays_by_date)

# today's birthdays
todays_birthdays = birthdays_by_date.get((now.month, now.day), [])

# print(todays_birthdays)
letters_path = Path(__file__).with_name("letter_templates").resolve()
letters = {}
for letter_file in letters_path.glob("letter_*.txt"):
    letter_name = letter_file.name[7:-4]  # extract the number from letter_#.txt
    with open(letter_file, "r") as f:
        letters[letter_name] = f.read()


# print(letters["1"])  # letter_1.txt

for birthday_entry in todays_birthdays:
    name = birthday_entry["name"]
    email = birthday_entry["email"]
    year = birthday_entry["year"]
    age = now.year - year if year else None
    letter_template = random.choice(list(letters.values()))
    message = EmailMessage()
    message["Subject"] = f"Happy Birthday, {name}!"
    message["From"] = gmail_email
    message["To"] = email
    message.set_content(
        letter_template.replace("[NAME]", name).replace(
            "[AGE]", str(age) if age else ""
        )
    )
    with smtplib.SMTP("smtp.gmail.com", port=587) as server:
        server.starttls()
        server.login(user=gmail_email, password=gmail_app_password)
        server.sendmail(
            gmail_email,
            email,
            message.as_string(),
        )

# check your email inbox for the birthday emails sent today.
print("Birthday emails sent!")
