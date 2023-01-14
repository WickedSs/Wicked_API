from reportlab.pdfgen import canvas
import xml.etree.ElementTree as ET
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.pdfbase.ttfonts import TTFont

import os, sys

class PDF:
    def __init__(self, current_height: int = 0):
        self.dimensions = A4
        self.register_fonts()
        self.current_height = current_height

    def set_height(self, value):
        self.current_height += value

    def register_fonts(self):
        for file in os.listdir(os.path.join("Reporter", "fonts")):
            _, ext = file.split(".")
            registerFont(TTFont(_.capitalize(), os.path.join("Reporter", "fonts", f"{file}")))

    def create_pdf(self, filename: str, margin: list):
        self.path = os.path.join("Reporter", "examples", f"{filename}.pdf")
        self.pdf_canvas = canvas.Canvas(self.path, pagesize=letter, bottomup=0)

    def draw_line(self, x1: int, y1: int, x2: int, y2: int, line_width: float = .3):
        self.pdf_canvas.setLineWidth(line_width)
        self.pdf_canvas.setStrokeColorRGB(1, 0, 0)
        self.pdf_canvas.line(x1, y1, x2, y2)

    def draw_circle(self, x, y, radius, color: tuple, stroke: int = 1, fill: int = 0):
        self.pdf_canvas.setStrokeColorRGB(color[0]/255, color[1]/255, color[2]/255)
        self.pdf_canvas.circle(x, y, radius, stroke, fill)

    def draw_image(self, x, y, imagePath):
        self.pdf_canvas.drawImage(imagePath, x, y, 
            width=None, height=None, mask=None, preserveAspectRatio=False, 
            anchor='c', anchorAtXY=False, showBoundary=False
        )

    def set_font(self, fontname: str = "Arial", size: int = 11):
        self.pdf_canvas.setFont(fontname, size)

    
    def coord(self, x, y, width, height, unit=1.33):
        x, y = x * unit, (y + height + self.current_height) * unit
        return x, y

    def new_page(self):
        self.pdf_canvas.showPage()

    def save_pdf(self):
        self.pdf_canvas.save()
