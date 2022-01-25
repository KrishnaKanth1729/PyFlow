import _ast

def stringify_function_call(call_obj: _ast.Call) -> str:
    """
    Converts an _ast.Call object to a function call with params
    >>> func(arg1, arg2)
    """
    string = f'{call_obj.func.id}'
    args = list(map(stringify_value, call_obj.args))

    return f"{string}({', '.join(args)})"


def stringify_value(value):
    if isinstance(value, _ast.Call):
        return stringify_function_call(value)
    elif isinstance(value, _ast.Constant):
        return str(stringify_constant(value))
    elif isinstance(value, _ast.Name):
        return stringify_name(value)
    
def stringify_import(import_obj: _ast.Import) -> str:
    """
    Converts an `_ast.Import` object to an `import` statement
    >>> import module as alias
    """
    svg_content: str = 'import '
    imports = []

    for alias in import_obj.names:
        if alias.asname:
            imports.append(f"{alias.name} as {alias.asname}")
        else:
            imports.append(f"{alias.name}")

    svg_content += ", ".join(imports)
    return svg_content

def stringify_assign(assign_object: _ast.Assign) -> str:
    svg_content = ''
    for name in assign_object.targets:
        svg_content += str(name.id)
    svg_content += f' = {stringify_value(assign_object.value)}'

    return svg_content

def stringify_for(for_object: _ast.For) -> str:

    if isinstance(for_object.iter, _ast.Constant):
        svg_content = f"for {for_object.target.id} in {stringify_constant(for_object.iter)}"
    elif isinstance(for_object.iter, _ast.Call):
        svg_content = f"for {for_object.target.id} in {stringify_function_call(for_object.iter)}"
    else:
        svg_content = f"for {for_object.target.id} in {for_object.iter.id}"
        
    return svg_content


def stringify_function_def(func_def_object: _ast.FunctionDef) -> str:
    svg_content = f'start {func_def_object.name} '
    args = []

    for arg in func_def_object.args.args:
        args.append(arg.arg)
    
    svg_content += f"({', '.join(args)})"
    
    return svg_content
   
def stringify_return(return_object: _ast.Return):
    return f"return -> {stringify_value(return_object.value)}"

def stringify_name(name: _ast.Name):
    return name.id


def stringify_constant(const: _ast.Constant):
    return const.value
_ast.Lt
def stringify_compare(compare: _ast.Compare):
    print(stringify_value(compare.left))
    print(dir(compare.ops[0]))
    