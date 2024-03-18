from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus.para import Paragraph

from form_data.form_info import FourthLeague, RegionalLeague
from pdf_creator.other_remarks_table_data import OtherRemarksTableData


class MainTableData:
    data = {
        'parking': "Wydzielony parking dla oficjeli meczowych",
        'statute': "Regulamin meczu niebędącego imprezą masową",
        'field_verified_document': "Protokół weryfikacji boiska",
        'match_info_protocol': 'Informacja organizatora zawodów',
        'security_director': 'Kierownik ds. bezpieczeństwa (IV liga)',
        'club_coordinator': 'Kordynator służb klubowych (klasa Okręgowa)',
        'announcer': 'Spiker (IV liga)',
        'support_services': 'Służby porządkowo-informacyjne',
        'medical_point': 'Oznakowany punkt medyczny',
        'stretcher': 'Nosze i noszowi',
        'field_fenced': 'Ogrodzenie obszaru pola gry od widowni',
        'secured_passage': 'Zabezpieczone przejście do obszaru pola gry',
        'other_remarks': 'Inne uwagi',
    }

    def __init__(self, stadium_facilities: [FourthLeague, RegionalLeague]):
        self.stadium_facilities = stadium_facilities

    def table_data(self):
        styles = getSampleStyleSheet()
        bold_underline_style = styles["Normal"]

        # Define the text content
        bold_underline_text_yes = "<u>TAK</u>"
        bold_underline_text_no = "<u>NIE</u>"
        bold_underline_paragraph_yes = Paragraph(bold_underline_text_yes, bold_underline_style)
        bold_underline_paragraph_no = Paragraph(bold_underline_text_no, bold_underline_style)

        table = []
        counter = 1
        for key, value in MainTableData.data.items():
            if key == "other_remarks":
                other_remarks = OtherRemarksTableData()
                other_remarks.set_counter(counter)
                other_remarks.set_description(value)
                other_remarks.set_other_remarks(self.stadium_facilities.__getattribute__(key))
            else:
                try:
                    selected = self.stadium_facilities.__getattribute__(key)
                except AttributeError:
                    selected = None
                if selected:
                    table.append([counter, value, bold_underline_paragraph_yes, "NIE"])
                elif selected == False:
                    table.append([counter, value, "TAK", bold_underline_paragraph_no])
                else:
                    table.append([counter, value, "TAK", "NIE"])

                # add empty row
                table.append([])
                counter += 1
        return table
