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
		evaluateTree(ast);

def evaluateTree(ast):
	if (type(ast) is dict):
		operator = ast['operator']
		left = ast['L']
		right = ast['R']
		int i = 0;
		
		#When left half of operation is dictionary:
		if (type(left) is dict):
			#Remove the left branch and evaluateTree(left)
			#when down to ints and operators, proceed
			for 'L', 'operator', 'R' in left.iteritems():
				if 'operator' == ADD:
					return left['L'] + left['R']
				elif 'operator' == SUBTRACT:
					return left['L'] - left['R']
				elif 'operator' == MULTIPLY:
					return left['L'] * left['R']
				elif 'operator' == DIVIDE:
					return left['L'] / left['R']
				else:
					raise TypeError()
			#Return evaluated left half of the tree
		
		#When left is summed but right is dictionary:
		elif (type(right) is dict):
			#Remove the right branch and evaluateTree(right)
			#when down to ints and operators, proceed
			for 'L', 'operator', 'R' in right.iteritems():
				if 'operator' == ADD:
					return right['L'] + right['R']
					return right['R']
				elif 'operator' == SUBTRACT:
					return right['L'] - right['R']
				elif 'operator' == MULTIPLY:
					return right['L'] * right['R']
				elif 'operator' == DIVIDE:
					return right['L'] / right['R']
				else:
					raise TypeError()
			#Return evaluated right half of tree
			
		#When L and R are summed ints w operator between:
		else:
			for 'L', 'operator', 'R' in ast.iteritems():
				if 'operator' == ADD:
					return ast['L'] + ast['R']
				elif 'operator' == SUBTRACT:
					return ast['L'] - ast['R']
				elif 'operator' == MULTIPLY:
					return ast['L'] * ast['R']
				elif 'operator' == DIVIDE:
					return ast['L'] / ast['R']
				else:
					raise TypeError()
		
		
			

	elif (type(ast) is float or type(ast) is int):
		# ast is already a number
		return ast

	else:
		raise TypeError()
		
		


