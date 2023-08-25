from kivy.uix.screenmanager import Screen
from kivymd.uix.pickers import MDDatePicker
from kivymd.app import MDApp
from form_data.match_info import MatchInfo
import re


class MatchInfoScreen(Screen):
    match_details = MatchInfo()

    def on_pre_enter(self, *args):
        app = MDApp.get_running_app()
        if hasattr(app, "selected_league"):
            self.match_details.league = app.selected_league
            del app.selected_league

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

        self.ids.selected_date.text = str(value)

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''

    def save_data(self):
        """chosen_date is taken from text input field. To text input field value is entered in on_save method"""
        pattern = "([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))"
        chosen_date = self.ids.selected_date.text
        home_team = self.ids.home_team.text
        home_team = home_team.strip()
        away_team = self.ids.away_team.text
        away_team = away_team.strip()
        if not re.match(pattern, chosen_date):
            self.ids.selected_date.error = True
            self.ids.selected_date.helper_text = "Nieprawidłowa data"
            return False
        if not home_team:
            self.ids.home_team.text = home_team
            self.ids.home_team.helper_text = "Nieprawidłowa drużyna"
            return False
        if not away_team:
            self.ids.away_team.text = away_team
            self.ids.away_team.helper_text = "Nieprawidłowa drużyna"
            return False

        self.save_match_details_to_storage(home_team, away_team, chosen_date)

    def save_match_details_to_storage(self, home_team, away_team, date):
        self.match_details.home_team = home_team
        self.match_details.away_team = away_team
        self.match_details.date = date
        app = MDApp.get_running_app()
        app.match_details = self.match_details
