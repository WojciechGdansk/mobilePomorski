from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp


class FormScreen(Screen):
    def checkboxes(self, label_text, checkbox, value):
        if value:
            print(label_text)
            print('*****')
            print(value)
            MDApp.get_running_app().root.current = "MatchInfoScreen"
