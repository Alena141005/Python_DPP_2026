# Задание 2
# Вывести все заказы на продукт "C" с суммой больше 250. Использовать query и арифметику.

import pandas as pd

users = pd.read_csv('data/users_new.csv', delimiter=',')
orders = pd.read_csv('data/orders_new.csv', delimiter=',')
df = users.merge(orders, on='user_id', how='left')

df_filtered = df.query("product=='C' and price>250")

df_filtered['total'] = df_filtered['price'] * df_filtered['quantity']
print(df_filtered[['order_id', 'user_id','product','price','quantity','order_date', 'total']])
