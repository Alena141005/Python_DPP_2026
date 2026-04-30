#Задание_2
import pandas as pd

df = pd.read_csv('data/orders.csv', sep=',', encoding='utf-8')
# df['order_date'] = pd.to_datetime(df['order_date'])

filt_df = df[(df['order_id'] >= 68) & (df['order_id'] <= 88)]
filt_df = filt_df[filt_df['order_date'].str.contains('2022')]

print(filt_df[4:10][['order_id', 'total']])
