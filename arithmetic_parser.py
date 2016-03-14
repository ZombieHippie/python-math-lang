# Parser module
from operators import *

class ASTNode:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
	
	def genResult(self):
		root = self
		while(root.parent != None):
			root = root.parent
		return calcResult(root)
		
	def __str__(self):
		root = self
		while(root.parent != None):
			root = root.parent
		traverse(root)
		return ''
	
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

def calcResRecursive(node):
	if (isinstance(node, int)):
		return node
	else:
		tempres = {}
		tempres['operator'] = node.value
		tempres['L'] = calcResRecursive(node.left)
		tempres['R'] = calcResRecursive(node.right)
		return tempres
	
def calcResult(rootnode):
	result = {}
	result['operator'] = rootnode.value
	result['L'] = calcResRecursive(rootnode.left)
	result['R'] = calcResRecursive(rootnode.right)

	return result
			
def traverse(rootnode):
	queue = [rootnode]
	while (len(queue) != 0):
		nextlevel = []
		for node in queue:
			if not(isinstance(node, int)):
				print(node.value, end='')
				nextlevel.append(node.left)
				nextlevel.append(node.right)
			else:
				print(node, end='')
		print()
		queue = nextlevel

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
def parse(tokens): #add debug to tests
	debug = False
	numberStack = []
	operatorStack = []
	for token in tokens:
		if (token['type'] == 'number'):
			numberStack.insert(0,token['value'])
		else:
			operatorStack.insert(0,token['value'])
		
	oppSize = len(operatorStack)
	numSize = len(numberStack)
		
	#Sanity check for invalid syntax
	if (oppSize != (numSize - 1)):
		return False
	if (oppSize == 0):
		result = numberStack.pop(0)
		if (debug):
			print(result)
		#print (result) #remove this line
		return result
		
	res = ASTNode(operatorStack.pop(0))
	res.setNode(2, numberStack.pop(0))
	res.setNode(1, numberStack.pop(0))
	prevNode = res
	while(len(operatorStack) != 0):		
		prevNode = makeOperatorNode(operatorStack.pop(0), prevNode, numberStack)
	
	res = prevNode
	if (debug):
		print(res)
	result = res.genResult()
	#print (result)
	return result
'''
token1 = [
			{ 'type': 'number', 'value': 4 },
			{ 'type': 'operator', 'value': MULTIPLY },
			{ 'type': 'number', 'value': 5 },
			{ 'type': 'operator', 'value': ADD },
			{ 'type': 'number', 'value': 1 }
		]

token2 = [
			{ 'type': 'number', 'value': 90 },
			{ 'type': 'operator', 'value': SUBTRACT },
			{ 'type': 'number', 'value': -1 },
			{ 'type': 'operator', 'value': SUBTRACT },
			{ 'type': 'number', 'value': 5 }
		]
		
token3 = [
			{ 'type': 'number', 'value': 90 },
			{ 'type': 'operator', 'value': MULTIPLY },
			{ 'type': 'number', 'value': -1 },
			{ 'type': 'operator', 'value': MULTIPLY },
			{ 'type': 'number', 'value': 5 }
		]
		
token4 = [
			{ 'type': 'number', 'value': 90 },
			{ 'type': 'operator', 'value': DIVIDE },
			{ 'type': 'number', 'value': 1 },
			{ 'type': 'operator', 'value': DIVIDE },
			{ 'type': 'number', 'value': 5 }
		]
		
token5 = [
			{ 'type': 'number', 'value': 1 },
			{ 'type': 'operator', 'value': DIVIDE },
			{ 'type': 'number', 'value': 5 },
			{ 'type': 'operator', 'value': SUBTRACT },
			{ 'type': 'number', 'value': 90 }
		]
		
token6 = [
			{ 'type': 'number', 'value': 90 },
			{ 'type': 'operator', 'value': SUBTRACT },
			{ 'type': 'number', 'value': 1 },
			{ 'type': 'operator', 'value': DIVIDE },
			{ 'type': 'number', 'value': 5 }
		]
		
token7 = [
			{ 'type': 'number', 'value': 905 }
		]
		
token8 = [
			{ 'type': 'number', 'value': -49 }
		]
		
parse(token1)
parse(token2)
parse(token3)
parse(token4)
parse(token5)
parse(token6)
parse(token7)
parse(token8)
'''