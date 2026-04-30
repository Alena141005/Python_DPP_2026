# Задание_5
# Найдите пользователей, сделавших более 1 заказа, и выведите их имена и количество заказов.

import pandas as pd

users = pd.read_csv('data/users_new.csv', delimiter=',')
orders = pd.read_csv('data/orders_new.csv', delimiter=',')
df = users.merge(orders, on='user_id', how='left')

counts = df['name'].value_counts()
print(counts[counts>1].reset_index(name='order_count'))
