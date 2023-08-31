from kivy.uix.screenmanager import Screen
from kivy.properties import DictProperty


class FourthLeagueScreen(Screen):
    questions_dict = DictProperty({
        "Wydzielony parking dla oficjeli meczowych": "parking",
        "Regulamin meczu niebędącego imprezą masową": "statute",
        "Protokół weryfikacji boiska": "field_verified_document",
        # Add more labels and groups as needed
    })
    dupa =["adam", "karol"]
    def checkboxes(self, answer, checkbox, value):
        if value:
            print(checkbox.group)
            print(answer)
