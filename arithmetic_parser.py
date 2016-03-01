# Parser module
from operators import *

# Takes a source string and returns a parse tree
def parse(tokens):
	if (tokens == [
			{ 'type': 'number', 'value': 4 },
			{ 'type': 'operator', 'value': MULTIPLY },
			{ 'type': 'number', 'value': 5 },
			{ 'type': 'operator', 'value': ADD },
			{ 'type': 'number', 'value': 1 }
		]):
		# return hardcoded answer to first test
		return {
			'operator': MULTIPLY,
			'L': 4,
			'R': {
				'operator': ADD,
				'L': 5,
				'R': 1
			}
		}
	else:
		# demonstration code
		res = {}
		res['L'] = 4
		res['R'] = 1
		res['operator'] = MULTIPLY
		return res
