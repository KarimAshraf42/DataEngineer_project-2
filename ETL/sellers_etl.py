import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
from unidecode import unidecode

df_sellers=pd.read_csv('E-Commerce Dataset by Olist _ Dirty/olist_sellers_dataset.csv')

# print(df_sellers)

# some informations about sellers table
# print(df_sellers.head(10))
# print('----------------------')

# print(df_sellers.tail(10))
# print('----------------------')

# print(df_sellers.info())
# print('----------------------')

# print(df_sellers.isna().sum())
# print('----------------------')

# print(df_sellers.describe(include='all'))
# print('----------------------')

# print(df_sellers.duplicated().sum())
# print('----------------------')

# print(df_sellers['seller_state'].unique())
# print('----------------------')

# cleaning & transformations
df_sellers['seller_id']=df_sellers['seller_id'].str.strip()

df_sellers['seller_zip_code_prefix']=df_sellers['seller_zip_code_prefix'].apply(lambda x: str(x).zfill(5))
df_sellers['seller_zip_code_prefix']=df_sellers['seller_zip_code_prefix'].astype('string')
df_sellers['seller_zip_code_prefix']=df_sellers['seller_zip_code_prefix'].str.strip()

df_sellers['seller_city'] = (
    df_sellers['seller_city']
    .apply(lambda x: unidecode(x) if isinstance(x, str) else x)  
    .apply(lambda x: re.sub(r"[^a-zA-Z'\s]", ' ', x))              
    .str.strip()
    .str.lower()
)

df_sellers['seller_state']=df_sellers['seller_state'].str.strip()


df_sellers['seller_id']=df_sellers['seller_id'].astype('string')
df_sellers['seller_city']=df_sellers['seller_city'].astype('string')
df_sellers['seller_state']=df_sellers['seller_state'].astype('category')

# check after cleaning & transformations
print(df_sellers.head(10))
print('----------------------')

# print(df_sellers.info())
# print('----------------------')

# print(df_sellers.describe(include='all'))
# print('----------------------')

df_sellers.to_csv('sellers_clean',index=False)