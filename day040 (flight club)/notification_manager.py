import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv

load_dotenv()


class NotificationManager:
    """Send flight-deal notifications through EMAIL."""

    def __init__(self):
        self._smtp_address = os.getenv("SMTP_ADDRESS", "smtp.gmail.com")
        self._smtp_port = int(os.getenv("SMTP_PORT", "465"))
        self._email = os.getenv("GMAIL_EMAIL") or os.getenv("EMAIL")
        self._password = os.getenv("GMAIL_APP_PASSWORD") or os.getenv("EMAIL_PASSWORD")

        if not self._email or not self._password:
            raise RuntimeError(
                "Add GMAIL_EMAIL and GMAIL_APP_PASSWORD to your .env file."
            )

    def send_emails(self, email_list, message, subject="New Low Price Flight!"):
        """Send one UTF-8 flight-deal email to every unique customer address."""
        recipients = list(dict.fromkeys(email for email in email_list if email))
        if not recipients:
            print("No customer email addresses found.")
            return

        with smtplib.SMTP_SSL(self._smtp_address, self._smtp_port) as connection:
            connection.login(self._email, self._password)
            for recipient in recipients:
                email = EmailMessage()
                email["From"] = self._email
                email["To"] = recipient
                email["Subject"] = subject
                email.set_content(message, charset="utf-8")
                connection.send_message(email)

        print(f"Sent flight alert to {len(recipients)} customer(s).")
