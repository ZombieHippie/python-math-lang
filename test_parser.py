from arithmetic_parser import parse
import tests
import unittest

class Test_AST(unittest.TestCase):
	def test(self):
		print()
		for test in tests.tests:
			message = "\n  \"" + test['source'] + "\" generated incorrect AST."
			val = parse(test['source'])
			self.assertEqual(val, test['ast'], message)
			if(val == test['ast']):
				print(" Parse Success: " + str(test['source']) + " ==> OK")

if __name__ == '__main__':
    unittest.main(verbosity=2, failfast=True)