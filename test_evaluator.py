from arithmetic_evaluator import evaluate
from operators import *
import tests
import unittest

class Test_Evaluator(unittest.TestCase):
	def test(self):
		print()
		for test in tests.tests:
			with self.subTest(ast=str(test['ast']), source=str(test['source'])):
				message = "\n  " + str(test['ast']) + " evaluated incorrect value: " + str(evaluate(test['ast']))
				val = evaluate(test['ast'])
				self.assertEqual(val, test['eval'], message)
				if(val == test['eval']):
					print(" Evaluator Success: " + str(test['ast']) + " ==> OK\n")

if __name__ == '__main__':
    unittest.main(verbosity=2, failfast=True)
