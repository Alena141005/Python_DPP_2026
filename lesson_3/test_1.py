# Задание_1 
# Выполните фильтрацию с помощью [ ], .loc[] и .query().
# Объедините таблицы contacts, customers, orders. Будьте внимательны, не все
# пользователи делали заказы.
# Отберите все записи о продажах пользователей из европейских стран и России,
# совершенных в первые два квартала 2023 года. Оставьте поля order_id и total.
# Определите сумму отобранных продаж.
# Сумма продаж: 659255.0

import pandas as pd

contacts = pd.read_csv('data/contacts.csv', delimiter=',')
customers = pd.read_csv('data/customers.csv', delimiter=',')
orders = pd.read_csv('data/orders.csv', delimiter=',')

contacts['customer_id'] = pd.to_numeric(contacts['customer_id'], errors='coerce')


countries_to_filter = ['Italy', 'Spain', 'UK', 'France', 'Germany', 'Russia']

# print(contacts.info())
# print(customers.info())
# print(orders.info())

merged = customers.merge(contacts, on='customer_id', how='inner')
df = merged.merge(orders, on='customer_id', how='left')
df['order_date'] = pd.to_datetime(df['order_date'], format='%Y-%m-%d %H:%M:%S', errors='coerce')

filter_1 = df[(df['country'].isin(countries_to_filter)) & (df['order_date']>= '2023-01-01') & (df['order_date'] <= '2023-06-30')]
filter_2 = df.loc[(df['country'].isin(countries_to_filter)) &  (df['order_date']>= '2023-01-01') & (df['order_date'] <= '2023-06-30')]
filter_3 = df.query("(country in @countries_to_filter) and (order_date >= '2023-01-01') and (order_date <= '2023-06-30')")

print(sum(filter_1['total']))
print(sum(filter_2['total']))
print(sum(filter_3['total']))

