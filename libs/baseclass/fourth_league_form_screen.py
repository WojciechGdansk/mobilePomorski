from kivy.uix.screenmanager import Screen
from kivymd.uix.textfield import MDTextField


class FourthLeagueScreen(Screen):
    extra_text = ''
    text_field = ''
    def checkboxes(self, answer, checkbox, value):
        if value:
            print(checkbox.group)
            print(answer)
            if checkbox.group == "other_remarks" and answer:
                self.text_field = MDTextField(multiline=True, id="created_remarks", text=self.extra_text)
                self.ids.main_box.add_widget(self.text_field)
            if checkbox.group == 'other_remarks' and not answer:
                try:
                    self.extra_text = self.text_field.text
                    self.ids.main_box.remove_widget(self.text_field)
                except AttributeError:
                    pass

