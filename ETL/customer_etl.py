import pandas as pd
import matplotlib.pyplot as plt
import re
from unidecode import unidecode

# extraction
df_customers=pd.read_csv('E-Commerce Dataset by Olist _ Dirty/olist_customers_dataset.csv')

print(df_customers)

# some informations about customers table
print(df_customers.head(10))
print('----------------------')

print(df_customers.tail(10))
print('----------------------')

print(df_customers.info())
print('----------------------')

print(df_customers.isna().sum())
print('----------------------')

print(df_customers.describe(include='all'))
print('----------------------')

print(df_customers.duplicated().sum())
print('----------------------')

print(df_customers['customer_state'].unique())
print('----------------------')

# cleaning & transformations
df_customers['customer_id']=df_customers['customer_id'].str.strip()

df_customers['customer_unique_id']=df_customers['customer_unique_id'].str.strip()


df_customers['customer_zip_code_prefix']=df_customers['customer_zip_code_prefix'].apply(lambda x: str(x).zfill(5))
df_customers['customer_zip_code_prefix']=df_customers['customer_zip_code_prefix'].astype('string')
df_customers['customer_zip_code_prefix']=df_customers['customer_zip_code_prefix'].str.strip()

df_customers['customer_city'] = (
    df_customers['customer_city']
    .apply(lambda x: unidecode(x) if isinstance(x, str) else x)  
    .apply(lambda x: re.sub(r"[^a-zA-Z'\s]", '', x))              
    .str.strip()
    .str.lower()
)

df_customers['customer_state']=df_customers['customer_state'].str.strip()


df_customers['customer_id']=df_customers['customer_id'].astype('string')

df_customers['customer_unique_id']=df_customers['customer_unique_id'].astype('string')

df_customers['customer_city']=df_customers['customer_city'].astype('string')

df_customers['customer_state']=df_customers['customer_state'].astype('category')

# check after cleaning & transformations
print(df_customers.head(10))
print('----------------------')

print(df_customers.info())
print('----------------------')

print(df_customers.describe(include='all'))
print('----------------------')

# load
# df_customers.to_csv('customer_clean.csv',index=False)