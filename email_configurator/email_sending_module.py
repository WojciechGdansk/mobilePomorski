import requests
import os
from email_configurator.errors_handling import SendingErrors
from dotenv import load_dotenv

load_dotenv()


class Email:
    api_domain = os.getenv("API_DOMAIN")
    api_key = os.getenv("API_KEY")

    def __init__(self, sender, receiver, user_name):
        self.sender = sender
        self.receiver = receiver
        self.user_name = user_name

    def send_email(self):
        try:
            response = requests.post(
                f"https://api.mailgun.net/v3/{self.api_domain}/messages",
                auth=("api", self.api_key),
                data={"from": f"{self.user_name} <{self.sender}>",
                      "to": [f"{self.receiver}"],
                      "subject": "Hello",
                      "text": "Testing some Mailgun awesomness!"},
                files=[('attachment', ('new.docx', open('new.docx', 'rb').read()))])
            if response.status_code == 200:
                return True
            else:
                raise SendingErrors("Wystąpił błąd, spróbuj później")
        except requests.exceptions.RequestException:
            raise SendingErrors("Brak połączenia z internetem")
