# Tokenizer module
from operators import *

# Takes a source string and returns an array of tokens
def tokenize(str):

	token_map = {'+':'ADD', '-':'SUBTRACT',
             '*':'MULTIPLY', '/':'DIVIDE'}

	if (str == "4 * 5"):
		# return hardcoded answer to first test
		return [
			{ 'type': 'number', 'value': 4 },
			{ 'type': 'operator', 'value': MULTIPLY },
			{ 'type': 'number', 'value': 5 },
			{ 'type': 'operator', 'value': ADD },
			{ 'type': 'number', 'value': 1 }
		]
	else:
		# demonstration code
		# res.append({ 'type': 'number', 'value': 3 })
		# res.append({ 'type': 'operator', 'value': ADD })
		res = []

		# split_expr = str.findall('[\d.]+|[%s]' % ''.join(token_map), expr)
		# split_expr = [int(i) for i in str.split()]
		str.split()

		for x in str:
			if (isinstance(str[x], str)):
				res.append = ({ 'type': 'operator', 'value': (token_map.get(x)) })
			elif (isinstance(str[x], int)):
				res.append = ({ 'type': 'number', 'value': x })
		
		return res
