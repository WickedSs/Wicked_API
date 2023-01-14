from math import ceil, prod
from Reporter.elements.Objects import *
from reportlab.pdfbase.pdfmetrics import stringWidth


class StaticText(Util, ReportElement, TextElement, Text):
    
    def __init__(self, element):
        super().__init__()
        self.name = "StaticText"
        self.element = element
        self.subElements = []
        self.x, self.y = -10, -10

    def run(self, url):
        self.subElements.append(ReportElement().fetch(self.element, url))
        self.subElements.append(TextElement().fetch(self.element, url))
        self.subElements.append(Text().fetch(self.element, url))
        return self

    def prepare(self, canvas, section, jasperAttrib, jasperMargin, jasperParameters, current_v_position):
        size = [jasperAttrib.get("pageWidth"), jasperAttrib.get("pageHeight")]
        coords_element, text_element, text = self.subElements
        
        x = int(coords_element.coords.get("x"))
        y = int(coords_element.coords.get("y"))
        self.width = int(coords_element.coords.get("width"))
        self.height = int(coords_element.coords.get("height"))
        self.hAlignment = text_element.alignement.get("textAlignment")
        self.vAlignment = text_element.alignement.get("verticalAlignment") # always set to center
        self.text_value = text.text

        self.x, self.y = Util.coord(x, y, current_v_position + (self.height * 0.75), jasperMargin)

        fontFamily = "Arial" if text_element.font.get("fontName") == None else text_element.font.get("fontName")
        fontSize = 11 if text_element.font.get("size") == None else int(text_element.font.get("size"))
        text_width = stringWidth(text.text, fontFamily, fontSize)
        self.indentation = Util.calculate_alignment(self.width, text_width, self.hAlignment)

        canvas.pdf_canvas.setFillColorRGB(0, 0, 0)
        canvas.pdf_canvas.setFont(fontFamily, fontSize)


class TextField(Util, ReportElement, TextElement, textFieldExpression):
    
    def __init__(self, element):
        super().__init__()
        self.name = "TextField"
        self.element = element
        self.subElements = []
        self.x, self.y = -10, -10

    def run(self, url):
        self.subElements.append(ReportElement().fetch(self.element, url))
        self.subElements.append(TextElement().fetch(self.element, url))
        self.subElements.append(textFieldExpression().fetch(self.element, url))
        return self

    def prepare(self, canvas, section, jasperAttrib, jasperMargin, jasperParameters, current_v_position):
        size = [jasperAttrib.get("pageWidth"), jasperAttrib.get("pageHeight")]
        coords_element, text_element, text_expression = self.subElements
        
        self.text_value = ""
        if text_expression.expression_type == "parameter":
            parameter = jasperParameters.get(text_expression.expression[0])
            if parameter != None:
                self.text_value = parameter
        else:
            values = []
            for exp in text_expression.expression:
                field = section.fields.get(exp)
                if field != None:
                    values.append(field)

            values = [float(val) if Util.isFloat(val) else val for val in values]
            operation = text_expression.expression_operation[0] if text_expression.expression_operation else ""
            match operation:
                case "*":
                    self.text_value = prod(values)
                case "+":
                    self.text_value = sum(values)
                case "-":
                    self.text_value = values[0] - sum(values[1:])
                case "/":
                    self.text_value = values[0] - values[1]
                case _:
                    self.text_value = values[0] if len(values) > 0 else 0
        
        self.text_value = str(self.text_value)
        
        print(f"{text_expression.expression}")
        if all(item in ["price", "total", "FactureTVA", "FactureTotal"] for item in text_expression.expression):
            self.text_value = str(Util.format_currency(self.text_value))
        
        if all(item in ["quantity"] for item in text_expression.expression):
            self.text_value = str(int(float(self.text_value)))

        print(f"{text_expression.expression} {text_expression.expression_operation} {self.text_value}")
        x = int(coords_element.coords.get("x"))
        y = int(coords_element.coords.get("y"))
        self.width = int(coords_element.coords.get("width"))
        self.height = int(coords_element.coords.get("height"))
        self.hAlignment = text_element.alignement.get("textAlignment")
        self.vAlignment = text_element.alignement.get("verticalAlignment") # always set
        
        self.x, self.y = Util.coord(x, y, current_v_position + (self.height * 0.75), jasperMargin)

        fontFamily = "Arial" if text_element.font.get("fontName") == None else text_element.font.get("fontName")
        fontSize = 11 if text_element.font.get("size") == None else int(text_element.font.get("size"))
        text_width = stringWidth(self.text_value, fontFamily, fontSize)
        self.indentation = Util.calculate_alignment(self.width, text_width, self.hAlignment)
        
        if text_element.paragraph.get("leftIndent") != None:
            self.indentation += int(text_element.paragraph.get("leftIndent"))
        if text_element.paragraph.get("rightIndent") != None:
            self.indentation -= int(text_element.paragraph.get("rightIndent"))
        
        canvas.pdf_canvas.setFillColorRGB(0, 0, 0)
        canvas.pdf_canvas.setFont(fontFamily, fontSize)
        
class Rectangle(Util, ReportElement, GraphicElement):
    
    def __init__(self, element):
        super().__init__()
        self.name = "Rectangle"
        self.element = element
        self.element_attrib = self.element.attrib
        self.subElements = []
        self.x, self.y = -10, -10
    
    def run(self, url):
        self.subElements.append(ReportElement().fetch(self.element, url))
        self.subElements.append(GraphicElement().fetch(self.element, url))
        return self

    def prepare(self, canvas, section, jasperAttrib, jasperMargin, jasperParameters, current_v_position):
        size = [jasperAttrib.get("pageWidth"), jasperAttrib.get("pageHeight")]
        coords_element, graphic_element = self.subElements

        x = int(coords_element.coords.get("x"))
        y = int(coords_element.coords.get("y"))
        self.width = int(coords_element.coords.get("width"))
        self.height = int(coords_element.coords.get("height"))
        
        self.x, self.y = Util.coord(x, y, current_v_position, jasperMargin)

        self.radius = self.element_attrib.get("radius")
        self.stroke = ceil(float(graphic_element.pen.get("lineWidth")))
        self.fill = 0
        backcolor = coords_element.coords.get("backcolor")

        if backcolor != None and backcolor != "#FFFFFF":
            r, g, b = Util.hex_to_RGB(backcolor.replace("#", ""))
            canvas.pdf_canvas.setFillColorRGB(r/255, g/255, b/255)
            self.fill = 1

        canvas.pdf_canvas.setStrokeColorRGB(0, 0, 0)