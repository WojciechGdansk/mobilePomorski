from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from email_validator import validate_email, EmailNotValidError
from database_connection.database_queries import QueriesToDB


class SettingsScreen(Screen):
    def on_kv_post(self, base_widget):
        super(SettingsScreen, self).on_kv_post(base_widget)
        self.pre_load()

    def pre_load(self):
        emails_in_db = QueriesToDB.load_from_db()
        if emails_in_db:
            sender, receiver = emails_in_db
            self.ids.from_email_address.text = sender
            self.ids.to_email_address.text = receiver

    def save_email_details(self):
        from_email_text = self.ids.from_email_address.text
        to_email_text = self.ids.to_email_address.text
        QueriesToDB(from_email_text, to_email_text).save_to_db()
        if self.email_validator(from_email_text) and self.email_validator(to_email_text):
            MDApp.get_running_app().root.current = "StartScreen"
        if not self.email_validator(from_email_text):
            self.ids.from_email_address.error = True
            self.ids.from_email_address.helper_text = "Niepoprawny adres email"
        if not self.email_validator(to_email_text):
            self.ids.to_email_address.error = True
            self.ids.to_email_address.helper_text = "Niepoprawny adres email"

    @staticmethod
    def email_validator(sender_email_address):
        try:
            validate_email(sender_email_address)
            return True
        except EmailNotValidError:
            return False
