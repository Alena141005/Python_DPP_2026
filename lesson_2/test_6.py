#Задание_6
import pandas as pd

df = pd.read_csv('data/orders.csv', sep=',', encoding='utf-8')

print(df[((df['total'] >= 10000) & (df['total'] <= 15000)) & 
         (df['order_date'].str.contains('2023'))][['order_id', 'total', 'order_date']])

