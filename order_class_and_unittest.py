import datetime
import uuid

# Dictionary with simple meal calories, names and prices
meals = [
    {
        "id": "meal-1",
        "name": "hamburger",
        "calories": 600,
        "price": 5
    },
    {
        "id": "meal-2",
        "name": "cheese burger",
        "calories": 750,
        "price": 7},
    {
        "id": "meal-3",
        "name": "veggie burger",
        "calories": 400,
        "price": 6},
    {
        "id": "meal-4",
        "name": "vegan burger",
        "calories": 350,
        "price": 6},
    {
        "id": "meal-5",
        "name": "sweet potatoes",
        "calories": 230,
        "price": 3},
    {
        "id": "meal-6",
        "name": "salad",
        "calories": 15,
        "price": 4},
    {
        "id": "meal-7",
        "name": "iced tea",
        "calories": 70,
        "price": 2},
    {
        "id": "meal-8",
        "name": "lemonade",
        "calories": 90,
        "price": 2
    },
]

# Dictionary with combo contents, names and prices
combos = [
    {
        "id": "combo-1",
        "name": "cheesy combo",
        "meals": ["meal-2", "meal-5", "meal-8"],
        "price": 11,
    },
    {
        "id": "combo-2",
        "name": "veggie combo",
        "meals": ["meal-3", "meal-5", "meal-7"],
        "price": 10,
    },
    {
        "id": "combo-3",
        "name": "vegan combo",
        "meals": ["meal-4", "meal-6", "meal-8"],
        "price": 10,
    },

]

# Remap the two dictionaries to be accessed with id
combos = {
    combo['id']: {'type': 'combo', **combo} for combo in combos
}
meals = {
    meal['id']: {'type': 'meal', **meal} for meal in meals
}

class Order:
    """
    This class represents an order.

    Arguments:
        items (list): A list of item ids.
        date (datetime): The date and time of the order.

    Class attributes:
        counter (int): A counter for the number of orders.

    Attributes:
        order_id (str): A unique identifier for the order.
        order_accepted (bool): Whether or not the order was accepted.
        order_refused_reason (str): The reason the order was refused.
        date (datetime): The date and time of the order.
        items (list): A list of item ids.

    Properties:
        calories (int): The total calories for the order.
        price (int): The total price for the order.
    """
    counter = 0

    def __init__(self, items, date=datetime.datetime.now()):
        self.order_id = uuid.uuid4()
        self.order_accepted = True
        self.order_refused_reason = ''
        self.date = date
        self.items = items
        calories = self.calories
        if calories > 2000:
            raise MealTooBigError(calories)

    @property
    def calories(self):
        test = self.count_calories(self.items, i=0, total_calories=0)
        return test

    def count_calories(self, menu_order, i, total_calories):
        """
        For a list of given items to be ordered, calculates how many calories it contains recursively.
        ------
        Input: 
            menu_order: List
                list of items that are keys either in the calories or combos dictionaries
            i: int
                iterator that guides the recursive calling of the function
            total_calories: int
                total calories of an order, which is kept track of in the recursive calling of the function
        Return: 
            total_calories: int
                total calories of an order
        """
        
        meal = menu_order[i]
        if meals.get(meal):
            total_calories += meals.get(meal).get('calories')
        elif (combos.get(meal)):
            for submeal in combos.get(meal).get('meals'):
                total_calories += meals.get(submeal).get('calories')
        else:
            self.order_refused_reason = f'{meal} is not on the menu!'
            self.order_accepted = False
        if i+1 < len(menu_order):
            return self.count_calories(menu_order, i+1, total_calories)
        else:
            if (total_calories > 2000):
                self.order_refused_reason = 'Your meal contains ' + str(total_calories) + ' calories. That\'s more than 2000!'
                self.order_accepted = False
            return total_calories
    
    @property
    def price(self):
        test = self.count_price(self.items, i=0, total_price=0)
        return test

    def count_price(self, menu_order, i, total_price):
        """
        This function is fully analogous to count_calories, with two exceptions:
        1) it gets the price value of a given order item
        2) the combos dictionary contains the prices for combos, so it is not necessary to iterate over combo contents
        
        For a detailed explanation of the function's structure refer to the description of count_calories.
        """
        meal = menu_order[i]
        if meals.get(meal):
            total_price += meals.get(meal).get('price')
        elif (combos.get(meal)):
            total_price += combos.get(meal).get('price')
        else:
            self.order_refused_reason = f'{meal} is not on the menu!'
        if i+1 < len(menu_order):
            return self.count_price(menu_order, i+1, total_price)
        else:
            return total_price

class MealTooBigError(Exception):
    """
    Raises an error if the input order contains more  than 2000 calories.
    """
    def __init__(self, calories):
        self.calories = calories
        self.message = 'Your meal contains ' + str(calories) + ' calories. That\'s more than 2000!'
        super().__init__(self.message)

# order1 = Order(['combo-2', 'combo-2', 'combo-2'], datetime.datetime.now())
# print(order1.calories)

import unittest

class MyTestCase(unittest.TestCase):
    """
    This unittest class tests if:
    - the Order class raises an error when the order contains more than 2000 calories
    - the counter functions (count_calories and count_price) return correct values for:
        - mixed orders (meals + combos)
        - long orders of single meals
    - the order_refused_reason attribute is correctly filled in case the order contains an item that is not on the menu
    """
    
    def test_meal_too_big(self):
        # Check that the function raises an error
        with self.assertRaises(MealTooBigError):
            result = Order(['combo-2', 'combo-2', 'combo-2'])

    def test_calory_counter_combo(self):
        # Check that the function calculates calories correctly for an order that contains combos
        result = Order(['meal-1', 'combo-2']).calories
        self.assertEqual(result, 1300)

    def test_calory_counter_single(self):
        # Check that the function calculates calories correctly for an order that contains many single items
        result = Order(['meal-1', 'meal-2', 'meal-4', 'meal-5', 'meal-6']).calories
        self.assertEqual(result, 1945)

    def test_price_counter_combo(self):
        # Check that the function calculates price correctly for an order that contains combos
        result = Order(['meal-1', 'combo-2']).price
        self.assertEqual(result, 15)

    def test_price_counter_single(self):
        # Check that the function calculates price correctly for an order that contains many single items
        result = Order(['meal-1', 'meal-2', 'meal-4', 'meal-5', 'meal-6']).price
        self.assertEqual(result, 25)

    def test_item_not_on_menu(self):
        # Check that the function saves order_refused_reason if an entered item is not on the menu
        result = Order(['meal-123', 'meal-4', 'meal-5', 'meal-6']).order_refused_reason
        self.assertEqual(result, 'meal-123 is not on the menu!')
if __name__ == '__main__':
    unittest.main()
        
# Create a test suite
test_suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)

# Create a text test runner and redirect the output to a text file
with open("calory_counter/unit_tests/test_results.txt", "w") as f:
    test_runner = unittest.TextTestRunner(stream=f, verbosity=2)
    result = test_runner.run(test_suite)

# Check if the tests were successful
if result.wasSuccessful():
    print("All tests passed!")
else:
    print("Some tests failed. Check 'test_results.txt' for details.")