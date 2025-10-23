import pandas as pd
import re
from unidecode import unidecode

# extraction
df_geolocation=pd.read_csv('E-Commerce Dataset by Olist _ Dirty/olist_geolocation_dataset.csv')

print(df_geolocation)

# some informations about geolocation table
print(df_geolocation.head(10))
print('----------------------')

print(df_geolocation.tail(10))
print('----------------------')

print(df_geolocation.info())
print('----------------------')

print(df_geolocation.isna().sum())
print('----------------------')

print(df_geolocation.describe(include='all'))
print('----------------------')

print(df_geolocation.duplicated().sum())
print('----------------------')

print(df_geolocation['geolocation_state'].unique())
print('----------------------')

print(df_geolocation[(df_geolocation['geolocation_lat'] < -90) | (df_geolocation['geolocation_lat'] > 90)])
print('----------------------')

print(df_geolocation[(df_geolocation['geolocation_lng'] < -180) | (df_geolocation['geolocation_lng'] > 180)])
print('----------------------')

# cleaning & transformations
df_geolocation['geolocation_zip_code_prefix']=df_geolocation['geolocation_zip_code_prefix'].apply(lambda x: str(x).zfill(5))
df_geolocation['geolocation_zip_code_prefix']=df_geolocation['geolocation_zip_code_prefix'].astype('string')
df_geolocation['geolocation_zip_code_prefix']=df_geolocation['geolocation_zip_code_prefix'].str.strip()

df_geolocation['geolocation_city'] = (
    df_geolocation['geolocation_city']
    .apply(lambda x: unidecode(x) if isinstance(x, str) else x)  
    .apply(lambda x: re.sub(r"[^a-zA-Z'\s]", '', x))              
    .str.strip()
    .str.lower()
)

df_geolocation['geolocation_state']=df_geolocation['geolocation_state'].str.strip()

df_geolocation=df_geolocation.drop_duplicates()


df_geolocation['geolocation_city']=df_geolocation['geolocation_city'].astype('string')
df_geolocation['geolocation_state']=df_geolocation['geolocation_state'].astype('category')

# check after cleaning & transformations
print(df_geolocation.head(10))
print('----------------------')

print(df_geolocation.info())
print('----------------------')

print(df_geolocation.describe(include='all'))
print('----------------------')

# clean file
df_geolocation.to_csv('geolocation_clean.csv',index=False)