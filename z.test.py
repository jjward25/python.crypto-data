import pandas as pd
import requests
import datetime
import openpyxl
import time


## START: Top 250 Tokens Daily Market Metrics: to edit the # pulled, change the per_page and page= values in the links
top250 = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1').json()

top250_list = []
for token in top250:
    top250_list.append(token)
dataset = pd.DataFrame(top250_list)
top50 = dataset['id'][0:50]
t50_100 = dataset['id'][50:100]
t101_150 = dataset['id'][100:150]
t150_200 = dataset['id'][150:200]
t200_250 = dataset['id'][200:250]

## START: Token Historical Data
today = datetime.datetime.timestamp(datetime.datetime.now())

top50_hist = pd.DataFrame(columns=['id','price_date','prices','cap_date','market_caps','vol_date','total_volumes'])
for token in top50:
    historical_request = requests.get(f'https://api.coingecko.com/api/v3/coins/{token}/market_chart/range?vs_currency=usd&from=1546326000&to=1630505225').json()
    prices = pd.DataFrame(historical_request['prices'], columns=['date','prices'])
    mkt_caps = pd.DataFrame(historical_request['market_caps'], columns=['date','market_caps'])
    volumes = pd.DataFrame(historical_request['total_volumes'], columns=['date','total_volumes'])

    append_df = pd.DataFrame(columns=['id'])
    append_df.insert(1,'price_date', prices['date'])
    append_df.insert(2,'prices', prices['prices'])
    append_df.insert(3,'cap_date', mkt_caps['date'])
    append_df.insert(4,'market_caps', mkt_caps['market_caps'])
    append_df.insert(5,'vol_date', volumes['date'])
    append_df.insert(6,'total_volumes', volumes['total_volumes'])
    append_df['id'].fillna(token.strip("'<>() ").replace('\'', '\"'),inplace=True)
    append_df['price_date'] = pd.to_datetime(append_df['price_date'],unit='ms')
    append_df['cap_date'] = pd.to_datetime(append_df['cap_date'],unit='ms')
    append_df['vol_date'] = pd.to_datetime(append_df['vol_date'],unit='ms')
    
    top50_hist=top50_hist.append(append_df)

print(top50_hist.head())
time.sleep(60)

top100_hist = pd.DataFrame(columns=['id','price_date','prices','cap_date','market_caps','vol_date','total_volumes'])
for token in t50_100:
    historical_request2 = requests.get(f'https://api.coingecko.com/api/v3/coins/{token}/market_chart/range?vs_currency=usd&from=1546326000&to=1630505225').json()
    prices = pd.DataFrame(historical_request2['prices'], columns=['date','prices'])
    mkt_caps = pd.DataFrame(historical_request2['market_caps'], columns=['date','market_caps'])
    volumes = pd.DataFrame(historical_request2['total_volumes'], columns=['date','total_volumes'])

    append_df = pd.DataFrame(columns=['id'])
    append_df.insert(1,'price_date', prices['date'])
    append_df.insert(2,'prices', prices['prices'])
    append_df.insert(3,'cap_date', mkt_caps['date'])
    append_df.insert(4,'market_caps', mkt_caps['market_caps'])
    append_df.insert(5,'vol_date', volumes['date'])
    append_df.insert(6,'total_volumes', volumes['total_volumes'])
    append_df['id'].fillna(token.strip("'<>() ").replace('\'', '\"'),inplace=True)
    append_df['price_date'] = pd.to_datetime(append_df['price_date'],unit='ms')
    append_df['cap_date'] = pd.to_datetime(append_df['cap_date'],unit='ms')
    append_df['vol_date'] = pd.to_datetime(append_df['vol_date'],unit='ms')
    
    top100_hist=top100_hist.append(append_df)

print(top100_hist.head())
time.sleep(60)

