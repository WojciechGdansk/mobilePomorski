from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp


class FormScreen(Screen):
    def checkboxes(self, league, checkbox, value):
        if value:
            app = MDApp.get_running_app()
            app.selected_league = league  # save selected league to storage
            app.root.current = "MatchInfoScreen"

