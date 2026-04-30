# Решать задания необходимо по файлам users_new.csv и orders_new.csv
# Задание 1: Найдите всех пользователей из региона North, возраст которых младше 30, и
# определите общее количество заказов, сделанных ими.

import pandas as pd

users = pd.read_csv('data/users_new.csv', delimiter=',')
orders = pd.read_csv('data/orders_new.csv', delimiter=',')
df = users.merge(orders, on='user_id', how='left')

df_filtered = df.query("region=='North' and age<30")

result2 = df_filtered.groupby(['name']).agg({'order_id': 'count'})

print(result2.reset_index())
