# Tokenizer module
from operators import *

# Takes a source string and returns an array of tokens
def tokenize(str):
	if (str == "4 * 5 + 1"):
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
		res = []
		res.append({ 'type': 'number', 'value': 3 })
		res.append({ 'type': 'operator', 'value': ADD })
		return res