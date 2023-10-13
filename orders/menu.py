import json


f = open('orders/menu/meals.json')
meals = json.load(f)['meals']
f = open('orders/menu/combos.json')
combos = json.load(f)['combos']

# Remap the two dictionaries to be accessed with id
combos = {
    combo['id']: {'type': 'combo', **combo} for combo in combos
}
meals = {
    meal['id']: {'type': 'meal', **meal} for meal in meals
}
