from arithmetic_parser import parse
from operators import *
import tests
import unittest

class Test_AST(unittest.TestCase):
	def test(self):
		print()
		for test in tests.tests:
			message = "\n  \"" + str(test['tokens']) + "\" generated incorrect AST."
			val = parse(test['tokens'])
			self.assertEqual(val, test['ast'], message)
			if(val == test['ast']):
				print(" Parse Success: " + str(test['tokens']) + " ==> OK\n")

if __name__ == '__main__':
    unittest.main(verbosity=2, failfast=True)