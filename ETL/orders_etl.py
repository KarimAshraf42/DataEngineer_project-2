import pandas as pd

# extraction
df_orders=pd.read_csv('E-Commerce Dataset by Olist _ Dirty/olist_orders_dataset.csv')

print(df_orders)

# some informations about orders table
print(df_orders.head(10))
print('----------------------')

print(df_orders.tail(10))
print('----------------------')

print(df_orders.info())
print('----------------------')

print(df_orders.isna().sum())
print('----------------------')

print(df_orders.describe(include='all'))
print('----------------------')

print(df_orders.duplicated().sum())
print('----------------------')

print(df_orders['order_status'].unique())
print('----------------------')

# cleaning & transformations
df_orders['order_id']=df_orders['order_id'].str.strip()

df_orders['customer_id']=df_orders['customer_id'].str.strip()

df_orders['order_status']=df_orders['order_status'].str.strip().str.lower()

df_orders['order_purchase_timestamp']=df_orders['order_purchase_timestamp'].str.strip()

df_orders['order_approved_at']=df_orders['order_approved_at'].str.strip()

df_orders['order_delivered_carrier_date']=df_orders['order_delivered_carrier_date'].str.strip()

df_orders['order_delivered_customer_date']=df_orders['order_delivered_customer_date'].str.strip()

df_orders['order_estimated_delivery_date']=df_orders['order_estimated_delivery_date'].str.strip()


df_orders['order_id']=df_orders['order_id'].astype('string')

df_orders['customer_id']=df_orders['customer_id'].astype('string')

df_orders['order_status']=df_orders['order_status'].astype('category')

df_orders['order_purchase_timestamp']=pd.to_datetime(df_orders['order_purchase_timestamp'],format='%Y-%m-%d %H:%M:%S',errors='coerce')

df_orders['order_approved_at']=pd.to_datetime(df_orders['order_approved_at'],format='%Y-%m-%d %H:%M:%S',errors='coerce')

df_orders['order_delivered_carrier_date']=pd.to_datetime(df_orders['order_delivered_carrier_date'],format='%Y-%m-%d %H:%M:%S',errors='coerce')

df_orders['order_delivered_customer_date']=pd.to_datetime(df_orders['order_delivered_customer_date'],format='%Y-%m-%d %H:%M:%S',errors='coerce')

df_orders['order_estimated_delivery_date']=pd.to_datetime(df_orders['order_estimated_delivery_date'],format='%Y-%m-%d %H:%M:%S',errors='coerce')

# check after cleaning & transformations
print(df_orders.head(10))
print('----------------------')

print(df_orders.info())
print('----------------------')

print(df_orders.describe(include='all'))
print('----------------------')

# analysis
print('total orders')
print(df_orders['order_id'].count())
print('------------------------------------------------')

print('number for each order status')
print(df_orders['order_status'].value_counts())
print('------------------------------------------------')

print('most day have ordered')
print(df_orders['order_purchase_timestamp'].dt.date.value_counts().head(1))
print('------------------------------------------------')

print('most delivery time day')
print((df_orders['order_delivered_customer_date'] - df_orders['order_purchase_timestamp']).dt.days.max())
print('------------------------------------------------')

print('least delivery time day')
print((df_orders['order_delivered_customer_date'] - df_orders['order_purchase_timestamp']).dt.days.min())
print('------------------------------------------------')

print('number of orders that not delivered')
print(df_orders['order_delivered_customer_date'].isna().sum())
print('------------------------------------------------')

print('number of orders late')
print(df_orders[df_orders['order_delivered_customer_date'] > df_orders['order_estimated_delivery_date']].shape[0])
print('------------------------------------------------')

# clean file
df_orders.to_csv('orders_clean.csv',index=False)