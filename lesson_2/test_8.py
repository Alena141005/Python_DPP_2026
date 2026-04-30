#Задание_8
import pandas as pd

df = pd.read_csv('data/orders.csv', sep=',', encoding='utf-8')
df['order_date'] = pd.to_datetime(df['order_date'], format='%Y-%m-%d', errors='coerce')

orders_feb23 = df[((df['order_date'].dt.month == 2) & (df['order_date'].dt.year == 2023)) & (df['total'] > 5000)]

print(orders_feb23)

