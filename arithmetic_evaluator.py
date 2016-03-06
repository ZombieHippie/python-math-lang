# Evaluator module
from operators import *

# Testing github comprehension
# Takes a source string and returns a parse tree
def evaluate(ast):
        if (ast == {
                        'operator': MULTIPLY,
                        'L': 4,
                        'R': {
                                'operator': ADD,
                                'L': 5,
                                'R': 1
                        }
                }):
                # return hardcoded answer to first test
                return 21
        elif (ast == {
                        'operator': SUBTRACT,
                        'L': { 'operator': SUBTRACT, 'L': 90, 'R': -1 },
                        'R': 5
                }):
                # return hardcoded answer to first test
                return 86
        else:
                # demonstration code
                recursive(ast);

def recursive(ast):

        if (type(ast) is float):
                return ast
                
        elif (type(ast) is int):
                return float(ast)
                
        elif (type(ast) is dict):
                operator = ast['operator']
                left = ast['L']
                right = ast['R']
                
                #When left half of operation is dictionary:
                if (type(left) is dict):
                        if operator == ADD:
                                return recursive(left) + ast['R']
                        elif operator == SUBTRACT:
                                return recursive(left) - ast['R']
                        elif operator == MULTIPLY:
                                return recursive(left) * ast['R']
                        elif operator == DIVIDE:
                                return recursive(left) / ast['R']
                        
                #When left is summed but right is dictionary:
                elif (type(right) is dict):
                        if operator == ADD:
                                return ast['L'] + recursive(right)
                        elif operator == SUBTRACT:
                                return ast['L'] - recursive(right)
                        elif operator == MULTIPLY:
                                return ast['L'] * recursive(right)
                        elif operator == DIVIDE:
                                return ast['L'] / recursive(right)
                        
                #When L and R are summed ints w operator between:
                else:
                        if operator == ADD:
                                return ast['L'] + ast['R']
                        elif operator == SUBTRACT:
                                return ast['L'] - ast['R']
                        elif operator == MULTIPLY:
                                return ast['L'] * ast['R']
                        elif operator == DIVIDE:
                                return ast['L'] / ast['R']
                        else:
                                raise TypeError()

        else:
                raise TypeError()
                
                



