import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_order_items=pd.read_csv('E-Commerce Dataset by Olist _ Dirty/olist_order_items_dataset.csv')

# print(df_order_items)

# some informations about order items table
# print(df_order_items.head(10))
# print('----------------------')

# print(df_order_items.tail(10))
# print('----------------------')

# print(df_order_items.info())
# print('----------------------')

# print(df_order_items.isna().sum())
# print('----------------------')

# print(df_order_items.describe(include='all'))
# print('----------------------')

# print(df_order_items.duplicated().sum())
# print('----------------------')

# cleaning & transformations
df_order_items['order_id']=df_order_items['order_id'].str.strip()

df_order_items['product_id']=df_order_items['product_id'].str.strip()

df_order_items['seller_id']=df_order_items['seller_id'].str.strip()

df_order_items['shipping_limit_date']=df_order_items['shipping_limit_date'].str.strip()


df_order_items['order_id']=df_order_items['order_id'].astype('string')

df_order_items['product_id']=df_order_items['product_id'].astype('string')

df_order_items['seller_id']=df_order_items['seller_id'].astype('string')

df_order_items['shipping_limit_date']=pd.to_datetime(df_order_items['shipping_limit_date'],format='%Y-%m-%d %H:%M:%S',errors='coerce')

df_order_items['total_price']=df_order_items['price'] + df_order_items['freight_value']

# check after cleaning & transformations
print(df_order_items.head(10))
print('----------------------')

# print(df_order_items.info())
# print('----------------------')

# print(df_order_items.describe(include='all'))
# print('----------------------')

# analysis
# print('The highest product in price')
# print(df_order_items.groupby('product_id')['price'].max().sort_values(ascending=False).head(1))
# print('---------------------------------------------------------')

# print('The most 10 products have ordered')
# print(df_order_items['product_id'].value_counts().head(10))
# print('---------------------------------------------------------')

# print('The most 10 sellers have sold products')
# print(df_order_items['seller_id'].value_counts().head(10))
# print('---------------------------------------------------------')

# print('total price for each order')
# print(df_order_items.groupby('order_id')['total_price'].sum().sort_values(ascending=False))
# print('---------------------------------------------------------')

# print('total revenue')
# print(df_order_items['total_price'].sum())
# print('---------------------------------------------------------')

# print('total orders')
# print(df_order_items['order_id'].count())
# print('---------------------------------------------------------')

df_order_items.to_csv('order_items_clean',index=False)