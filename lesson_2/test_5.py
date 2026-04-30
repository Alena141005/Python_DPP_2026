#Задание_5
import pandas as pd

df = pd.read_csv('data/orders.csv', sep=',', encoding='utf-8')

result = df[df['total'] > 8000]

print(result[9:20][['order_id', 'customer_id', 'total']])

