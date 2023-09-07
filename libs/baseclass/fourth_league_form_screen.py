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
    other_remarks_selected = None

    def checkboxes(self, user_answer, checkbox, value):
        if value:

            if checkbox.group in self.forth_league_attr:
                setattr(self.form, checkbox.group, user_answer)

            if checkbox.group == "other_remarks" and user_answer:
                self.other_remarks_text_field = MDTextField(multiline=True, id="created_remarks",
                                                            text=self.text_after_activating_and_deactivating_field)
                self.ids.main_box.add_widget(self.other_remarks_text_field)
                self.other_remarks_selected = True
            if checkbox.group == 'other_remarks' and not user_answer:
                try:  # save user input in case user by mistake selected "no" in other_remarks after activating field
                    self.text_after_activating_and_deactivating_field = self.other_remarks_text_field.text
                    self.ids.main_box.remove_widget(self.other_remarks_text_field)

                except AttributeError:
                    pass

                finally:
                    self.other_remarks_selected = False

    def save_details(self):
        if self.other_remarks_selected:
            self.form.other_remarks = self.other_remarks_text_field.text
        else:
            self.form.other_remarks = None
        print(self.form.parking)
        print(self.form.statute)
        print(self.form.other_remarks)
