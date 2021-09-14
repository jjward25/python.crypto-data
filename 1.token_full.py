import pandas as pd
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
t151_200 = dataset['id'][150:200]
t201_250 = dataset['id'][200:250]
time.sleep(90)

## Loop for Token Data
coin_fields = ["id", "symbol","name","asset_platform_id","block_time_in_minutes","hashing_algorithm","categories","public_notice","description.en",  ## general info
                "links.homepage","links.repos_url.github","genesis_date","sentiment_votes_up_percentage","sentiment_votes_down_percentage","market_cap_rank","developer_score", ## general info
                "community_score","liquidity_score","public_interest_score","market_data.current_price.usd", "market_data.ath.usd", ## market data
                "market_data.ath_change_percentage.usd","market_data.atl_date.usd","market_data.atl.usd","market_data.atl_change_percentage.usd", ## market data
                "market_data.market_cap.usd","market_data.total_volume.usd","market_data.high_24h.usd","market_data.low_24h.usd", ## market data
                "market_data.price_change_24h","market_data.price_change_percentage_24h","market_data.price_change_percentage_7d","market_data.price_change_percentage_14d", ## market data
                "market_data.price_change_percentage_30d","market_data.price_change_percentage_60d","market_data.price_change_percentage_200d","market_data.price_change_percentage_1y", ## market data
                "market_data.market_cap_change_24h","market_data.market_cap_change_percentage_24h","market_data.total_supply","market_data.max_supply","market_data.circulating_supply",  ## market data
                "community_data.facebook_likes","community_data.twitter_followers","community_data.reddit_average_posts_48h","community_data.reddit_average_comments_48h", ## social data
                "community_data.reddit_subscribers","community_data.reddit_accounts_active_48h","community_data.telegram_channel_user_count", ## social data
                "developer_data.forks","developer_data.stars","developer_data.subscribers","developer_data.total_issues","developer_data.closed_issues","developer_data.pull_requests_merged", ## developer data
                "developer_data.pull_request_contributors","developer_data.commit_count_4_weeks"] ## developer data
df50 = pd.DataFrame()
for token in top50:
    new_df = pd.json_normalize(cg.get_coin_by_id(id=token, localization='false'))[coin_fields]
    df50 = df50.append(new_df)
print(df50)

time.sleep(90)

df_100 = pd.DataFrame()
for token in t50_100:
    new_df = pd.json_normalize(cg.get_coin_by_id(id=token, localization='false'))[coin_fields]
    df_100 = df_100.append(new_df)
print(df_100)

time.sleep(90)

df_150 = pd.DataFrame()
for token in t101_150:
    new_df = pd.json_normalize(cg.get_coin_by_id(id=token, localization='false'))[coin_fields]
    df_150 = df_150.append(new_df)
print(df_150)

time.sleep(90)

df_200 = pd.DataFrame()
for token in t151_200:
    new_df = pd.json_normalize(cg.get_coin_by_id(id=token, localization='false'))[coin_fields]
    df_200 = df_200.append(new_df)
print(df_200)

time.sleep(90)

df_250 = pd.DataFrame()
for token in t201_250:
    new_df = pd.json_normalize(cg.get_coin_by_id(id=token, localization='false'))[coin_fields]
    df_250 = df_250.append(new_df)
print(df_250)

coin_df = pd.concat([df50,df_100,df_150,df_200,df_250])
#print(coin_df)

coin_df.to_excel('crypto_data.xlsx',sheet_name='token_data')
## END: Top 50 Tokens Daily Market Metrics

