import ast
import _ast
_ast.Compare
code = '''
while x < 5:
    print("h")
'''

print(ast.parse(code).body[0].test)