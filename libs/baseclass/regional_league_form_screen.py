from form_data.form_info import RegionalLeague
from libs.baseclass.leagues import League


class RegionalLeagueScreen(League):
    form = RegionalLeague()
    attrs = ['parking', 'statute', 'field_verified_document', 'match_info_protocol', 'club_coordinator',
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
