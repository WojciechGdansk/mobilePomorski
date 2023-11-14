from kivy.uix.screenmanager import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.app import MDApp
from form_data.form_info import FourthLeague, RegionalLeague
from word_creator.word_document_creator import CreateWord
from email_configurator.email_sending_module import Email
from user_data.user_info import User
from email_configurator.errors_handling import SendingErrors
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window


class League(Screen):
    dialog = None
    text_after_activating_and_deactivating_field = ''
    other_remarks_text_field = ''
    form: [FourthLeague, RegionalLeague] = object
    match_info = None
    # data from DB saved in app storage
    user_info: User = object
    attrs = []
    label_data = {}

    other_remarks_to_add = None  # check if there is text to add as other_remarks
    other_remarks_selected = False  # check if other_remarks checkbox is selected

    def checkboxes(self, user_answer, checkbox, value):
        if value:
            if checkbox.group in self.attrs:
                setattr(self.form, checkbox.group, user_answer)

            if checkbox.group == "other_remarks" and user_answer:  # if user selected Yes in other remarks
                self.other_remarks_text_field = MDTextField(multiline=True, id="created_remarks",
                                                            text=self.text_after_activating_and_deactivating_field,
                                                            on_focus=self.keyboard_display())
                self.ids.main_box.add_widget(self.other_remarks_text_field)
                self.other_remarks_to_add = True
                self.other_remarks_selected = True
            if checkbox.group == 'other_remarks' and not user_answer:  # if user selected No in other remarks
                self.other_remarks_selected = True
                self.remove_other_remarks_input()
        if not value and checkbox.group == 'other_remarks':
            self.other_remarks_selected = False
            self.remove_other_remarks_input()

        if not value and checkbox.group in self.attrs:
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
        if self.other_remarks_to_add:  # if other_remarks field is selected and with text
            self.form.other_remarks = self.other_remarks_text_field.text
        elif self.other_remarks_selected:  # if other_remarks field is selected but no extra text to add
            self.form.other_remarks = False
        else:  # if field other_remarks hasn't been selected at all
            self.form.other_remarks = None
        if not self.all_fields_selected():
            return self.display_not_selected_fields()
        # in case when user previously click save button field is created at the bottom with info which fields
        # haven't been selected. When user click again Save button new created field should be erased
        self.erase_missing_fields_field()
        self.get_info_from_storage()
        CreateWord(self.match_info, self.form, self.user_info.user).create_document()
        try:
            Email(self.user_info.sender, self.user_info.receiver, self.user_info.user).send_email()
            self.show_success_dialog()
        except SendingErrors as e:
            self.show_error_dialog(e)

    def all_fields_selected(self):
        """check if all required checkboxes are selected"""
        all_fields_except_other_remarks_selected = all(self.form.__getattribute__(attr) is not None
                                                       for attr in self.attrs)
        if self.other_remarks_selected and all_fields_except_other_remarks_selected:
            return True
        else:
            return False

    def get_not_selected_fields(self):
        """return a list of fields which haven't been selected"""
        fields_not_selected = []
        for attr in self.attrs:
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
            # for plural and singular version
            text_to_print = "Nie zaznaczono pól: " + ", ".join(list_of_fields) \
                if len(list_of_fields) > 1 else "Nie zaznaczono pola " + list_of_fields[0]
            self.ids.missing_fields.text = text_to_print

    def erase_missing_fields_field(self):
        """remove list of missing fields at the bottom of screen"""
        self.ids.missing_fields.text = ''

    def set_match_details(self, app: MDApp):
        """get match details object saved in memory and set as object here"""
        if hasattr(app, "match_details"):
            self.match_info = app.match_details
            del app.match_details

    def set_user_object(self, app: MDApp):
        """get username saved in memory and set as variable"""
        if hasattr(app, 'info_from_db'):
            self.user_info = app.info_from_db
            del app.info_from_db

    def get_info_from_storage(self):
        """run methods to get necessary info from app memory"""
        app = MDApp.get_running_app()
        self.set_match_details(app)
        self.set_user_object(app)

    def show_success_dialog(self):
        self.dialog = MDDialog(
            text="Wysłano",
            buttons=[MDFlatButton(text="Wyjdź", on_release=self.close_dialog)]
        )
        self.dialog.open()

    def show_error_dialog(self, error_text):
        self.dialog = MDDialog(
            text=f"{error_text}",
            buttons=[MDFlatButton(text="Wyjdź", on_release=self.close_dialog)]
        )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()
        app = MDApp.get_running_app()
        app.root.current = "StartScreen"

    def keyboard_display(self):
        Window.softinput_mode = "below_target"
