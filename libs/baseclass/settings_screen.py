from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from email_validator import validate_email, EmailNotValidError


class SettingsScreen(Screen):
    def on_kv_post(self, base_widget):
        super(SettingsScreen, self).on_kv_post(base_widget)
        self.pre_load()

    def pre_load(self):
        self.ids.from_email_address.text = "aaa@op.pl"

    def save_email_details(self):
        from_email_text = self.ids.from_email_address.text
        to_email_text = self.ids.to_email_address.text
        print("To Email Address:", to_email_text + " " + from_email_text)
        if self.email_validator(from_email_text, to_email_text):
            MDApp.get_running_app().root.current = "StartScreen"

    @staticmethod
    def email_validator(sender_email_address, received_email_address):
        try:
            validate_email(sender_email_address)
            validate_email(received_email_address)
            return True
        except EmailNotValidError:
            return False
