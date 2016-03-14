from arithmetic_tokenizer import tokenize
from arithmetic_parser import parse
from arithmetic_evaluator import evaluate

import re

import pprint

pp = pprint.PrettyPrinter(indent=4, width=1)

re_ops = '([\+\-\/\*])'
re_num = '(\d+(\.\d+)?)'
valid_input_re = re.compile('^((' + re_num + '|' + re_ops + ')( |$))+$')

def run():
	print('')
	try:
		source = input('Source:')
		is_source_valid = valid_input_re.match(source)
		is_valid_matched = is_source_valid != None
		if not is_valid_matched:
			print("Source string was invalid, please input an expression that is numbers and operators separated by single spaces")
			return run()
	except:
		print("Error reading input")
		return
	
	print("TOKENS (arithmetic_tokenizer.py)")
	tokens = tokenize(source)
	pp.pprint(tokens)
	print("TREE (Abstract Syntax Tree) (arithmetic_parser.py)")
	tree = parse(tokens)
	pp.pprint(tree)

	if tree is False:
		print("Error: Invalid source string")
		return run()

	print("VALUE (arithmetic_evaluator.py)")
	value = evaluate(tree)

	print(value)
	run()

print("Use CTRL+C to exit") 
run()
