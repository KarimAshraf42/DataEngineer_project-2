import pandas as pd
import os

customers=pd.read_csv('E-Commerce Dataset by Olist _ Clean/customer_clean.csv')

geolocation=pd.read_csv('E-Commerce Dataset by Olist _ Clean/geolocation_clean.csv')

order_items=pd.read_csv('E-Commerce Dataset by Olist _ Clean/order_items_clean.csv')

order_payments=pd.read_csv('E-Commerce Dataset by Olist _ Clean/order_payments_clean.csv')

order_reviews=pd.read_csv('E-Commerce Dataset by Olist _ Clean/order_reviews_clean.csv')

orders=pd.read_csv('E-Commerce Dataset by Olist _ Clean/orders_clean.csv')

product_category_name_translation=pd.read_csv('E-Commerce Dataset by Olist _ Clean/product_category_name_translation_clean.csv')

products=pd.read_csv('E-Commerce Dataset by Olist _ Clean/products_clean.csv')

sellers=pd.read_csv('E-Commerce Dataset by Olist _ Clean/sellers_clean.csv')

# dimension tables
dim_customers = customers.copy()

# print(dim_customers)

dim_geolocation = geolocation.copy()

# print(dim_geolocation)

dim_products = pd.merge(
    products,
    product_category_name_translation,
    how='left',
    on='product_category_name'
)

# print(dim_products)

dim_sellers = sellers.copy()

# print(dim_sellers)

# fact tables
fact_orders_items = pd.merge(
    orders,
    order_items,
    how='left',
    on='order_id'
)

# print(fact_orders_items)

fact_orders_payments= pd.merge(
    fact_orders_items,
    order_payments,
    how='left',
    on='order_id'
)

# print(fact_orders_payments)

fact_orders_reviews = pd.merge(
    fact_orders_payments,
    order_reviews,
    how='left',
    on='order_id'
)

# print(fact_orders_reviews)

fact_orders_products = pd.merge(
    fact_orders_reviews,
    dim_products,
    how='left',
    on='product_id'
)

# print(fact_orders_products)

fact_orders_customers = pd.merge(
    fact_orders_products,
    dim_customers,
    how='left',
    on='customer_id'
)

# print(fact_orders_customers)

fact_orders_full = pd.merge(
    fact_orders_customers,
    dim_sellers,
    how='left',
    on='seller_id',
    suffixes=('_customer', '_seller')
)

# print(fact_orders_full)

# fact & dimension tables
dim_customers.to_csv('Warehouse/dim_customers.csv', index=False)

dim_geolocation.to_csv('Warehouse/dim_geolocation.csv', index=False)

dim_products.to_csv('Warehouse/dim_products.csv', index=False)

dim_sellers.to_csv('Warehouse/dim_sellers.csv', index=False)

fact_orders_items.to_csv('Warehouse/fact_orders_items.csv', index=False)

fact_orders_payments.to_csv('Warehouse/fact_orders_payments.csv', index=False)

fact_orders_reviews.to_csv('Warehouse/fact_orders_reviews.csv', index=False)

fact_orders_products.to_csv('Warehouse/fact_orders_products.csv', index=False)

fact_orders_customers.to_csv('Warehouse/fact_orders_customers.csv', index=False)

fact_orders_full.to_csv('Warehouse/fact_orders_full.csv', index=False)






