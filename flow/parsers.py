import _ast
from ast import parse
from svg.canvas import Canvas
from svg.shapes import Text
from nodes import *


def parse_module(module: _ast.Module, canvas: Canvas, y: int) -> int:
    for item in module:
        if isinstance(item, _ast.Import):
            y = parse_import(item, canvas, y)
        elif isinstance(item, _ast.Assign):
            y = parse_assign(item, canvas, y)
        elif isinstance(item, _ast.For):
            y = parse_for(item, canvas, y)
    return y


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
    svg_content = ''
    for name in assign_object.targets:
        svg_content += str(name.id)
    svg_content += f' = {assign_object.value.id}'

    OperationNode(text=svg_content, canvas=canvas, y=y, color="pink")
    Text(x="50%", y=y+30, text=svg_content, parent=canvas, font_size="2.1em")
    Line(x1=canvas.width//2, y1=y+50, x2=canvas.width//2, y2=y+120, parent=canvas)

    return y + 100



def parse_for(for_object: _ast.For, canvas: Canvas, y: int) -> int:
    svg_content = f"for {for_object.target.id} in {for_object.iter.id}"
    start_y = int(y)

    OperationNode(text=svg_content, canvas=canvas, y=y, color="pink")
    Text(x="50%", y=y+30, text=svg_content, parent=canvas, font_size="2.1em")
    Line(x1=canvas.width//2, y1=y+50, x2=canvas.width//2, y2=y+120, parent=canvas)
    
    y = parse_module(for_object.body, canvas, y+100)

    Line(x1=canvas.width//2-len(svg_content)*10 - 50, y1=start_y+25, x2=canvas.width//2-len(svg_content)*10, y2=start_y+25, parent=canvas) 
    Line(x1=canvas.width//2-len(svg_content)*10 - 50, y1=start_y+25, x2=canvas.width//2-len(svg_content)*10 - 50, y2=y-50, parent=canvas)
    Line(x1=canvas.width//2-len(svg_content)*10 - 50, y1=y-50, x2=canvas.width//2, y2=y-50, parent=canvas)

    return y+100

def parse_function(func_object: _ast.FunctionDef, canvas: Canvas, y: int):
    pass


def parse_if(if_object: _ast.If, canvas: Canvas, y: int) -> int:
    pass


def parse_expr(expr_object: _ast.Expr, canvas: Canvas, y: int) -> int:
    pass


def parse_while(while_object: _ast.While, canvas: Canvas, y: int) -> int:
    pass


def parse_pass(pass_object: _ast.Pass, canvas: Canvas, y: int) -> int:
    pass

def parse_tuple(tuple_object: _ast.Tuple, canvas: Canvas, y: int) -> int:
    pass

def parse_call(call_obj: _ast.Call, canvas: Canvas, y: int, draw: bool):
    pass