from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from database_connection.database_queries import QueriesToDB
from user_data.user_info import User


class StartScreen(Screen):
    dialog = None

    def check_whether_settings_set(self):
        emails_in_db = QueriesToDB.load_from_db()
        if emails_in_db:
            sender, receiver, user_name = emails_in_db
            data_from_db = User()
            data_from_db.sender = sender
            data_from_db.receiver = receiver
            data_from_db.user = user_name
            app = MDApp.get_running_app()
            app.info_from_db = data_from_db
            app.root.current = "FormScreen"
        else:
            self.show_alert_dialog()

    def show_alert_dialog(self):
        self.dialog = MDDialog(
            text="Brak ustawień, skonfiguruj zanim wypełnisz formularz",
            buttons=[MDFlatButton(text="Zamknij okno", on_release=self.close_dialog)]
        )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()
