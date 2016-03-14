from arithmetic_tokenizer import tokenize
from arithmetic_parser import parse
from arithmetic_evaluator import evaluate

import re

import pprint

pp = pprint.PrettyPrinter(indent=4, width=1)

re_ops = '([\+\-\/\*])'
re_num = '(-?\d+(\.\d+)?)'
valid_input_re = re.compile('^((' + re_num + '|' + re_ops + ')( |$))+$')

debug = True

def run():
	print('')
	try:
		source = input('Source:')
		is_source_valid = valid_input_re.match(source)
		is_valid_matched = is_source_valid != None
		if not is_valid_matched:
			if source == "debug":
				global debug
				debug = not debug
				print("DEBUG:", "ON" if debug else "OFF")
			else:
				print("Source string was invalid, please input an expression that is numbers and operators separated by single spaces")
			return run()
	except:
		print("Error reading input")
		return
	
	print("TOKENS (arithmetic_tokenizer.py)")
	tokens = tokenize(source, debug)
	pp.pprint(tokens)
	print("TREE (Abstract Syntax Tree) (arithmetic_parser.py)")
	tree = parse(tokens, debug)
	pp.pprint(tree)

	if tree is False:
		print("Error: Invalid source string")
		return run()

	print("VALUE (arithmetic_evaluator.py)")
	value = evaluate(tree, debug)

	print(value)
	run()

print("Enter `debug` to toggle debugging. Use CTRL+C to exit.")
print("DEBUG:", "ON" if debug else "OFF") 
run()
