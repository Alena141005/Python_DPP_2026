# Задание 1
# Используйте файл group_orders.csv. Посчитайте общее количество заказов в каждом
# городе.

import pandas as pd

df = pd.read_csv('data/group_orders.csv', delimiter=',')

#print(df.info())
cities = df.groupby('city')['order_id'].count()
print(cities)