top150_hist = pd.DataFrame(columns=['id','price_date','prices','cap_date','market_caps','vol_date','total_volumes'])
for token in t101_150:
    historical_request3 = requests.get(f'https://api.coingecko.com/api/v3/coins/{token}/market_chart/range?vs_currency=usd&from=1546326000&to=1630505225').json()
    prices = pd.DataFrame(historical_request3['prices'], columns=['date','prices'])
    mkt_caps = pd.DataFrame(historical_request3['market_caps'], columns=['date','market_caps'])
    volumes = pd.DataFrame(historical_request3['total_volumes'], columns=['date','total_volumes'])

    append_df = pd.DataFrame(columns=['id'])
    append_df.insert(1,'price_date', prices['date'])
    append_df.insert(2,'prices', prices['prices'])
    append_df.insert(3,'cap_date', mkt_caps['date'])
    append_df.insert(4,'market_caps', mkt_caps['market_caps'])
    append_df.insert(5,'vol_date', volumes['date'])
    append_df.insert(6,'total_volumes', volumes['total_volumes'])
    append_df['id'].fillna(token.strip("'<>() ").replace('\'', '\"'),inplace=True)
    append_df['price_date'] = pd.to_datetime(append_df['price_date'],unit='ms')
    append_df['cap_date'] = pd.to_datetime(append_df['cap_date'],unit='ms')
    append_df['vol_date'] = pd.to_datetime(append_df['vol_date'],unit='ms')
    
    top150_hist=top150_hist.append(append_df)
    
print(top150_hist.head())
time.sleep(60)

top200_hist = pd.DataFrame(columns=['id','price_date','prices','cap_date','market_caps','vol_date','total_volumes'])
for token in t150_200:
    historical_request4 = requests.get(f'https://api.coingecko.com/api/v3/coins/{token}/market_chart/range?vs_currency=usd&from=1546326000&to=1630505225').json()
    prices = pd.DataFrame(historical_request4['prices'], columns=['date','prices'])
    mkt_caps = pd.DataFrame(historical_request4['market_caps'], columns=['date','market_caps'])
    volumes = pd.DataFrame(historical_request4['total_volumes'], columns=['date','total_volumes'])

    append_df = pd.DataFrame(columns=['id'])
    append_df.insert(1,'price_date', prices['date'])
    append_df.insert(2,'prices', prices['prices'])
    append_df.insert(3,'cap_date', mkt_caps['date'])
    append_df.insert(4,'market_caps', mkt_caps['market_caps'])
    append_df.insert(5,'vol_date', volumes['date'])
    append_df.insert(6,'total_volumes', volumes['total_volumes'])
    append_df['id'].fillna(token.strip("'<>() ").replace('\'', '\"'),inplace=True)
    append_df['price_date'] = pd.to_datetime(append_df['price_date'],unit='ms')
    append_df['cap_date'] = pd.to_datetime(append_df['cap_date'],unit='ms')
    append_df['vol_date'] = pd.to_datetime(append_df['vol_date'],unit='ms')
    
    top200_hist=top200_hist.append(append_df)

print(top200_hist.head())
time.sleep(60)

top250_hist = pd.DataFrame(columns=['id','price_date','prices','cap_date','market_caps','vol_date','total_volumes'])
for token in t200_250:
    historical_request5 = requests.get(f'https://api.coingecko.com/api/v3/coins/{token}/market_chart/range?vs_currency=usd&from=1546326000&to=1630505225').json()
    prices = pd.DataFrame(historical_request5['prices'], columns=['date','prices'])
    mkt_caps = pd.DataFrame(historical_request5['market_caps'], columns=['date','market_caps'])
    volumes = pd.DataFrame(historical_request5['total_volumes'], columns=['date','total_volumes'])

    append_df = pd.DataFrame(columns=['id'])
    append_df.insert(1,'price_date', prices['date'])
    append_df.insert(2,'prices', prices['prices'])
    append_df.insert(3,'cap_date', mkt_caps['date'])
    append_df.insert(4,'market_caps', mkt_caps['market_caps'])
    append_df.insert(5,'vol_date', volumes['date'])
    append_df.insert(6,'total_volumes', volumes['total_volumes'])
    append_df['id'].fillna(token.strip("'<>() ").replace('\'', '\"'),inplace=True)
    append_df['price_date'] = pd.to_datetime(append_df['price_date'],unit='ms')
    append_df['cap_date'] = pd.to_datetime(append_df['cap_date'],unit='ms')
    append_df['vol_date'] = pd.to_datetime(append_df['vol_date'],unit='ms')
    
    top250_hist=top250_hist.append(append_df)

print(top250_hist.head())
hist_df = pd.concat([top50_hist,top100_hist,top150_hist,top200_hist,top250_hist])
print(hist_df.head())

hist_df.to_excel('crypto_hist.xlsx',sheet_name='token_data')