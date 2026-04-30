# Задание_2
# Методом value_counts() подсчитайте сколько заказов 
# в период 2022-2023 годов было осуществлено пользователями 
# мужского пола и сколько пользователями женского пола.

import pandas as pd

customers = pd.read_csv('data/customers.csv', sep=',', encoding='utf-8')
contacts = pd.read_csv('data/contacts.csv', sep=',', encoding='utf-8')
orders = pd.read_csv('data/orders.csv', sep=',', encoding='utf-8')

contacts['customer_id'] = pd.to_numeric(contacts['customer_id'], errors='coerce')

# print(contacts.info())
# print(customers.info())
# print(orders.info())

customers_contacts = customers.merge(contacts, on='customer_id', how='inner')
full_table = customers_contacts.merge(orders, on='customer_id', how='inner')

full_table['order_date'] = pd.to_datetime(full_table['order_date'], errors='coerce')

mask = full_table['order_date'].dt.year.isin([2022, 2023])
filtered = full_table[mask]
gender_counts = filtered['gender'].value_counts()

print(gender_counts)
