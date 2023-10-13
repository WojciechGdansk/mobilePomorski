from kivy.uix.screenmanager import Screen
from kivymd.uix.pickers import MDDatePicker
from kivymd.app import MDApp
from form_data.match_info import MatchInfo
import re


class MatchInfoScreen(Screen):
    match_details = MatchInfo()

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
        chosen_date = self.ids.selected_date.text
        home_team = self.ids.home_team.text
        home_team = home_team.strip()
        away_team = self.ids.away_team.text
        away_team = away_team.strip()
        if self.validate_input(chosen_date, home_team, away_team):
            self.save_match_details_to_storage(home_team, away_team, chosen_date)
            self.select_next_screen()

    def validate_input(self, chosen_date, home_team, away_team):
        input_valid = True
        pattern = r"([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))"
        if not re.match(pattern, chosen_date):
            self.ids.selected_date.error = True
            self.ids.selected_date.helper_text = "Nieprawidłowa data"
            input_valid = False
        if not home_team:
            self.ids.home_team.text = home_team
            self.ids.home_team.helper_text = "Nieprawidłowa drużyna"
            input_valid = False
        if not away_team:
            self.ids.away_team.text = away_team
            self.ids.away_team.helper_text = "Nieprawidłowa drużyna"
            input_valid = False
        if input_valid:
            return True
        else:
            return False

    def save_match_details_to_storage(self, home_team, away_team, date):
        self.match_details.home_team = home_team
        self.match_details.away_team = away_team
        self.match_details.date = date

    def select_next_screen(self):
        app = MDApp.get_running_app()
        if hasattr(app, "selected_league"):
            self.match_details.league = app.selected_league
            del app.selected_league
        app.match_details = self.match_details
        if self.match_details.league == "IV Liga":
            app.root.current = "FourthLeagueScreen"
        if self.match_details.league == "Klasa Okręgowa":
            app.root.current = "RegionalLeagueScreen"
