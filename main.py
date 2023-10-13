from orders.menu import meals, combos
from orders.exceptions import MealTooBigError


def count_calories(menu_order, i, total_calories):
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
    # For each item in the input list, check if it is in the calories or in the combos dictionary.
    if meals.get(meal):
        # If it is in calories dictionary, then add the value for the given key to total_calories.
        total_calories += meals.get(meal).get('calories')
    elif (combos.get(meal)):
        # If it is in the combos dictionary, then iterate over the input combo to get the meal keys and get their calory value from calories
        for submeal in combos.get(meal).get('meals'):
            total_calories += meals.get(submeal).get('calories')
    else:
        # If item is not in either dictionaries, print error and reject the calculation.
        print(meal + ' is not on the menu! Correct your order input.')
        return False
    if i+1 < len(menu_order):
        # If the last order item has not been reached, call the next iteration of count_recursive
        count_calories(menu_order, i+1, total_calories)
        return total_calories
    else:
        # If the last order item has been reached, check if the total_calories is less than 2000.
        if (total_calories > 2000):
            # If it is more than 2000, raise MealTooBiggError
            raise MealTooBigError(total_calories)
        else:
            # If it is less than 2000, return total_calories of the order.
            return total_calories


def count_price(menu_order, i, total_price):
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
        print(meal + ' is not on the menu!')
    if i+1 < len(menu_order):
        count_price(menu_order, i+1, total_price)
        return total_price
    else:
        total_calories = int(str(count_calories(menu_order, i=0, total_calories=0)))  # This is used to get the last return of the recursive function.
        if (total_calories > 2000):
            raise MealTooBigError(total_calories)
        return total_price


print(count_calories(['meal-1', 'combo-1', 'meal-8'], i=0, total_calories=0))
print(count_price(['combo-1', 'combo-2'], i=0, total_price=0))
