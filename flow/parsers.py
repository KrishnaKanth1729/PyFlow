import _ast
from ast import parse
from svg.canvas import Canvas
from svg.shapes import Text
from nodes import *
from readers import *


def parse_module(module: _ast.Module, canvas: Canvas, y: int) -> int:
    """
    Function parses an _ast.Module object to convert it into a flowchart
    """
    for item in module:
        if isinstance(item, _ast.Import):
            y = parse_import(item, canvas, y)
        elif isinstance(item, _ast.Assign):
            y = parse_assign(item, canvas, y)
        elif isinstance(item, _ast.For):
            y = parse_for(item, canvas, y)
        elif isinstance(item, _ast.FunctionDef):
            y = parse_function(item, canvas, y)
            print(item.body)
        # elif isinstance(item, _ast.While):
            # y = parse_while(item, canvas, y)
        elif isinstance(item, _ast.Return):
            y = parse_return(item, canvas, y)
        elif isinstance(item, _ast.If):
            y = parse_if(item, y, canvas)
    return y


def parse_import(import_object: _ast.Import, canvas: Canvas, y: int) -> int:
    """
    Function to parse the _ast.Import and convert it to SVG

    :param import_object
    :param canvas
    :param y
    """
    
    svg_content = stringify_import(import_object)

    InputOutputNode(text=svg_content, canvas=canvas, y=y, color="yellow")
    Text(x="50%", y=y+30, text=svg_content, parent=canvas, font_size="2.1em")
    Line(x1=canvas.width//2, y1=y+50, x2=canvas.width//2, y2=y+120, parent=canvas)
    
    return y + 100


def parse_assign(assign_object: _ast.Assign, canvas: Canvas, y: int) -> int:
    
    svg_content = stringify_assign(assign_object)

    OperationNode(text=svg_content, canvas=canvas, y=y, color="pink")
    Text(x="50%", y=y+30, text=svg_content, parent=canvas, font_size="2.1em")
    Line(x1=canvas.width//2, y1=y+50, x2=canvas.width//2, y2=y+120, parent=canvas)

    return y + 100


def parse_for(for_object: _ast.For, canvas: Canvas, y: int) -> int:
    svg_content = stringify_for(for_object)
    start_y = int(y)

    OperationNode(text=svg_content, canvas=canvas, y=y, color="pink")
    Text(x="50%", y=y+30, text=svg_content, parent=canvas, font_size="2.1em")
    Line(x1=canvas.width//2, y1=y+50, x2=canvas.width//2, y2=y+120, parent=canvas)
    
    y = parse_module(for_object.body, canvas, y+100)
    
    Terminal(text=" end ", canvas=canvas, y=y, color="pink")
    Text(x="50%", y=y+30, text="end", parent=canvas, font_size="2.1em")

    Line(x1=canvas.width//2-len(svg_content)*10 - 50, y1=start_y+25, 
    x2=canvas.width//2-len(svg_content)*10, y2=start_y+25, parent=canvas) 
    Line(x1=canvas.width//2-len(svg_content)*10 - 50, y1=start_y+25, 
    x2=canvas.width//2-len(svg_content)*10 - 50, y2=y+50, parent=canvas)
    Line(x1=canvas.width//2-len(svg_content)*10 - 50, y1=y+50, 
    x2=canvas.width//2, y2=y+50, parent=canvas)

    Line(x1=canvas.width // 2, y1=y+50, x2=canvas.width // 2, y2=y+100, parent=canvas)
    return y+100


def parse_function(func_object: _ast.FunctionDef, canvas: Canvas, y: int):
    svg_content = stringify_function_def(func_object)

    OperationNode(text=svg_content, canvas=canvas, y=y, color="pink")
    Text(x="50%", y=y+30, text=svg_content, parent=canvas, font_size="2.1em")
    Line(x1=canvas.width//2, y1=y+50, x2=canvas.width//2, y2=y+150, parent=canvas)
    start_y = int(y)

    y = parse_module(func_object.body, canvas, y+120) - 100

    Line(x1=canvas.width//2-len(svg_content)*10 - 50, y1=start_y+25, x2=canvas.width//2-len(svg_content)*10, y2=start_y+25, parent=canvas) 
    Line(x1=canvas.width//2-len(svg_content)*10 - 50, y1=start_y+25, x2=canvas.width//2-len(svg_content)*10 - 50, y2=y+50, parent=canvas)
    Line(x1=canvas.width//2-len(svg_content)*10 - 50, y1=y+50, x2=canvas.width//2, y2=y+50, parent=canvas)

    return y + 100


def parse_return(return_object: _ast.Return, canvas: Canvas, y: int) -> int:
    svg_content = stringify_return(return_object)

    OperationNode(text=svg_content, canvas=canvas, y=y, color="pink")
    Text(x="50%", y=y+30, text=svg_content, parent=canvas, font_size="2.1em")
    Line(x1=canvas.width//2, y1=y+50, x2=canvas.width//2, y2=y+150, parent=canvas)
    
    return y+100



def parse_if(if_object: _ast.If, canvas: Canvas, y: int) -> int:
    print(if_object.test)
    print("")



def parse_expr(expr_object: _ast.Expr, canvas: Canvas, y: int) -> int:
    if isinstance(expr_object, _ast.Compare):
        return stringify_compare(expr_object)


def parse_while(while_object: _ast.While, canvas: Canvas, y: int) -> int:

    stringify_compare(while_object.test)

def parse_pass(pass_object: _ast.Pass, canvas: Canvas, y: int) -> int:
    pass

def parse_tuple(tuple_object: _ast.Tuple, canvas: Canvas, y: int) -> int:
    pass

def parse_call(call_obj: _ast.Call, canvas: Canvas, y: int, draw: bool):
    pass