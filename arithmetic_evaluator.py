# Evaluator module
from operators import *

# Testing github comprehension
# Takes a source string and returns a parse tree

def evaluate(ast):
        # demonstration code
        return recursive(ast);

def recursive(ast):

        if (type(ast) is float):
                return ast
                
        elif (type(ast) is int):
                return float(ast)
                
        elif (type(ast) is dict):
                operator = ast['operator']
                left = recursive(ast['L'])
                right = recursive(ast['R'])
                print(ast)
                
                #When left half of operation is dictionary:
                # Delve into left side, preserve original right side
                if operator == ADD:
                        return left + right
                elif operator == SUBTRACT:
                        return left - right
                elif operator == MULTIPLY:
                        return left * right
                elif operator == DIVIDE:
                        return left / right
                else:
                        raise TypeError()

        else:
                raise TypeError()




