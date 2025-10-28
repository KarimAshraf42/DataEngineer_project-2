import pandas as pd
import re
from unidecode import unidecode

# extraction
df_order_reviews=pd.read_csv('E-Commerce Dataset by Olist _ Dirty/olist_order_reviews_dataset.csv')

print(df_order_reviews)

# some informations about order reviews table
print(df_order_reviews.head(10))
print('----------------------')

print(df_order_reviews.tail(10))
print('----------------------')

print(df_order_reviews.info())
print('----------------------')

print(df_order_reviews.isna().sum())
print('----------------------')

print(df_order_reviews.describe(include='all'))
print('----------------------')

print(df_order_reviews.duplicated().sum())
print('----------------------')

# cleaning & transformations
df_order_reviews['review_id']=df_order_reviews['review_id'].str.strip()
df_order_reviews['order_id']=df_order_reviews['order_id'].str.strip()
df_order_reviews['review_comment_title']=df_order_reviews['review_comment_title'].fillna('no comment title')
df_order_reviews['review_comment_message']=df_order_reviews['review_comment_message'].fillna('no comment message')

df_order_reviews['review_comment_title'] = (
    df_order_reviews['review_comment_title']
    .apply(lambda x: unidecode(x) if isinstance(x, str) else x)  
    .apply(lambda x: re.sub(r"[^a-zA-Z'\s]", '', x))              
    .str.strip()
    .str.lower()
)

df_order_reviews['review_comment_message'] = (
    df_order_reviews['review_comment_message']
    .apply(lambda x: unidecode(x) if isinstance(x, str) else x)  
    .apply(lambda x: re.sub(r"[^a-zA-Z'\s]", '', x))              
    .str.strip()
    .str.lower()
)

df_order_reviews['review_creation_date']=df_order_reviews['review_creation_date'].str.strip()
df_order_reviews['review_answer_timestamp']=df_order_reviews['review_answer_timestamp'].str.strip()


df_order_reviews['review_id']=df_order_reviews['review_id'].astype('string')
df_order_reviews['order_id']=df_order_reviews['order_id'].astype('string')
df_order_reviews['review_comment_title']=df_order_reviews['review_comment_title'].astype('string')
df_order_reviews['review_comment_message']=df_order_reviews['review_comment_message'].astype('string')
df_order_reviews['review_creation_date']=pd.to_datetime(df_order_reviews['review_creation_date'],format='%Y-%m-%d %H:%M:%S',errors='coerce')
df_order_reviews['review_answer_timestamp']=pd.to_datetime(df_order_reviews['review_answer_timestamp'],format='%Y-%m-%d %H:%M:%S',errors='coerce')

def label_review(score):
    if score == 5:
        return 'excellent'
    elif score == 4:
        return 'very good'
    elif score == 3:
        return 'good'
    elif score == 2:
        return 'poor'
    elif score == 1:
        return 'very bad'
    else:
        return 'unknown'

df_order_reviews['review_label'] = df_order_reviews['review_score'].apply(label_review)

# check after cleaning & transformations
print(df_order_reviews.head(10))
print('----------------------')

print(df_order_reviews.info())
print('----------------------')

print(df_order_reviews.describe(include='all'))
print('----------------------')

# load
# df_order_reviews.to_csv('order_reviews_clean.csv',index=False)
