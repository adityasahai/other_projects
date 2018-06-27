import ast

source = '6 + 8'
node = ast.parse(source, mode='eval')

print eval(compile(node, '<string>', mode='eval'))
