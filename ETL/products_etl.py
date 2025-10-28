import pandas as pd
import re
from unidecode import unidecode

# extraction
df_products=pd.read_csv('E-Commerce Dataset by Olist _ Dirty/olist_products_dataset.csv')

print(df_products)

# some informations about products table
print(df_products.head(10))
print('----------------------')

print(df_products.tail(10))
print('----------------------')

print(df_products.info())
print('----------------------')

print(df_products.isna().sum())
print('----------------------')

print(df_products.describe(include='all'))
print('----------------------')

print(df_products.duplicated().sum())
print('----------------------')

# cleaning & transformations
df_products=df_products.dropna(subset=['product_category_name'])

df_products=df_products.dropna(subset=['product_weight_g'])

df_products['product_id']=df_products['product_id'].str.strip()

df_products['product_category_name'] = (
    df_products['product_category_name']
    .apply(lambda x: unidecode(x) if isinstance(x, str) else x)  
    .apply(lambda x: re.sub(r"[^a-zA-Z'\s]", ' ', x))              
    .str.strip()
    .str.lower()
)

df_products['product_name_lenght']=df_products['product_name_lenght'].astype(int)

df_products['product_description_lenght']=df_products['product_description_lenght'].astype(int)

df_products['product_photos_qty']=df_products['product_photos_qty'].astype(int)

df_products['product_id']=df_products['product_id'].astype('string')

df_products['product_category_name']=df_products['product_category_name'].astype('string')

# check after cleaning & transformations
print(df_products.head(10))
print('----------------------')

print(df_products.info())
print('----------------------')

print(df_products.describe(include='all'))
print('----------------------')

# load
# df_products.to_csv('products_clean.csv',index=False)