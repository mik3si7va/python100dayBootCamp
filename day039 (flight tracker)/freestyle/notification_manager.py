class NotificationManager:
    def __init__(self, dry_run=True, account_sid=None, auth_token=None,
                 messaging_service_sid=None, to_number=None):
        self.dry_run = dry_run
        self.settings = (account_sid, auth_token, messaging_service_sid, to_number)

    def send(self, message):
        if self.dry_run:
            print(f"\n--- SMS PREVIEW ---\n{message}\n")
            return False
        if not all(self.settings):
            raise RuntimeError("Twilio settings are required when DRY_RUN=false")
        from twilio.rest import Client
        account_sid, auth_token, service_sid, to_number = self.settings
        sent = Client(account_sid, auth_token).messages.create(
            messaging_service_sid=service_sid, body=message, to=to_number
        )
        print(f"Sent Twilio alert {sent.sid}")
        return True
