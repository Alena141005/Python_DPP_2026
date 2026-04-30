import pandas as pd

df = pd.read_csv('data/products.csv', sep=',', encoding='utf-8')

result = df[(df['price'] < 500) & (df['volume_ml'] == 5.0)]

print(result[['product_name', 'price']])

