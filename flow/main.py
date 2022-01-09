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
                
        # print(self.canvas.svg_content())
        svg_server(self.canvas, port=9000)


p = FlowchartSVG('''
import this as t, that; import all
import pygame
import cv2 as cv
xas = cv
for i in this:
    for name in n:
        x = y
        y = y
    dx = dy
@decorator
def hello():
    print("mhm")
if x == cv:
    print("True")
elif y == l:
    pass
while i < 5:
    pass
print("hello")
''', 1000, 2000, "#333")
p.svg()
_ast.Call
