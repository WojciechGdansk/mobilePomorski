from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, TableStyle
from reportlab.pdfbase.ttfonts import TTFont

from form_data.form_info import FourthLeague
from form_data.match_info import MatchInfo
from pdf_creator.main_table_data import MainTableData
from pdf_creator.top_table_data import TableData


class PDFDocument:
    def __init__(self):
        self.canvas = Canvas

    def create_document(self):
        self.set_filename_and_size()
        self.register_fonts()
        self.draw_text("ZAŁĄCZNIK DO SPRAWOZDANIA SĘDZIEGO LUB OBSERWATORA SĘDZIÓW")
        match = MatchInfo()
        match.league = "iv liga"
        match.date = "22-05-2022"
        match.home_team = "Anioly"
        match.away_team = "Powsiel"
        self.draw_top_table(TableData(match).table_info())
        stadion_facilities = FourthLeague()
        stadion_facilities.parking = True
        stadion_facilities.statute = False
        stadion_facilities.field_verified_document = True
        self.draw_main_table(MainTableData(stadion_facilities).table_data())
        self.save_file()

    def set_filename_and_size(self, filename="Załącznik do sprawozdania - MW.pdf") -> None:
        self.canvas = Canvas(filename, pagesize=A4)

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
                                   ('FONTNAME', (0, 0), (-1, -1), "Cambria")
                                   ]))
        table.wrapOn(self.canvas, self.cm_to_points(2), self.cm_to_points(9.4))
        table.drawOn(self.canvas, self.cm_to_points(2), self.cm_to_points(9.4))

    def save_file(self):
        self.canvas.save()


    @staticmethod
    def register_fonts():
        pdfmetrics.registerFont(TTFont("Cambria", "cambria.ttf"))
        pdfmetrics.registerFont(TTFont("Cambria Bold", "Cambria Bold.ttf"))

    @staticmethod
    def cm_to_points(cm):
        return cm * 28.35


doc = PDFDocument()
doc.create_document()
