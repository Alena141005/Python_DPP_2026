# Задание 4: Постройте сводную таблицу, где по строкам — region, по столбцам — product, а значения — общая сумма заказов (цена × количество).

import pandas as pd

users = pd.read_csv('data/users_new.csv', delimiter=',')
orders = pd.read_csv('data/orders_new.csv', delimiter=',')
df = users.merge(orders, on='user_id', how='left')

df['total_amount'] = df['price'] * df['quantity']

pivot = df.pivot_table(index='region', columns='product', values='total_amount', aggfunc='sum')

print(pivot)
