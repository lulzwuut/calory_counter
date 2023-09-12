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

combos = {
    combo['id']: {'type': 'combo', **combo} for combo in combos
}
meals = {
    meal['id']: {'type': 'meal', **meal} for meal in meals
}

class MealTooBigError(Exception):
    # Raised when the entered meal contains more than 2000 calories
    def __init__(self, calories):
        self.calories = calories
        self.message = 'Your meal contains ' + str(calories) + ' calories. That\'s more than 2000!'
        super().__init__(self.message)

def count_calories(menu_order, i, total_calories):
    meal = menu_order[i]
    if meals.get(meal):
        total_calories += meals.get(meal).get('calories')
    elif (combos.get(meal)):
        for submeal in combos.get(meal).get('meals'):
            total_calories += meals.get(submeal).get('calories')
    else:
        print(meal + ' is not on the menu!')
    if i+1 < len(menu_order):
        count_calories(menu_order, i+1, total_calories)
    else:
        if (total_calories > 2000):
            raise MealTooBigError(total_calories)
        print(total_calories)

def count_price(menu_order, i, total_price):
    meal = menu_order[i]
    if meals.get(meal):
        total_price += meals.get(meal).get('price')
    elif (combos.get(meal)):
        for submeal in combos.get(meal).get('meals'):
            total_price += meals.get(submeal).get('price')
    else:
        print(meal + ' is not on the menu!')
    if i+1 < len(menu_order):
        count_price(menu_order, i+1, total_price)
    else:
        print(total_price)

count_calories(['meal-1', 'combo-1', 'meal-8'], i=0, total_calories=0)
count_price(['meal-1', 'combo-1', 'meal-8'], i=0, total_price=0)