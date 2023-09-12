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
def count_calories(*args):
    total_calories = 0;
    for meal in args:
        if calories.get(meal):
            total_calories += calories.get(meal)
        elif (combos.get(meal)):
            for submeal in combos.get(meal):
                total_calories += calories.get(submeal)
        else:
            print('This meal is not on the menu!')
    return total_calories

print(count_calories('Cheesy Combo'))