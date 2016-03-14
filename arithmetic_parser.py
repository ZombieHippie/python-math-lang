# Parser module
from operators import *

class ASTNode:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
	
	def __str__(self):
		root = self
		while(root.parent != None):
			root = root.parent
		inOrder(root)
		return ""
	
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
		else:
			return False
	
def inOrder(node):
	if (node == None):
		return ''
	elif(isinstance(node, int)):
		print(node)
		return ''
	else:
		inOrder(node.left)
		print(node.value)
		inOrder(node.right)

def checkPrec(current, prev):
	precOrder = {SUBTRACT: 0, ADD: 1, DIVIDE: 2, MULTIPLY: 3}
	if (precOrder[current] < precOrder[prev]):
		return False
	else: # current > prev || current = prev (left associativity)
		return True
	
def makeOperatorNode(currentValue, prevNode, numberStack):
	precedence = checkPrec(currentValue, prevNode.value)
	newNode = ASTNode(currentValue)
	if (precedence == False):
		newNode.setNode(2, prevNode) # prev node is the right child of new node
		prevNode.setNode(0, newNode) # new node is parent of prev node
		newNode.setNode(1, numberStack.pop(0))
		
	else: #operators are the same, left associative by default -> make left child
		newNode.setNode(0, prevNode) # prev node is parent of new node
		newNode.setNode(2, prevNode.left)
		newNode.setNode(1, numberStack.pop(0))
		prevNode.setNode(1, newNode) # new node is left child of prev node

	return newNode
	
# Takes a source string and returns a parse tree
def parse(tokens, debug):
	numberStack = []
	operatorStack = []
	for token in tokens:
		if (token['type'] == 'number'):
			numberStack.insert(0,token['value'])
		else:
			operatorStack.insert(0,token['value'])
		
	oppSize = len(operatorStack)
	numSize = len(numberStack)
	print(operatorStack)
	print(numberStack)
		
	#Sanity check for invalid syntax
	if (oppSize < 1 or numSize < 2 or oppSize != (numSize - 1)):
		return False
		
	res = ASTNode(operatorStack.pop(0))
	res.setNode(2, numberStack.pop(0))
	res.setNode(1, numberStack.pop(0))
	prevNode = res
	while(len(operatorStack) != 0):		
		prevNode = makeOperatorNode(operatorStack.pop(0), prevNode, numberStack)
	
	res = prevNode
	if (debug):
		print(res)
	return res

tokens = [
			{ 'type': 'number', 'value': 4 },
			{ 'type': 'operator', 'value': MULTIPLY },
			{ 'type': 'number', 'value': 5 },
			{ 'type': 'operator', 'value': ADD },
			{ 'type': 'number', 'value': 1 }
		]
tokens1 =	[
			{ 'type': 'number', 'value': 4 },
			{ 'type': 'operator', 'value': DIVIDE },
			{ 'type': 'number', 'value': 2 },
			{ 'type': 'operator', 'value': SUBTRACT},
			{ 'type': 'number', 'value': 3 },
			{ 'type': 'operator', 'value': ADD},
			{ 'type': 'number', 'value': 4 },
			{ 'type': 'operator', 'value': MULTIPLY},
			{ 'type': 'number', 'value': 2},
			]
parse(tokens1, True)
