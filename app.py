from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager


class WindowManager(ScreenManager):
    pass


class MainApp(MDApp):
    def build(self):
        return Builder.load_file("libs/kvs/screen_manager.kv")

    def exit_func(self):
        self.stop()


if __name__ == "__main__":
    MainApp().run()
