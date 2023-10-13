# Calory Counter
Advanced level project for Python course @LPI
## Description of the repository structure:
1. **main.py**: this file contains the solutions to the tasks as provided on Notion, up until the 'Use OOP logic to handle orders'. This is the basic class-less file with functions aimed at evaluating input orders. This file is executable from VS Code.
2. **data**: this file contains the orders_history.json file that is used in counters.py for analysis of the order history.
3. **orders**: this folder contains all functionality related to processing tests.
    1. **menu**: this folder contains combos and meals json files that describe the composition, pricing and calories for possible input meals.
    2. **tests**: this folder contains the files for unit testing.
        * **test_classes.py:**: this file contains the unit testing classes that are necessary to test the correct functioning of the methods of the Object class.
        * **test_results.txt**: this file saves the results of a unit test run. Every run is appended to the end of the file with the date.
    3. **counters.py**: this file contains the analysis of orders_history.json file using pandas, numpy and matplotlib libraries. executable in Terminal with python -m orders.counters
    4. **exceptions.py**: contains the MealTooBigError exception, which is called when an order contains more than 2000 calories.
    5. **menu.py**: this file extracts the data from the meals and combos json files contained, then reformats them as dictionaries.
    6. **orders.py**: this file contains the Order class, which implements the logic from main.py into an Order class with methods and attributes.
## Documentation
* The unit tests are performed in Terminal with: python -m unittest
* The orders_history.json analysis is performed in Terminal with the command: python -m orders.counters
* main.py has to be run from a development environment with the input order of interest

