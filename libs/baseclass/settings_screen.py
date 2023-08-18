from kivy.uix.screenmanager import Screen


class SettingsScreen(Screen):
    def save_email_details(self):
        from_email_text = self.ids.from_email_address.text
        to_email_text = self.ids.to_email_address.text
        print("To Email Address:", to_email_text)
