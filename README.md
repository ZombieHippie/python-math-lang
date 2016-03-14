# python-arithmetic-language

IMPORTANT: You can view this file and the files of this repository at https://github.com/ZombieHippie/python-arithmetic-language

## Demonstration of code

Run the command
```
python run.py
```

## Grammar rules

Please refer to the `Grammar rules.txt` file for grammar rules

## Contributions

Refer to this git repository for how each member contributed.

## Development getting started

 1. Install Python 3.x (default settings worked for me)

## To develop against this project

This project can be developed with a TDD attitude, by simply running the test script for your section of code each time you wish to test.

These tests need to pass, then we will string them together to complete the application.

### Developing the Tokenizer

While in the project folder.

Run the following command to run the `arithmetic_tokenizer.py` tests.
```sh
python test_tokenizer.py
```

### Developing the Parser

While in the project folder.

Run the following command to run the `arithmetic_parser.py` tests.
```sh
python test_parser.py
```

### Developing the Evaluator

While in the project folder.

Run the following command to run the `arithmetic_evaluator.py` tests.
```sh
python test_evaluator.py
```

### Overall testing

While in the project folder.

Run all tests with `test.cmd`.

## References

Throughout development the following posts may have been referenced for development.

 1. [Visitor Pattern in Python](https://chris-lamb.co.uk/posts/visitor-pattern-in-python) - Used for AST
 2. [Python Modules](https://docs.python.org/3/tutorial/modules.html) - General reference
 3. [Python Unittest](https://docs.python.org/3/library/unittest.html#unittest.TestCase.subTest) - Unittest reference documents