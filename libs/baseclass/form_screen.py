from kivy.uix.screenmanager import Screen


class FormScreen(Screen):
    def checkboxes(self, label_text, checkbox, value):
        if value:
            print(label_text)
            print('*****')
            print(value)
