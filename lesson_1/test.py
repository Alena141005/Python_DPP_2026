
#ДЗ №3
print("Hello, World!")

#Задание_1
import pandas as pd

contacts = pd.read_csv('contacts.csv', sep=',', encoding='utf-8')
customers = pd.read_csv('customers.csv', sep=',', encoding='utf-8')
orders = pd.read_csv('orders.csv', sep=',', encoding='utf-8')

customers_info = customers.merge(contacts, on='customer_id', how='left')
df = customers_info.merge(orders, on='customer_id', how='inner')

df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
europ = ['France', 'Germany', 'Italy', 'UK', 'Spain']

# With .loc()
task1 = df.loc[
        ((df['order_date'].dt.year == 2023) & (df['order_date'].dt.month <= 6)) 
        & ((df['country'].isin(europ)) | (df['country'] == 'Russia')), 
        ['order_id', 'total']
        ]

# # With []
# task2 = df[
#          ((df['order_date'].dt.year == 2023) & (df['order_date'].dt.month <= 6))
#          & ((df['country'].isin(europ)) | (df['country'] == 'Russia'))
#          ] [['order_id', 'total']]

# # With .query()
# df['year'] = df['order_date'].dt.year
# df['month'] = df['order_date'].dt.month
# df['in_europ'] = df['country'].isin(europ)

# task3 = df.query('year == 2023 and month <= 6 and (in_europ or country == "Russia")')[['order_id', 'total']]


print(task1.sum())
# print(task2.sum())
# print(task3.sum())

# df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
# year = df['order_date'].dt.year 
# month = df['order_date'].dt.month
# mask = 

# df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
# date = (df['order_date'].dt.month < 6) & (df['order_date'].dt.year == 2023)
# europ = ['France', 'Germany', 'Italy', 'UK', 'Spain']
# europeans = df.query('country == europ and order_date == date')

# print(europeans.loc[:, 'order_id', 'total'].sum())

#Задание_2
#import pandas as pd


#Задание_3

