import datetime
import uuid
from orders.menu import meals, combos
from orders.exceptions import MealTooBigError


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
