import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df_order_payments=pd.read_csv('E-Commerce Dataset by Olist _ Dirty/olist_order_payments_dataset.csv')

print(df_order_payments)

# some informations about order payments table
# print(df_order_payments.head(10))
# print('----------------------')

# print(df_order_payments.tail(10))
# print('----------------------')

# print(df_order_payments.info())
# print('----------------------')

# print(df_order_payments.isna().sum())
# print('----------------------')

# print(df_order_payments.describe(include='all'))
# print('----------------------')

# print(df_order_payments.duplicated().sum())
# print('----------------------')

# print(df_order_payments['payment_type'].unique())
# print('----------------------')

# cleaning & transformations
df_order_payments['order_id']=df_order_payments['order_id'].str.strip()
df_order_payments['payment_type']=df_order_payments['payment_type'].str.strip().str.lower()
df_order_payments['payment_type']=df_order_payments['payment_type'].replace(['credit_card','debit_card','not_defined'],['credit card','debit card',np.nan])
df_order_payments=df_order_payments.dropna(subset=['payment_type'])

df_order_payments['order_id']=df_order_payments['order_id'].astype('string')
df_order_payments['payment_type']=df_order_payments['payment_type'].astype('category')

# check after cleaning & transformations
# print(df_order_payments.head(10))
# print('----------------------')

# print(df_order_payments.info())
# print('----------------------')
