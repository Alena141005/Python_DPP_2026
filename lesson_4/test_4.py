# Задание 4
# Сгруппируйте данные по месяцу заказа и найдите общую выручку в каждом месяце.

import pandas as pd

df = pd.read_csv('data/group_orders.csv', delimiter=',')
df['order_date'] = pd.to_datetime(df['order_date'], format='%Y-%m-%d', errors='coerce')

df_filtered = df.groupby(df['order_date'].dt.to_period('M'))['total'].sum()

print(df_filtered)
