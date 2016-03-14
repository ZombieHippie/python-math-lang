# About this Project

## Members

**Jacob Addotta**

 * Programmed `arithmetic_tokenizer.py`

**Ali Bajwa**

 * Programmed `arithmetic_evaluator.py`
 * Designed `Grammar rules.txt`

**Jess Geiger**

 * Programmed `arithmetic_evaluator.py`

**Cole Lawrence**

 * Designed test cases and test files.
 * Set up Slack communications
 * Set up Git repository
 * Documentation


## Summary

### Background Experience

The tools that enabled our team to complete this project included:
 * **All members**: Lectures given on Grammar Rules, Lexical Analysis, Compiler Process by Professor Razib Iqbal
 * **All members**: Past classes on Python for intermediate understanding of the language.
 * **Ali Bajwa**: Strong foundation on node tree traversal, applied to creating the parser.
 * **Cole Lawrence**: Past experience contributing to the [coffee-script](http://coffeescript.org/) and [CodeMirror](https://codemirror.net/) projects.

### Test Driven Development

A large focus of this project was to enable each developer to work independently on separate parts of the code base. Which enables each person to enable each person to work independent of the group. So, the test files were written in the first week of the project, [before any additional contributions](https://github.com/ZombieHippie/python-arithmetic-language/tree/7008475a00b6aed74534d6223f56c3e403d2cde3).

### Lexical Analysis (Tokenizer)

In the `run.py` file there is a [validator regex which matches only operators and numbers separated by spaces](https://github.com/ZombieHippie/python-arithmetic-language/blob/b4f9305042db3ef244dbdb884ceabdac0e0598c9/run.py#L13), so that the tokenizer will not fail to separate out the letters and numbers.

**Input**
```python
"90 - 1 / 5"
```

**Output**
```python
[
	{ 'type': 'number', 'value': 90 },
	{ 'type': 'operator', 'value': SUBTRACT },
	{ 'type': 'number', 'value': 1 },
	{ 'type': 'operator', 'value': DIVIDE },
	{ 'type': 'number', 'value': 5 }
]
```

### Abstract Syntax Tree[AST] Generator (Parser)

This part of the language is the functioning implementation of our grammar rules (detailed in `./Grammar rules.txt`).

**Input**
```python
[
	{ 'type': 'number', 'value': 90 },
	{ 'type': 'operator', 'value': SUBTRACT },
	{ 'type': 'number', 'value': 1 },
	{ 'type': 'operator', 'value': DIVIDE },
	{ 'type': 'number', 'value': 5 }
]
```

**Output**
```python
'ast': {
	'operator': SUBTRACT,
	'L': 90,
	'R': { 'operator': DIVIDE, 'L': 1, 'R': 5 }
}
```

> We notice that the Output AST looks very similar to just a Syntax Tree Diagram, this was enabled by Python's [`dict` (dictionary) data structure](https://docs.python.org/3.5/tutorial/datastructures.html#dictionaries)
> Using Python overall made this code very lightweight working with classes, and reduced the amount of structure needed to create the test cases.

### Evaluator

Here, we take the results of our AST and actualy do the computations. Using a visitor pattern, we wrote a recursive strategy to evaluate the deepest dictionaries first, and then travel up the structure to continue the operations.

**Input**
```python
'ast': {
	'operator': SUBTRACT,
	'L': 90,
	'R': { 'operator': DIVIDE, 'L': 1, 'R': 5 }
}
```

**Output**
```python
'eval': 89.8
```

### Trying it out

 1. Look over the `./tests.py` file to see more examples of inputs and outputs between each stage, and then reference each `arithmetic_<step>.py` file for the implementation.
 2. Read the `README.md` file for additional information about running the code, and testing.