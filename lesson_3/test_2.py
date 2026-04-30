# Задание_2
# Выполните фильтрацию с помощью .query(). Отберите все записи продаж пользователей , 
# прошедших регистрацию начиная с 2022 года и совершивших заказы в 2023 году на сумму более 30000 руб. 
# Оставьте поля с ФИО и total. Подсчитайте количество таких продаж.

import pandas as pd

customers = pd.read_csv('data/customers.csv', sep=',', encoding='utf-8')
contacts = pd.read_csv('data/contacts.csv', sep=',', encoding='utf-8')
orders = pd.read_csv('data/orders.csv', sep=',', encoding='utf-8')

contacts['customer_id'] = pd.to_numeric(contacts['customer_id'], errors='coerce')

customers_contacts = customers.merge(contacts, on='customer_id', how='inner')
full_table = customers_contacts.merge(orders, on='customer_id', how='inner')

full_table['registration_date'] = pd.to_datetime(full_table['registration_date'], errors='coerce')
full_table['order_date'] = pd.to_datetime(full_table['order_date'], errors='coerce')

filtered = full_table[
    (full_table['registration_date'].dt.year >= 2022) &
    (full_table['order_date'].dt.year == 2023) &
    (full_table['total'] > 30000)
]

result = filtered[['first_name', 'last_name', 'total']]
print(result)
print(f"\nКоличество продаж: {len(result)}")