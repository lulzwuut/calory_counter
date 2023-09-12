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
combos = {
    "Cheesy Combo" : ["Cheese Burger", "Sweet Potatoes", "Lemonade"],
    "Veggie Combo" : ["Veggie Burger", "Sweet Potatoes", "Iced Tea"],
    "Vegan Combo" : ["Vegan Burger", "Salad", "Lemonade"],
}

class MealTooBigError(Exception):
    # Raised when the entered meal contains more than 2000 calories
    def __init__(self, calories):
        self.calories = calories
        self.message = 'Your meal contains ' + str(calories) + ' calories. That\'s more than 2000!'
        super().__init__(self.message)

def count_calories(*args):
    total_calories = 0;
    for meal in args:
        if calories.get(meal):
            total_calories += calories.get(meal)
        elif (combos.get(meal)):
            for submeal in combos.get(meal):
                total_calories += calories.get(submeal)
        else:
            print('This item is not on the menu!')
    return total_calories

def count_recursive(menu_order, i, total_calories):
    meal = menu_order[i]
    if calories.get(meal):
        total_calories += calories.get(meal)
    elif (combos.get(meal)):
        for submeal in combos.get(meal):
            total_calories += calories.get(submeal)
    else:
        print(meal + ' is not on the menu!')
    if i+1 < len(menu_order):
        count_recursive(menu_order, i+1, total_calories)
    else:
        if (total_calories > 2000):
            raise MealTooBigError(total_calories)
        print(total_calories)

count_recursive(['Cheesy Combo', 'Cheesy Combo'], i=0, total_calories=0)



