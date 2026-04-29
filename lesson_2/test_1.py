import pandas as pd

df = pd.read_csv('orders.csv', sep=',', encoding='utf-8')

filt_df = df[(df['total'] >= 30) & (df['total'] <= 40)]
filt_df = filt_df[filt_df['order_date'] >= '2024-01-01']

print(filt_df[['order_id']])


