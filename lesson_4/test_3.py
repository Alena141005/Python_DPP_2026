# Задание_3
# Определите, какой товар продавался в наибольшем количестве (по сумме quantity).

import pandas as pd

df = pd.read_csv('data/group_orders.csv', delimiter=',')

cities = df.groupby('product')['quantity'].sum().sort_values(ascending=False)
print(cities.head(1))
