from kivy.uix.screenmanager import Screen
from kivymd.uix.textfield import MDTextField
from form_data.form_info import RegionalLeague


class RegionalLeagueScreen(Screen):
    text_after_activating_and_deactivating_field = ''
    other_remarks_text_field = ''
    form = RegionalLeague()
    regional_league_attr = ['parking', 'statute', 'field_verified_document', 'match_info_protocol', 'club_coordinator',
                            'support_services', 'medical_point', 'stretcher', 'field_fenced', 'secured_passage']

    label_data = {
        'parking': 'Wydzielony parking dla oficjeli meczowych',
        'statute': 'Regulamin meczu niebędącego imprezą masową',
        'field_verified_document': 'Protokół weryfikacji boiska',
        'match_info_protocol': 'Informacja organizatora zawodów',
        'club_coordinator': 'Kordynator służb klubowych',
        'support_services': 'Służby porządkowo-informacyjne',
        'medical_point': 'Oznakowany punkt medyczny',
        'stretcher': 'Nosze i noszowi',
        'field_fenced': 'Ogrodzenie obszaru pola gry od widowni',
        'secured_passage': 'Zabezpieczone przejście do obszaru pola gry',
        'other_remarks': 'Inne uwagi',
    }

    other_remarks_to_add = None  # check if there is text to add as other_remarks
    other_remarks_selected = False  # check if other_remarks checkbox is selected

    def checkboxes(self, user_answer, checkbox, value):
        if value:
            if checkbox.group in self.regional_league_attr:
                setattr(self.form, checkbox.group, user_answer)

            if checkbox.group == "other_remarks" and user_answer:  # if user selected Yes in other remarks
                self.other_remarks_text_field = MDTextField(multiline=True, id="created_remarks",
                                                            text=self.text_after_activating_and_deactivating_field)
                self.ids.main_box.add_widget(self.other_remarks_text_field)
                self.other_remarks_to_add = True
                self.other_remarks_selected = True
            if checkbox.group == 'other_remarks' and not user_answer:  # if user selected No in other remarks
                self.other_remarks_selected = True
                self.remove_other_remarks_input()

        if not value and checkbox.group == 'other_remarks':
            self.other_remarks_selected = False
            self.remove_other_remarks_input()

        if not value and checkbox.group in self.regional_league_attr:
            setattr(self.form, checkbox.group, None)

    def remove_other_remarks_input(self):
        try:  # save user input in case user by mistake selected "no" in other_remarks after activating field
            self.text_after_activating_and_deactivating_field = self.other_remarks_text_field.text
            self.ids.main_box.remove_widget(self.other_remarks_text_field)

        except AttributeError:
            pass

        finally:
            self.other_remarks_to_add = False

    def save_details(self):
        if self.other_remarks_to_add:
            self.form.other_remarks = self.other_remarks_text_field.text
        elif self.other_remarks_selected:
            self.form.other_remarks = False
        else:
            self.form.other_remarks = None
        if not self.all_fields_selected():
            return self.display_not_selected_fields()
        self.erase_missing_fields_field()
        print("wsyzstkie pola ok")

    def all_fields_selected(self):
        """check if all required checkboxes are selected"""
        all_fields_except_other_remarks_selected = all(self.form.__getattribute__(attr) is not None
                                                       for attr in self.regional_league_attr)
        if self.other_remarks_selected and all_fields_except_other_remarks_selected:
            return True
        else:
            return False

    def get_not_selected_fields(self):
        """return a list of fields which haven't been selected"""
        fields_not_selected = []
        for attr in self.regional_league_attr:
            if self.form.__getattribute__(attr) is None:
                fields_not_selected.append(self.label_data[attr])
        if self.form.other_remarks is None:
            fields_not_selected.append(self.label_data['other_remarks'])
        return fields_not_selected

    def display_not_selected_fields(self):
        """display at the bottom of screen not selected fields"""
        self.erase_missing_fields_field()
        list_of_fields = self.get_not_selected_fields()
        if len(list_of_fields) > 0:
            # height of field related to width of screen
            self.ids.missing_fields_layout.height = (len(list_of_fields) / self.width) * 6000
            # for plural and singular version
            text_to_print = "Nie zaznaczono pól: " + ", ".join(list_of_fields) \
                if len(list_of_fields) > 1 else "Nie zaznaczono pola " + list_of_fields[0]
            self.ids.missing_fields.text = text_to_print

    def erase_missing_fields_field(self):
        """remove list of missing fields at the bottom of screen"""
        self.ids.missing_fields.text = ''
        self.ids.missing_fields_layout.height = 0
