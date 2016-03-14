# Evaluator module
from operators import *

# Testing github comprehension
# Takes a source string and returns a parse tree

def evaluate(ast, debug=False):
        # demonstration code
        if debug:
                print('DEBUG: Evaluator Operations:')

        return recursive(ast, debug);

def recursive(ast, debug):

        if (type(ast) is float):
                return ast
                
        elif (type(ast) is int):
                return float(ast)
                
        elif (type(ast) is dict):
                operator = ast['operator']
                left = recursive(ast['L'], debug)
                right = recursive(ast['R'], debug)
                
                #When left half of operation is dictionary:
                # Delve into left side, preserve original right side
                if operator == ADD:
                        res = left + right
                elif operator == SUBTRACT:
                        res = left - right
                elif operator == MULTIPLY:
                        res = left * right
                elif operator == DIVIDE:
                        res = left / right
                else:
                        raise TypeError()

                if debug:
                        print('\t', left, operator, right, ' = ', res)

                return res

        else:
                raise TypeError()




