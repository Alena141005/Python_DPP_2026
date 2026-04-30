#Задание_4
import pandas as pd

df = pd.read_csv('data/customers.csv', sep=',', encoding='utf-8')
df['birth_date'] = pd.to_datetime(df['birth_date'])

result = df[(df['gender'] == 'F') & (df['birth_date'].dt.year < 1995)]

print(result[['customer_id', 'first_name', 'last_name', 'birth_date']])
