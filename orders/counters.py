import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
from orders.menu import meals, combos
from orders.orders import Order

# Opening JSON file
f = open('data/orders_history.json')
data = json.load(f)

order_objects = []  # List to store the created Order objects
items_list = []     # List to sttore all the ordered items to analyse their "popularity" for the last part
for order in data['orders']:
    try:
        order_obj = Order(order['items'], order['date'])
        # Append all the Order objects to the list
        order_objects.append(order_obj)
        # Create a simple list enumerating all ordered meals/combos
        items_list.extend(order['items'])
    finally:
        continue


df = pd.DataFrame()

# Create a dataframe that contains the all Object attributes as separate columns for each order as separate row
print(len(order_objects))
for i in range(len(order_objects)):
    order_object = order_objects[i]
    d = {'order_id': str(order_object.order_id),
         'order_accepted': order_object.order_accepted,
         'order_refused_reason': order_object.order_refused_reason,
         'date': order_object.date, 'items': order_object.items,
         'calories': order_object.calories,
         'price': order_object.price}
    df = pd.concat([df, pd.DataFrame(d)], ignore_index=True)

# Plot the three plots in one figure
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharey=False, sharex=False)

# - Total calories per day
dates = df['date'].unique()
total_df = df.groupby('date', as_index=False).sum(numeric_only=True)
ax1.plot(total_df['date'], total_df['calories'])
ax1.set_xlabel('Date')
ax1.set_ylabel('Total Calories')

# - Total earnings per day
ax2.plot(total_df['date'], total_df['price'])
ax2.set_xlabel('Date')
ax2.set_ylabel('Total Earnings')

# - Average earnings by customer served per day
mean_df = df.groupby('date', as_index=False).mean(numeric_only=True)
ax3.plot(mean_df['date'], mean_df['price'])
ax3.set_xlabel('Date')
ax3.set_ylabel('Average Earnings')
plt.show()

# Create temporary variables to comparitively find the most ordered meal/combo and the most expensive one.
tmp_meal = 0
top_meal = ''
tmp_combo = 0
top_combo = ''
top_price = 0
top_item = ''

# For all unique occurences in the ordered items, check if it's a meal or a combo,
# then count how many times it occurs and check if it's higher than the previously saved top counter.
# Then use the meals/combos dictionaries to get the price of the item and use a similar comparison to find the most expensive item.
for meal in np.unique(items_list):
    if meal.find('meal') != -1:
        counter = items_list.count(meal)
        if counter > tmp_meal:
            tmp_meal = counter
            top_meal = meal
        price = meals.get(meal).get('price')
        if price > top_price:
            top_price = price
            top_item = meal
    elif meal.find('combo') != -1:
        counter = items_list.count(meal)
        if counter > tmp_combo:
            tmp_combo = counter
            top_combo = meal
        price = combos.get(meal).get('price')
        if price > top_price:
            top_price = price
            top_item = meal
print(f'Most ordered meal: {top_meal}. Ordered {tmp_meal} times.')
print(f'Most ordered combo: {top_combo}. Ordered {tmp_combo} times.')
print(f'Combo/meal that brought the most money: {top_item}. Total cost: {top_price}.')
