import os

from dotenv import load_dotenv
from twilio.rest import Client


load_dotenv()


class NotificationManager:
    """Send flight-deal notifications through Twilio."""

    def __init__(self):
        self._sid = os.getenv("TWILIO_SID") or os.environ["TWILIO_ACCOUNT_SID"]
        self._auth_token = os.environ["TWILIO_AUTH_TOKEN"]
        self._from_number = os.getenv("TWILIO_VIRTUAL_NUMBER")
        self._to_number = os.getenv("TWILIO_VERIFIED_NUMBER") or os.environ["TWILIO_TO_NUMBER"]
        self._messaging_service_sid = os.getenv("TWILIO_MESSAGING_SERVICE_SID")
        self._client = Client(self._sid, self._auth_token)

    def send_sms(self, message_body):
        message_options = {"body": message_body, "to": self._to_number}
        if self._messaging_service_sid:
            message_options["messaging_service_sid"] = self._messaging_service_sid
        else:
            message_options["from_"] = self._from_number

        message = self._client.messages.create(**message_options)
        print(message.status)

    def send_whatsapp(self, message_body):
        message = self._client.messages.create(
            body=message_body,
            from_=f"whatsapp:{os.environ['TWILIO_WHATSAPP_NUMBER']}",
            to=f"whatsapp:{self._to_number}",
        )
        print(message.status)
