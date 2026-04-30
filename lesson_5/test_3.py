# Задание_3
# Посчитайте, сколько раз каждый продукт заказывался. Используйте value_counts.

import pandas as pd

users = pd.read_csv('data/users_new.csv', delimiter=',')
orders = pd.read_csv('data/orders_new.csv', delimiter=',')
df = users.merge(orders, on='user_id', how='left')

print(df['product'].value_counts().reset_index(name='order_count'))
