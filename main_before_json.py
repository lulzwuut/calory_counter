# Dictionary with simple meal calories
calories = {
   'Hamburger': 600,
   'Cheese Burger': 750,
   'Veggie Burger': 400,
   'Vegan Burger': 350,
   'Sweet Potatoes': 230,
   'Salad': 15,
   'Iced Tea': 70,
   'Lemonade': 90,
}
# Dictionary with contents of combos
combos = {
    "Cheesy Combo" : ["Cheese Burger", "Sweet Potatoes", "Lemonade"],
    "Veggie Combo" : ["Veggie Burger", "Sweet Potatoes", "Iced Tea"],
    "Vegan Combo" : ["Vegan Burger", "Salad", "Lemonade"],
}

class MealTooBigError(Exception):
    """
    Raises an error if the input order contains more  than 2000 calories
    """
    def __init__(self, calories):
        self.calories = calories
        self.message = 'Your meal contains ' + str(calories) + ' calories. That\'s more than 2000!'
        super().__init__(self.message)

def count_calories(*args):
    """
    For a list of given items to be ordered, calculates how many calories it contains
    
    ------
    Input: 
        *args: List
            list of items that are keys either in the calories or combos dictionaries
    Return: 
        total_calories: int
            total calories of an order
    """
    
    total_calories = 0 
    # For each item in the input list, check if it is in the calories or in the combos dictionary.
    for meal in args:
        if calories.get(meal):
            # If it is in calories dictionary, then add the value for the given key to total_calories.
            total_calories += calories.get(meal)
        elif (combos.get(meal)):
            # If it is in the combos dictionary, then iterate over the input combo to get the meal keys and get their calory value from calories
            for submeal in combos.get(meal):
                total_calories += calories.get(submeal)
        else:
            # If item is not in either dictionaries, print error and reject the calculation.
            print(f'{meal} is not on the menu! Please correct your order.')
            break
    return total_calories

print(count_calories('Hamburger', 'Cheesy Combo'))

def count_recursive(menu_order, i, total_calories):
    """
    For a list of given items to be ordered, calculates how many calories it contains recursively.
    ------
    Input: 
        menu_order (list): list of items that are keys either in the calories or combos dictionaries
        i (int): iterator that guides the recursive calling of the function
        total_calories (int): total calories of an order, which is kept track of in the recursive calling of the function
    Return: 
        total_calories(int): total calories of an order
    """
    
    meal = menu_order[i]
    # For each item in the input list, check if it is in the calories or in the combos dictionary.
    if calories.get(meal):
        # If it is in calories dictionary, then add the value for the given key to total_calories.
        total_calories += calories.get(meal)
    elif (combos.get(meal)):
        # If it is in the combos dictionary, then iterate over the input combo to get the meal keys and get their calory value from calories
        for submeal in combos.get(meal):
            total_calories += calories.get(submeal)
    else:
        # If item is not in either dictionaries, print error and reject the calculation.
        print(meal + ' is not on the menu! Correct your order input.')
        return False
    if i+1 < len(menu_order):
        # If the last order item has not been reached, call the next iteration of count_recursive
        count_recursive(menu_order, i+1, total_calories)
        return total_calories
    else:
         # If the last order item has been reached, check if the total_calories is less than 2000.
        if (total_calories > 2000):
            # If it is more than 2000, raise MealTooBiggError
            raise MealTooBigError(total_calories)
        # If it is less than 2000, return total_calories of the order.
        print(total_calories)
        return total_calories

count_recursive(['Cheesy Combo', 'Cheesy Combo'], i=0, total_calories=0)
