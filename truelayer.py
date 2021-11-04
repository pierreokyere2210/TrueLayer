from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile
import pandas as pd
from sqlalchemy import create_engine
import json
import ast
import gzip
import requests
import urllib.request
import wikipediaapi

api = KaggleApi()
api.authenticate()
#
# #Downloading Kaggle File
url = 'https://www.kaggle.com/rounakbanik/the-movies-dataset/version/7#movies_metadata.csv'
#
# api.dataset_download_files('rounakbanik/the-movies-dataset','/Users/pierre-stephaneokyere/Documents/TrueLayer',unzip= True)
api.dataset_download_file('rounakbanik/the-movies-dataset/version/','movies_metadata.csv')

zf = zipfile.ZipFile('movies_metadata.csv.zip')
zf.extractall()
zf.close()

df = pd.read_csv('movies_metadata.csv',low_memory=False)

df['budget']=pd.to_numeric(df['budget'],errors='coerce').fillna(0)
df['revenue']=pd.to_numeric(df['revenue'],errors='coerce').fillna(0)
df['release_date']=df['release_date'].str[:4].astype(float)
df['budget']= df['budget'].replace(0,1)
df['revenue']= df['revenue'].replace(0,1)
df2 = df.assign(ratio=df['budget']/df['revenue'])

df_tfr = df2.nlargest(1000,'ratio',keep='first')

df_tfr = df_tfr[['original_title','revenue','budget','release_date','vote_average','ratio','production_companies']]

wiki_wiki = wikipediaapi.Wikipedia('en')

rows_url = []
rows_summary = []
for i in range(len(df_tfr['original_title'])):
    try:
        wikititle = df_tfr['original_title'][i]
        page_url = wiki_wiki.page(wikititle).fullurl
        page_summary = wiki_wiki.page(wikititle).summary
    except:
        page_url = ''
        page_summary=''
    rows_url.append(page_url)
    rows_summary.append(page_summary)
df3 = pd.DataFrame(rows_url)
df4 = pd.DataFrame(rows_summary)

df_tfr= df_tfr.assign(url=df3)
df_tfr= df_tfr.assign(summary=df4)
print(df_tfr)

engine = create_engine('postgresql+psycopg2://postgres:dover2210@localhost:9011/truefilm', pool_pre_ping=True)
df_tfr.to_sql(name = 'truefilm_tfr', con = engine, if_exists='replace', index = False)

















# # page_py = wiki_wiki.page(page)
# print(df['original_title'][28])
# rows = []
# for i in range(len(df['original_title'])):
#     page = df['original_title'][i]
#     page_py = wiki_wiki.page.get(pageo)
#
#     print(page_py)
    # if page_py:
    #     rows.append(page_py)
    # else:
    #     rows.append('test')
    # print(rows)


#     # rows.append(page_py)
# print(rows)
#     except KeyError:
#         continue
#         page_py = 'test'
# rows.append(page_py)
# print(rows)
# print(pd.DataFrame(rows))
#

#
# #
# df['original_title'].apply(wiki)
# print(df['original_title'])
# print(wiki_wiki.page(df['original_title'][0]).fullurl)



















