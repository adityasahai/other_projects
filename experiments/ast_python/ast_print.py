from astpretty import pprint as pp
import ast
import sys

if __name__ == '__main__':
	filename = sys.argv[1]
	# read file
	filedata = open(filename, 'r').read()
	# dump data
	pp(ast.parse(filedata))
