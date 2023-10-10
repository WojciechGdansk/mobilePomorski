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
        user_name = self.ids.name_and_last_name.text
        if self.email_validator(from_email_text) and self.email_validator(to_email_text) and \
                self.user_name_validator(user_name):
            # save to DB data provided by user in settings screen only if data are correct
            QueriesToDB(from_email_text, to_email_text, user_name).save_to_db()
            # when correct save to DB and go to start screen
            MDApp.get_running_app().root.current = "StartScreen"
        if not self.email_validator(from_email_text):
            self.ids.from_email_address.error = True
            self.ids.from_email_address.helper_text = "Niepoprawny adres email"
        if not self.email_validator(to_email_text):
            self.ids.to_email_address.error = True
            self.ids.to_email_address.helper_text = "Niepoprawny adres email"
        if not self.user_name_validator(user_name):
            self.ids.name_and_last_name.error = True
            self.ids.name_and_last_name.helper_text = "Błędne imię i nazwisko, wymagane przynajmniej 5 znaków"

    @staticmethod
    def email_validator(sender_email_address):
        try:
            validate_email(sender_email_address)
            return True
        except EmailNotValidError:
            return False

    @staticmethod
    def user_name_validator(user_name):
        if len(user_name) > 4:
            return True
        else:
            return False
