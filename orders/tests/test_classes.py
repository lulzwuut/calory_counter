import datetime
import unittest
from orders.orders import Order


class MyTestCase(unittest.TestCase):
    """
    This unittest class tests if:
    - the Order class raises an error when the order contains more than 2000 calories
    - the counter functions (count_calories and count_price) return correct values for:
        - mixed orders (meals + combos)
        - long orders of single meals
    - the order_refused_reason attribute is correctly filled in case the order contains an item that is not on the menu
    """

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


# Create a test suite
test_suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)

# Create a text test runner and redirect the output to a text file
with open("orders/tests/test_results.txt", "a") as f:
    date = datetime.datetime.now()
    f.write(f"\n**********************************************************************\nTest run on: {date}\n")
    test_runner = unittest.TextTestRunner(stream=f, verbosity=2)
    result = test_runner.run(test_suite)

# Check if the tests were successful
if result.wasSuccessful():
    print("All tests passed!")
else:
    print("Some tests failed. Check 'test_results.txt' for details.")
