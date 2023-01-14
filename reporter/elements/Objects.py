import re



class Util:

    def calculate_alignment(rect_width, text_width, alignement):
        match alignement:
            case "Center":
                return (rect_width - text_width) / 2
            case "Left":
                return 0 
            case "Right":
                return rect_width - text_width
            case _:
                return 2

    def hex_to_RGB(hex_value):
        return tuple(int(hex_value[i:i+2], 16) for i in (0, 2, 4))

    def coord(x, y, current_height, margin):
        position_x = ((margin[2] + margin[2] * 0.5) + x)
        position_y = (margin[2]) + y + current_height
        return position_x, position_y

    def format_currency(amount):
        return f"{float(amount):,.2f}"

    def new_page(x, y, jasperAttrib, jasperMargin, canvas):
        if y >= int(jasperAttrib.get("pageHeight")) - jasperMargin[2]:
            canvas.new_page()
            x, y = Util.coord(x, jasperMargin[0], 0, jasperMargin)
            return x, y
        
        return x, y

    def isFloat(value):
        try:
            value = float(value)
            return True
        except ValueError:
            return False



class ReportElement(object):
    coords = None

    def fetch(self, element, url):
        report_element = element.find(f"{url}reportElement")
        if report_element != None:
            self.coords = report_element.attrib

        return self


class TextElement(object):
    alignement = None
    font = None
    paragraph = None

    def fetch(self, element, url):
        text_element = element.find(f"{url}textElement")
        if text_element != None:
            self.alignement = text_element.attrib
            self.font = text_element.find(f"{url}font").attrib if text_element.find(f"{url}font") != None else {}
            self.paragraph = text_element.find(f"{url}paragraph").attrib if text_element.find(f"{url}paragraph") != None else {}

        return self


class GraphicElement(object):
    pen = { "lineWidth" : 0 }

    def fetch(self, element, url):
        graphic_element = element.find(f"{url}graphicElement")
        if graphic_element != None:
            self.pen = graphic_element.find(f"{url}pen").attrib if graphic_element.find(f"{url}pen") != None else { "lineWidth" : 0 }

        return self


class Text(object):
    text = None

    def fetch(self, element, url):
        text_element = element.find(f"{url}text")
        if text_element != None:
            self.text = text_element.text

        return self


class textFieldExpression(object):
    expression = None
    expression_type = None
    expression_operation = None

    def fetch(self, element, url):
        text_Field_Expression = element.find(f"{url}textFieldExpression")
        if text_Field_Expression != None:
            self.expression_type = "field" if "$F" in text_Field_Expression.text else "parameter"
            self.expression = re.findall(r'{(.+?)}', str(text_Field_Expression.text))
            self.expression_operation = [c for c in str(text_Field_Expression.text) if c in '+-/*']

        return self
