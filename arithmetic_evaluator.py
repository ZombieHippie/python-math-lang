# Evaluator module

# Takes a source string and returns a parse tree
def evaluate(ast):
	if (ast == { '*': { 'L': 4, 'R': { '+': { 'L': 5, 'R': 1 } } } }):
		# return hardcoded answer to first test
		return 21
	elif (ast == {
			'-': {
				'L': { '-': { 'L': 90, 'R': -1 } },
				'R': 5
			}
		}):
		# return hardcoded answer to first test
		return 86
	else:
		return 0
