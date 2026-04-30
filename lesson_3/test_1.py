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

# print(contacts.info())
# print(customers.info())
# print(orders.info())

merged = customers.merge(contacts, on='customer_id', how='inner')
df = merged.merge(orders, on='customer_id', how='left')

europ = ['Italy', 'Spain', 'UK', 'France', 'Germany', 'Russia']

df['order_date'] = pd.to_datetime(df['order_date'], format='%Y-%m-%d %H:%M:%S', errors='coerce')


# With []
task_2 = df[
         ((df['order_date'].dt.year == 2023) & (df['order_date'].dt.month <= 6))
         & ((df['country'].isin(europ)) | (df['country'] == 'Russia'))
         ] [['order_id', 'total']]

# With .loc()
task_1 = df.loc[
        ((df['order_date'].dt.year == 2023) & (df['order_date'].dt.month <= 6)) 
        & ((df['country'].isin(europ)) | (df['country'] == 'Russia')), 
        ['order_id', 'total']
        ]

# With .query()
df['year'] = df['order_date'].dt.year
df['month'] = df['order_date'].dt.month

task_3 = df.query('year == 2023 and month <= 6 and country.isin(@europ)')[['order_id', 'total']]


print(sum(task_1['total']))
print(sum(task_2['total']))
print(sum(task_3['total']))
