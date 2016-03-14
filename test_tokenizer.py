from arithmetic_tokenizer import tokenize
import tests
import unittest

class Test_Tokenizer(unittest.TestCase):
	def test(self):
		print()
		for test in tests.tests:
			message = "\n  \"" + test['source'] + "\" generated incorrect Tokens."
			val = tokenize(test['source'])
			self.assertEqual(val, test['tokens'], message)
			if(val == test['tokens']):
				print(" Tokenizer Success: " + str(test['source']) + " ==> OK\n")

if __name__ == '__main__':
    unittest.main()