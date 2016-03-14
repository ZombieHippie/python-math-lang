# Parser module
from operators import *

# Written and documented by Ali Bajwa

class ASTNode:
        # Constructor function for node class
        # Note: Nodes are only generated for operators
        # Note: Numeric values are assigned to the left/right of operator nodes
        def __init__(self, value):
                self.value = value
                self.left = None
                self.right = None
                self.parent = None
        
        # Generate the AST that tests are expecting
        # This method can be accessed by the last created node
        def genResult(self):
                root = self
                while(root.parent != None):
                        root = root.parent #Find the root
                return calcResult(root)
        
        # Used to print the AST when debug is enabled
        def __str__(self):
                root = self
                while(root.parent != None):
                        root = root.parent      # Find the root
                return traverse(root)              # Print the AST breadth-wise
        
        # Used to set values/pointers of the node object
        # 1 => left, 2 => right, 0 => parent
        def setNode(self, pos, nodeOrValue):
                if (pos == 1):
                        self.left = nodeOrValue
                        return True
                elif (pos == 2):
                        self.right = nodeOrValue
                        return True
                elif (pos == 0):
                        self.parent = nodeOrValue
                        return True
                else: # Sanity check for failure/wrong position given
                        return False
# End class
                        
# Recursive call to generate AST that the tests are expecting
def calcResRecursive(node):
        if (isinstance(node, int) or isinstance(node, float)): # If the node is a number
                return node                             # Return the number
        else:                                           # Node is an operator node
                tempres = {}
                tempres['operator'] = node.value
                tempres['L'] = calcResRecursive(node.left)
                tempres['R'] = calcResRecursive(node.right)
                return tempres

# Driver function for recursive call to create represent created AST as tests expect it
# Root node is always an operator node in this function - root node being a number is taken care of earlier
def calcResult(rootnode):
        result = {}
        result['operator'] = rootnode.value
        result['L'] = calcResRecursive(rootnode.left)
        result['R'] = calcResRecursive(rootnode.right)

        return result

# Used to print the AST in debug mode
# Implements a typical breadth first algorithm while printing the nodes in each level
def traverse(rootnode, level=0):
        res_str = ''
        queue = [rootnode]
        while (len(queue) != 0):
                nextlevel = []
                for node in queue:
                        if not(isinstance(node, int) or isinstance(node, float)):               # Node is an operator
                                res_str += str(node.value) + '\t'
                                nextlevel.append(node.left)
                                nextlevel.append(node.right)
                        else:                                                           # Node is a number/leaf/endpt
                                res_str += str(node) + '\t'
                res_str += '\n'
                queue = nextlevel
        return res_str

# Check operator precedence based on the grammar rules
def checkPrec(current, prev):
        precOrder = {SUBTRACT: 0, ADD: 1, DIVIDE: 2, MULTIPLY: 3}
        if (precOrder[current] < precOrder[prev]):
                return False
        else: # current > prev || current = prev (left associativity)
                return True

# Creates an operator node based on precedence
def makeOperatorNode(currentValue, prevNode, numberStack):
        precedence = checkPrec(currentValue, prevNode.value)
        newNode = ASTNode(currentValue)
        if (precedence == False):                                       # Case 1: Current < Prev
                newNode.setNode(2, prevNode)                    # prev node is the right child of new node
                prevNode.setNode(0, newNode)                    # new node is parent of prev node
                newNode.setNode(1, numberStack.pop(0))  # pop a new number from the number stack and assign to left of new node
                
        else:                                                                           # Case 2: Current > Prev || Current == Prev
                newNode.setNode(0, prevNode)                    # prev node is parent of new node
                newNode.setNode(2, prevNode.left)               # prev node's left integer is the new nodes right integer
                newNode.setNode(1, numberStack.pop(0))  # pop a new number from the number stack and assign to the left of the new node
                prevNode.setNode(1, newNode)                    # new node is left child of prev node

        return newNode
        
# Takes a source string and returns a parse tree
def parse(tokens, debug=False):
        if debug:
                print('DEBUG: Parse Tree:')
        numberStack = []                # Stack for numbers
        operatorStack = []              # Stack for operators
        for token in tokens:    # Parse tokens into respective stacks
                if (token['type'] == 'number'):
                        numberStack.insert(0,token['value'])
                else:
                        operatorStack.insert(0,token['value'])
                
        oppSize = len(operatorStack)    # Stack size of operators
        numSize = len(numberStack)              # Stack size of numbers
                
        #Sanity check for invalid syntax
        if (oppSize != (numSize - 1)):  # We must have one more number than we have operators
                return False
        if (oppSize == 0):                              # If we have no operators, we must have only one number - return it
                result = numberStack.pop(0)
                if (debug):
                        print(result)
                return result
                
        res = ASTNode(operatorStack.pop(0))     # Pop the first operator
        res.setNode(2, numberStack.pop(0))      # Pop the first number and assign to the right of popped operator node
        res.setNode(1, numberStack.pop(0))      # Pop the next number and assign to left of popped operator node
        prevNode = res                                          # Set previous node to this created node
        while(len(operatorStack) != 0):         # Run till out of operators
                prevNode = makeOperatorNode(operatorStack.pop(0), prevNode, numberStack)
        
        res = prevNode
        if (debug):
                print(res)
        result = res.genResult()
        return result