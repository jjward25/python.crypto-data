# https://github.com/man-c/pycoingecko
# https://www.coingecko.com/en/api/documentation?

from pycoingecko import CoinGeckoAPI
import pandas as pd
from pandas import ExcelWriter

cg = CoinGeckoAPI()
input_id='bitcoin'
writer = ExcelWriter('C:/Users/Josep/OneDrive/Desktop/Coding/python.crypto-data/token_files/tokens.xlsx')
#df.to_csv(r'C:\Users\Josep\OneDrive\Desktop\Coding\python.crypto-data\new_file_name.csv')

####################################
############## TOKEN DATA ##################
####################################

##### list of all supported coins: id, name and symbol
#print(cg.get_coins_list())
#all_coins_df = pd.DataFrame(cg.get_coins_list())
#all_coins_df.to_excel(writer, sheet_name='coins_list')
#print(all_coins_df)

##### all supported coins price, market cap, volume and market related data
#print(cg.get_coins_markets(vs_currency='usd'))
#markets_df = pd.DataFrame(cg.get_coins_markets(vs_currency='usd'))
#markets_df.to_excel(writer, sheet_name='market_data')
#print(markets_df)

####################################
############## SINGLE TOKEN DATA ##################
####################################

##### token profile data  -- probably the most valuable field here is the bid_ask_spread_percentage.  Everything else I think is in the table below.
#print(cg.get_coin_by_id(id='bitcoin', localization='false'))
#ticker_fields= ["base","target","last","volume","trust_score","bid_ask_spread_percentage","timestamp","last_traded_at"]
#bitfinex_data = pd.json_normalize(cg.get_coin_by_id(id=input_id, localization='false'))['tickers'][0][0]
#coinbase_data = pd.json_normalize(cg.get_coin_by_id(id=input_id, localization='false'))['tickers'][0][7] ## for bitcoin, coinbase BTC-USD is the 8th object
#print(bitfinex_data)

coin_fields = ["id", "symbol","name","asset_platform_id","block_time_in_minutes","hashing_algorithm","categories","public_notice","additional_notices","description.en",  ## general info
                "links.homepage","links.repos_url.github","genesis_date","sentiment_votes_up_percentage","sentiment_votes_down_percentage","market_cap_rank","developer_score", ## general info
                "community_score","liquidity_score","public_interest_score","market_data.current_price.usd","market_data.total_value_locked", "market_data.ath.usd", ## market data
                "market_data.ath_change_percentage.usd","market_data.atl_date.usd","market_data.atl.usd","market_data.atl_change_percentage.usd","market_data.atl_date.usd", ## market data
                "market_data.market_cap.usd", "market_data.fully_diluted_valuation.usd","market_data.total_volume.usd","market_data.high_24h.usd","market_data.low_24h.usd", ## market data
                "market_data.price_change_24h","market_data.price_change_percentage_24h","market_data.price_change_percentage_7d","market_data.price_change_percentage_14d", ## market data
                "market_data.price_change_percentage_30d","market_data.price_change_percentage_60d","market_data.price_change_percentage_200d","market_data.price_change_percentage_1y", ## market data
                "market_data.market_cap_change_24h","market_data.market_cap_change_percentage_24h","market_data.total_supply","market_data.max_supply","market_data.circulating_supply",  ## market data
                "community_data.facebook_likes","community_data.twitter_followers","community_data.reddit_average_posts_48h","community_data.reddit_average_comments_48h", ## social data
                "community_data.reddit_subscribers","community_data.reddit_accounts_active_48h","community_data.telegram_channel_user_count", ## social data
                "developer_data.forks","developer_data.stars","developer_data.subscribers","developer_data.total_issues","developer_data.closed_issues","developer_data.pull_requests_merged", ## developer data
                "developer_data.pull_request_contributors","developer_data.commit_count_4_weeks","status_updates"] ## developer data
coin_df = pd.json_normalize(cg.get_coin_by_id(id=input_id, localization='false'))[coin_fields]
#coin_df.to_excel(writer,sheet_name='coin_detail')
print(coin_df)

##### Historical mkt data: Minutely data will be used for duration within 1 day, Hourly data will be used for duration between 1 day and 90 days, 
##### Daily data will be used for duration above 90 days. Returns as date in unix format, price

#coin_list_500 = []

#price_df = pd.DataFrame()

#for c in coin_list_500:
    
#    price_df = pd.DataFrame(cg.get_coin_market_chart_by_id(id=input_id, vs_currency='usd', days=365))

#price_df.to_excel(writer,sheet_name='price_history')
#print(price_df)

#### pull price data within a range
#price_range_df = pd.DataFrame(cg.get_coin_market_chart_range_by_id(id=input_id, vs_currency='usd', from_timestamp='1392577232', to_timestamp='1422577232'))
#print(price_range_df)

##### Token status updates
#coin_status_df = pd.DataFrame(cg.get_coin_status_updates_by_id(id='cardano'))
#coin_status_df.to_excel(writer,sheet_name='coin_status')
#print(coin_status_df)

#####* Open High Low Close -- only works for single day, candles are 30 minutes for 1-2 day pulls
#ohlc_df = pd.DataFrame(cg.get_coin_ohlc_by_id(id=input_id,vs_currency='usd',days=1))
#ohlc_df.to_excel(writer,sheet_name='ohlc')
#print(ohlc_df)

#writer.save()