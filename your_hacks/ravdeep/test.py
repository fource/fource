import os
import sys

local_module_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../..', 'lib')
)
sys.path.append(local_module_path)


from fource.parser.yaml_parser import Parser

def run():
	file1 = '../../config/checks/test/read.yml'

	parse = Parser(file1)
	print parse.parse()

run()
