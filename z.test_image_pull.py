import pandas as pd
import openpyxl
import requests
from pycoingecko import CoinGeckoAPI
import time

cg = CoinGeckoAPI()

#### START: Top 500 Tokens Daily Market Metrics: to edit the # pulled, change the per_page and page= values in the links
top250 = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1').json()
next250 = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=2').json()
top500 = []
for token in top250:
    top500.append(token)
for token in next250:
    top500.append(token)
dataset = pd.DataFrame(top500)

top50 = dataset['id'][0:50]
t50_100 = dataset['id'][50:100]
t101_150 = dataset['id'][100:150]
t150_200 = dataset['id'][150:200]
t200_250 = dataset['id'][200:250]

## Loop for Token Data
coin_fields = ["id", "symbol","name","image.thumb","image.small","image.large"] ## developer data

top50_df = pd.DataFrame()
for token in top50:
    new_df = pd.json_normalize(cg.get_coin_by_id(id=token, localization='false'))[coin_fields]
    top50_df = top50_df.append(new_df)
print(top50_df)

time.sleep(40)
df_100 = pd.DataFrame()
for token in t50_100:
    new_df = pd.json_normalize(cg.get_coin_by_id(id=token, localization='false'))[coin_fields]
    df_100 = df_100.append(new_df)
print(df_100)

time.sleep(40)
df_150 = pd.DataFrame()
for token in t101_150:
    new_df = pd.json_normalize(cg.get_coin_by_id(id=token, localization='false'))[coin_fields]
    df_150 = df_150.append(new_df)
print(df_150)

time.sleep(40)
df_200 = pd.DataFrame()
for token in t150_200:
    new_df = pd.json_normalize(cg.get_coin_by_id(id=token, localization='false'))[coin_fields]
    df_200 = df_200.append(new_df)
print(df_200)

time.sleep(40)
df_250 = pd.DataFrame()
for token in t200_250:
    new_df = pd.json_normalize(cg.get_coin_by_id(id=token, localization='false'))[coin_fields]
    df_250 = df_250.append(new_df)
print(df_250)

coin_images = pd.concat([top50_df,df_100,df_150,df_200,df_250])
print(coin_images)