from kivy.uix.screenmanager import Screen
from kivymd.uix.pickers import MDDatePicker
import re


class MatchInfoScreen(Screen):
    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        '''
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;
        :param value: selected date;
        :type value: <class 'datetime.date'>;
        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        '''

        print(instance, value, date_range)
        print('----')
        print(value)
        self.ids.selected_date.text = str(value)

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''

    def save_data(self):
        pattern = "([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))"
        selected_date = self.ids.selected_date.text
        home_team = self.ids.home_team.text
        home_team = home_team.strip()
        away_team = self.ids.away_team.text
        away_team = away_team.strip()
        if not re.match(pattern, selected_date):
            self.ids.selected_date.text = "Nieprawidłowa data"
        elif not home_team:
            self.ids.home_team.text = home_team
            self.ids.home_team.helper_text = "Nieprawidłowa drużyna"
        elif not away_team:
            self.ids.away_team.text = away_team
            self.ids.away_team.helper_text = "Nieprawidłowa drużyna"
        else:
            print("OK")
