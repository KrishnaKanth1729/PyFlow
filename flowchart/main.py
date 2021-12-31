import ast
import _ast
import svg
from svg.canvas import Canvas
from svg.shapes import Parallelogram, Rectangle, Text, Line
from svg.style import Style
from svg.server import svg_server

_ast.Assign
class Terminal:
    def __init__(self, text: str, canvas: Canvas, y:str):
        self.text = text
        self.canvas = canvas
        self.y = y
    
    def svg_content(self):
        return Rectangle(width=len(self.text)*20, height=40, x=self.canvas.width//2 - len(self.text)*10, y=self.y, parent=self.canvas, rx=50, ry=50).svg_content()

class OperationNode:
    def __init__(self, text: str, canvas: Canvas, y:str, color: str = "white"):
        self.text = text
        self.canvas = canvas
        self.y = y 
        self.color = color
    
    def svg_content(self):
        return Rectangle(width=len(self.text)*20, height=40, x=self.canvas.width//2 - len(self.text)*10, y=self.y, parent=self.canvas, style=Style({"fill": self.color}))

class InputOutputNode:
    def __init__(self, text, canvas, y: str, color: str = "white"):
        self.text = text
        self.canvas = canvas
        self.y = y
        self.color = color
        Rectangle(width=len(self.text)*20, height=50, x=self.canvas.width//2 - len(self.text)*10, y=self.y, parent=self.canvas, style=Style({"fill": self.color}))


def parse_import(import_object: _ast.Import, canvas: Canvas, y: int) -> int:
    """
    Function to parse the _ast.Import and convert it to SVG

    :param import_object
    :param canvas
    :param y
    """
    svg_content: str = 'import '
    imports = []

    for alias in import_object.names:
        if alias.asname:
            imports.append(f"{alias.name} as {alias.asname}")
        else:
            imports.append(f"{alias.name}")

    svg_content += ", ".join(imports)

    InputOutputNode(text=svg_content, canvas=canvas, y=y, color="yellow")
    Text(x="50%", y=y+30, text=svg_content, parent=canvas, font_size="2.1em")
    Line(x1=canvas.width//2, y1=y+50, x2=canvas.width//2, y2=y+120, parent=canvas)
    
    return y + 100


def parse_assign(assign_object: _ast.Assign, canvas: Canvas, y: int) -> int:
    pass


def parse_for(for_object: _ast.For, canvas: Canvas, y: int) -> int:
    pass


def parse_function(func_object: _ast.FunctionDef, canvas: Canvas, y: int):
    pass


def parse_if(if_object: _ast.If, canvas: Canvas, y: int) -> int:
    pass


def parse_expr(expr_object: _ast.Expr):
    pass



class FlowchartSVG:
    """
    A class to convert Python3 code to SVG Flowcharts
    """
    def __init__(self, code: str, canvas_width: int, canvas_height: int, color: str):
        self.code = code
        self.canvas_width = canvas_width
        self.color = color
        self.canvas_height = canvas_height
        self.canvas = Canvas(canvas_width, canvas_height)
        self.y = 0
    
    def svg(self):
        ast_module = ast.parse(self.code).body
        print(ast_module)
        for item in ast_module:
            if isinstance(item, _ast.Import):
                self.y = parse_import(item, self.canvas, self.y)
            elif isinstance(item, _ast.Assign):
                self.y = parse_assign(item, self.canvas, self.y)
                
        # print(self.canvas.svg_content())
        svg_server(self.canvas, port=5000)


p = FlowchartSVG('''
import this as t, that; import all
import pygame
import cv2 as cv
x = cv
for i in range(5):
    print("Hello, World")
@decorator
def hello():
    print("mhm")
if x == cv:
    print("True")

''', 1000, 800, "#333")
p.svg()