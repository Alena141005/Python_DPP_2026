#Задание_7
import pandas as pd

orders = pd.read_csv('data/orders.csv', sep=',', encoding='utf-8')
customers = pd.read_csv('data/customers.csv', sep=',', encoding='utf-8')

shop = orders.merge(customers, on='customer_id', how='inner')

clients_90s = shop[shop['birth_date'].str.contains('1990')]

print(clients_90s[['order_id', 'customer_id']])

