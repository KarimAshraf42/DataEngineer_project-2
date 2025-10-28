import pandas as pd
import re
from unidecode import unidecode

# extraction
df_product_category_name_translation=pd.read_csv('E-Commerce Dataset by Olist _ Dirty/product_category_name_translation.csv')

print(df_product_category_name_translation)

# some informations about product_category_name_translation table
print(df_product_category_name_translation.head(10))
print('----------------------')

print(df_product_category_name_translation.tail(10))
print('----------------------')

print(df_product_category_name_translation.info())
print('----------------------')

print(df_product_category_name_translation.isna().sum())
print('----------------------')

print(df_product_category_name_translation.describe(include='all'))
print('----------------------')

print(df_product_category_name_translation.duplicated().sum())
print('----------------------')

# cleaning & transformations
df_product_category_name_translation['product_category_name'] = (
    df_product_category_name_translation['product_category_name']
    .apply(lambda x: unidecode(x) if isinstance(x, str) else x)  
    .apply(lambda x: re.sub(r"[^a-zA-Z'\s]", ' ', x))              
    .str.strip()
    .str.lower()
)

df_product_category_name_translation['product_category_name_english'] = (
    df_product_category_name_translation['product_category_name_english']
    .apply(lambda x: unidecode(x) if isinstance(x, str) else x) 
    .apply(lambda x: re.sub(r"[^a-zA-Z'\s]", ' ', x))              
    .str.strip()
    .str.lower()
)


df_product_category_name_translation['product_category_name']=df_product_category_name_translation['product_category_name'].astype('string')
df_product_category_name_translation['product_category_name_english']=df_product_category_name_translation['product_category_name_english'].astype('string')

# check after cleaning & transformations
print(df_product_category_name_translation.head(10))
print('----------------------')

print(df_product_category_name_translation.info())
print('----------------------')

print(df_product_category_name_translation.describe(include='all'))
print('----------------------')

# load
# df_product_category_name_translation.to_csv('product_category_name_translation_clean.csv',index=False)