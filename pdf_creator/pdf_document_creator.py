from kivymd.app import MDApp
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.pdfbase.ttfonts import TTFont

from form_data.form_info import FourthLeague, RegionalLeague
from form_data.match_info import MatchInfo
from pdf_creator.main_table_data import MainTableData
from pdf_creator.other_remarks_table_data import OtherRemarksTableData
from pdf_creator.top_table_data import TableData

import os


class PDFDocument:
    def __init__(self, match_data_object: MatchInfo, stadium_facilities: [FourthLeague, RegionalLeague], user_name):
        self.canvas = Canvas
        self.match_data = match_data_object
        self.stadium_facilities = stadium_facilities
        self.user_name = user_name

    def create_document(self):
        self.set_filename_and_size()
        self.register_fonts()
        self.draw_text("ZAŁĄCZNIK DO SPRAWOZDANIA SĘDZIEGO LUB OBSERWATORA SĘDZIÓW")
        self.draw_top_table(TableData(self.match_data).table_info())
        self.draw_main_table(MainTableData(self.stadium_facilities).table_data())
        other_remarks = OtherRemarksTableData()
        self.draw_other_remarks_table(other_remarks.other_remarks_table_data())
        self.draw_bottom_table()
        self.save_file()

    def set_filename_and_size(self, filename="Załącznik do sprawozdania - MW.pdf") -> None:
        path = os.path.join(MDApp.get_running_app().user_data_dir, filename)
        self.canvas = Canvas(path, pagesize=A4)

    def draw_text(self, text_to_draw) -> None:
        self.canvas.setFont("Cambria Bold", 14)
        self.canvas.drawString(self.cm_to_points(2), self.cm_to_points(27), text_to_draw)

    def draw_top_table(self, data: TableData) -> None:
        col_widths_in_cm = [4.47, 4.23, 4.27, 4.23]
        col_widths_in_points = list(map(lambda x: self.cm_to_points(x), col_widths_in_cm))
        table = Table(data, colWidths=col_widths_in_points)
        table.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 1, colors.black),
                                   ('FONTNAME', (0, 0), (-1, -1), "Cambria")
                                   ]))
        table.wrapOn(self.canvas, self.cm_to_points(2), self.cm_to_points(25.2))
        table.drawOn(self.canvas, self.cm_to_points(2), self.cm_to_points(25.2))

    def draw_main_table(self, data: MainTableData):
        col_widths_in_cm = [0.94, 11.65, 2.25, 2.25]
        col_widths_in_points = list(map(lambda x: self.cm_to_points(x), col_widths_in_cm))
        table = Table(data, colWidths=col_widths_in_points)
        table.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 1, colors.black),
                                   ('FONTNAME', (0, 0), (-1, -1), "Cambria"),
                                   ]))
        table.wrapOn(self.canvas, self.cm_to_points(2), self.cm_to_points(9.2))
        table.drawOn(self.canvas, self.cm_to_points(2), self.cm_to_points(9.2))

    def draw_other_remarks_table(self, data: OtherRemarksTableData):
        d = OtherRemarksTableData()
        if d.other_remarks_text:
            # Configure style and word wrap
            s = getSampleStyleSheet()
            s = s["BodyText"]
            s.wordWrap = 'CJK'
            data2 = [[Paragraph(cell, s) for cell in row] for row in data]
        else:
            data2 = data
        # set column width
        col_width_in_cm = [0.94, 3, 13.15]
        col_width_in_points = list(map(lambda x: self.cm_to_points(x), col_width_in_cm))
        table = Table(data2, colWidths=col_width_in_points, rowHeights=200)
        table.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 1, colors.black),
                                   ('FONTNAME', (0, 0), (-1, -1), "Cambria"),
                                   ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                   ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                                   ('WORDWRAP', (0, 0), (-1, -1), True)
                                   ]))
        table.wrapOn(self.canvas, self.cm_to_points(2), self.cm_to_points(2))
        table.drawOn(self.canvas, self.cm_to_points(2), self.cm_to_points(2))

    def draw_bottom_table(self):
        col_widths_in_cm = [6, 11.2]
        col_widths_in_points = list(map(lambda x: self.cm_to_points(x), col_widths_in_cm))
        data = [["Imię i nazwisko sporządzającego", self.user_name]]
        table = Table(data, colWidths=col_widths_in_points)
        table.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 1, colors.black),
                                   ('FONTNAME', (0, 0), (-1, -1), "Cambria"),
                                   ]))
        table.wrapOn(self.canvas, self.cm_to_points(2), self.cm_to_points(1))
        table.drawOn(self.canvas, self.cm_to_points(2), self.cm_to_points(1))

    def save_file(self):
        self.canvas.save()

    @staticmethod
    def register_fonts():
        pdfmetrics.registerFont(TTFont("Cambria", "media/cambria.ttf"))
        pdfmetrics.registerFont(TTFont("Cambria Bold", "media/Cambria Bold.ttf"))

    @staticmethod
    def cm_to_points(cm):
        return cm * 28.35
