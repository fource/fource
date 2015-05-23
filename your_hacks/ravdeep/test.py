from yaml_parser import Parser


def run():
	file1 = 'test.yml'

	parse = Parser(file1)
	print parse.parse()

run()
