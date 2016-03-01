from operators import *

tests = [
	{
		'source': "4 * 5 + 1",
		'tokens': [
			{ 'type': 'number', 'value': 4 },
			{ 'type': 'operator', 'value': MULTIPLY },
			{ 'type': 'number', 'value': 5 },
			{ 'type': 'operator', 'value': ADD },
			{ 'type': 'number', 'value': 1 }
		],
		'ast': {
			'operator': MULTIPLY,
			'L': 4,
			'R': { 'operator': ADD, 'L': 5, 'R': 1 }
		},
		'eval': 21
	},
	{
		'source': "90 - -1 - 5",
		'tokens': [
			{ 'type': 'number', 'value': 90 },
			{ 'type': 'operator', 'value': SUBTRACT },
			{ 'type': 'number', 'value': -1 },
			{ 'type': 'operator', 'value': SUBTRACT },
			{ 'type': 'number', 'value': 5 }
		],
		'ast': {
			'operator': SUBTRACT,
			'L': { 'operator': SUBTRACT, 'L': 90, 'R': -1 },
			'R': 5
		},
		'eval': 86
	},
	{
		'source': "90 * -1 * 5",
		'tokens': [
			{ 'type': 'number', 'value': 90 },
			{ 'type': 'operator', 'value': MULTIPLY },
			{ 'type': 'number', 'value': -1 },
			{ 'type': 'operator', 'value': MULTIPLY },
			{ 'type': 'number', 'value': 5 }
		],
		'ast': {
			'operator': MULTIPLY,
			'L': { 'operator': MULTIPLY, 'L': 90, 'R': -1 },
			'R': 5
		},
		'eval': -450
	},
	{
		'source': "90 / 1 / 5",
		'tokens': [
			{ 'type': 'number', 'value': 90 },
			{ 'type': 'operator', 'value': DIVIDE },
			{ 'type': 'number', 'value': 1 },
			{ 'type': 'operator', 'value': DIVIDE },
			{ 'type': 'number', 'value': 5 }
		],
		'ast': {
			'operator': DIVIDE,
			'L': { 'operator': DIVIDE, 'L': 90, 'R': 1 },
			'R': 5
		},
		'eval': 18
	},
	{
		'source': "1 / 5 - 90",
		'tokens': [
			{ 'type': 'number', 'value': 1 },
			{ 'type': 'operator', 'value': DIVIDE },
			{ 'type': 'number', 'value': 5 },
			{ 'type': 'operator', 'value': SUBTRACT },
			{ 'type': 'number', 'value': 90 }
		],
		'ast': {
			'operator': SUBTRACT,
			'L': { 'operator': DIVIDE, 'L': 1, 'R': 5 },
			'R': 90
		},
		'eval': -89.8
	},
	{
		'source': "90 - 1 / 5",
		'tokens': [
			{ 'type': 'number', 'value': 90 },
			{ 'type': 'operator', 'value': SUBTRACT },
			{ 'type': 'number', 'value': 1 },
			{ 'type': 'operator', 'value': DIVIDE },
			{ 'type': 'number', 'value': 5 }
		],
		'ast': {
			'operator': SUBTRACT,
			'L': 90,
			'R': { 'operator': DIVIDE, 'L': 1, 'R': 5 }
		},
		'eval': 89.8
	},
	{
		'source': "905",
		'tokens': [
			{ 'type': 'number', 'value': 905 }
		],
		'ast': 905,
		'eval': 905
	},
	{
		'source': "-49",
		'tokens': [
			{ 'type': 'number', 'value': -49 }
		],
		'ast': -49,
		'eval': -49
	}
]