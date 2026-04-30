# Задание 2
# Найдите среднюю сумму заказа по каждому городу.

import pandas as pd

df = pd.read_csv('data/group_orders.csv', delimiter=',')

cities = df.groupby('city')['total'].mean()
print(cities)
