from kivy.uix.screenmanager import Screen
from kivymd.uix.textfield import MDTextField
from form_data.form_info import FourthLeague


class FourthLeagueScreen(Screen):
    text_after_activating_and_deactivating_field = ''
    other_remarks_text_field = ''
    form = FourthLeague()
    forth_league_attr = ['parking', 'statute', 'field_verified_document', 'match_info_protocol', 'security_director',
                         'announcer', 'support_services', 'medical_point', 'stretcher', 'field_fenced',
                         'secured_passage']
    other_remarks_to_add = None  # check if there is text to add as other_remarks
    other_remarks_selected = None  # check if other_remarks checkbox is selected

    def checkboxes(self, user_answer, checkbox, value):
        if value:
            if checkbox.group in self.forth_league_attr:
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
            self.other_remarks_selected = None
            self.remove_other_remarks_input()

        if not value and checkbox.group in self.forth_league_attr:
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
        else:
            self.form.other_remarks = None
        self.check_all_fields_are_checked()

    def check_all_fields_are_checked(self):
        all_fields_except_other_remarks_selected = all(self.form.__getattribute__(attr) is not None
                                                       for attr in self.forth_league_attr)
        other_remarks_selected = self.other_remarks_selected is not None
        if other_remarks_selected and all_fields_except_other_remarks_selected:
            return True
        else:
            return False
