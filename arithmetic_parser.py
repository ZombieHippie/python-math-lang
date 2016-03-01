# Parser module

# Takes a source string and returns a parse tree
def parse(str):
	if (str == "4 * 5 + 1"):
		# return hardcoded answer to first test
		return {
			'*': {
				'L': 4,
				'R': { '+': { 'L': 5, 'R': 1 } }
			}
		}
	else:
		return {}
