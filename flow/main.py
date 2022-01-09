import ast
import _ast
from svg.shapes import Parallelogram, Rectangle, Text, Line
from svg.server import svg_server
from parsers import parse_module
from svg.canvas import Canvas


class FlowchartSVG:
    """
    A class to convert Python3 code to SVG Flowcharts
    using ast
    """
    def __init__(self, code: str, canvas_width: int,
                canvas_height: int, color: str):
        self.code = code
        self.canvas_width = canvas_width
        self.color = color
        self.canvas_height = canvas_height
        self.canvas = Canvas(canvas_width, canvas_height)
        self.y = 0

    def svg(self):
        ast_module = ast.parse(self.code).body
        print(ast_module)
        parse_module(ast_module, self.canvas, 0)
                
        svg_server(self.canvas, port=9000)

code = '''
import this

x = y
for item in this:
    x = y
'''
FlowchartSVG(code, 1000, 2000, "yellow").svg()