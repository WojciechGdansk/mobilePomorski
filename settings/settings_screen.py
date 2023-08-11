from kivymd.app import MDApp
from kivy.lang.builder import Builder


class SettingsApp(MDApp):
    def build(self):
        return Builder.load_file('settings/settings.kv')

