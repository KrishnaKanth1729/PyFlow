import _ast
import ast
_ast.Name
_ast.For
code = """
for item in this:
    for name in names:
        print("hello")
"""

print(ast.parse(code).body[0].target.id)
print(ast.parse(code).body[0].iter.id)