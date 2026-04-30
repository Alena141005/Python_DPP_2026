# Задание_1
# Найдите всех пользователей из региона North, возраст которых младше 30, и
# определите общее количество заказов, сделанных ими.

import pandas as pd

users = pd.read_csv('data/users_new.csv', delimiter=',')
orders = pd.read_csv('data/orders_new.csv', delimiter=',')
df = users.merge(orders, on='user_id', how='left')

filtered = df.query("region=='North' and age<30")

result2 = filtered.groupby(['name']).agg({'order_id': 'count'})

print(result2.reset_index())
