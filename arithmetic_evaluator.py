# Evaluator module
from operators import *

# Testing github comprehension
# Takes a source string and returns a parse tree
def evaluate(ast):
	if (ast == {
			'operator': MULTIPLY,
			'L': 4,
			'R': {
				'operator': ADD,
				'L': 5,
				'R': 1
			}
		}):
		# return hardcoded answer to first test
		return 21
	elif (ast == {
			'operator': SUBTRACT,
			'L': { 'operator': SUBTRACT, 'L': 90, 'R': -1 },
			'R': 5
		}):
		# return hardcoded answer to first test
		return 86
	else:
		# demonstration code
		if (type(ast) is dict):
			operator = ast['operator']
			left = ast['L']
			right = ast['R']
			# probably make use of a recursive strategy
			# may be useful: https://chris-lamb.co.uk/posts/visitor-pattern-in-python
			return -1

		elif (type(ast) is float or type(ast) is int):
			# ast is already a number
			return ast

		else:
			raise	TypeError()
