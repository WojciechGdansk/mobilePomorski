from kivymd.app import MDApp
from kivy.lang.builder import Builder
from settings.settings_screen import SettingsApp
from kivymd.uix.button.button import MDFlatButton

class MainApp(MDApp):
    def build(self):
        return Builder.load_file('start_screen/first_screen.kv')

    def exit_func(self):
        self.stop()


    def settings_button(self):
        self.root.clear_widgets()
        # SettingsApp().run()
        # self.root.add_widget(Builder.load_file('settings/settings.kv'))



if __name__ == "__main__":
    MainApp().run()