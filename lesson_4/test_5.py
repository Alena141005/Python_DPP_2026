# Задание_5
# Выведите топ-3 города с самой высокой средней стоимостью одного заказа (total).

import pandas as pd

df = pd.read_csv('data/group_orders.csv', delimiter=',')

cities = df.groupby('city')['total'].mean().sort_values(ascending=False)

print(cities.head(3))
