from svg.canvas import Canvas
from svg.shapes import Rectangle, Parallelogram, Line
from svg.style import Style

class Terminal:
    def __init__(self, text: str, canvas: Canvas, y: str, color: str):
        self.text = text
        self.canvas = canvas
        self.y = y
        self.color = color
        Rectangle(width=len(self.text)*20, height=40, x=self.canvas.width//2 - len(self.text)*10, y=self.y+10, parent=self.canvas, rx=15, ry=15, style=Style({"fill": self.color, "stroke-width": 3, "stroke": "black"})).svg_content()

class OperationNode:
    def __init__(self, text: str, canvas: Canvas, y:str, coeff: int = 0, color: str = "white"):
        self.text = text
        self.canvas = canvas
        self.y = y 
        self.color = color
        Rectangle(width=len(self.text)*20, height=50, x=(self.canvas.width//2 - len(self.text)*10) + coeff, y=self.y, parent=self.canvas, style=Style({"fill": self.color, "stroke-width": 3, "stroke": "black"}))

class InputOutputNode:
    def __init__(self, text, canvas, y: str, coeff: int = 0, color: str = "white"):
        self.text = text
        self.canvas = canvas
        self.y = y
        self.color = color
        self.coeff = coeff
        Parallelogram(width=len(self.text)*20, height=50, x=(self.canvas.width // 2 - len(self.text)*10) + self.coeff, y=self.y, canvas=self.canvas, style=Style({"fill": self.color, 'stroke-width' :3, 'stroke':'rgb(0,0,0)'}))

class ConditionNode:
    def __init__(self, text, canvas, y: str, color: str = "white"):
        self.text = text
        self.canvas = canvas
        self.y = y
        self.color = color