import ast
import _ast
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

    def svg(self) -> str:
        """
        A function to return the <svg> content of the code
        """
        ast_module = ast.parse(self.code).body
        print(ast_module)
        print(ast_module)
        y = parse_module(ast_module, self.canvas, 0)
        self.canvas.height = y  
        svg_server(self.canvas, port=8000)
        return self.canvas.svg_content

_ast.While
# Testing the parser
code = '''
import this
def main(x, y):
    x = 5

for item in this:
    x = 5
x = 5
def i():
    x = x
    y = x
    return x
if name == this:
    x = x
while i < 5:
    print("True")
'''
FlowchartSVG(code, 1000, 0, "yellow").svg()
