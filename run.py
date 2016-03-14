from arithmetic_tokenizer import tokenize
from arithmetic_parser import parse
from arithmetic_evaluator import evaluate

import re

import pprint

pp = pprint.PrettyPrinter(indent=4)

valid_input_re = re.compile('^(((\d+(\.\d+)?)|([\+\-\/\*]))[ $])+$')

def run():
	print("Use CTRL+C to exit") 
	try:
		source = input('Source:')
		is_source_valid = valid_input_re.match(source)
		if is_source_valid:
			print("Source string was invalid, please input an expression that is separated by single spaces")
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
	print("VALUE (arithmetic_evaluator.py)")
	value = evaluate(tree)

	print(value)
	run()

run()
