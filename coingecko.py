# https://github.com/man-c/pycoingecko
# https://www.coingecko.com/en/api/documentation?

from pycoingecko import CoinGeckoAPI
import pandas as pd
cg = CoinGeckoAPI()
input_id='bitcoin'
# Check server status
#print(cg.ping())

####################################
############## TOKEN DATA ##################
####################################

# Coin price using the coin ID
#print(cg.get_price(ids=['binancecoin','bitcoin'], vs_currencies='usd'))
# provides the price using contract addresses
#print(cg.get_token_price())

# list of all supported coins id, name and symbol
#print(cg.get_coins_list())
all_coins_df = pd.DataFrame(cg.get_coins_list())
#print(all_coins_dfl)
#all_coins_df.to_csv(r'C:\Users\Josep\OneDrive\Desktop\Coding\python.crypto-data\all_coins.csv')

#** all supported coins price, market cap, volume and market related data
#print(cg.get_coins_markets(vs_currency='usd'))
markets_df = pd.DataFrame(cg.get_coins_markets(vs_currency='usd'))
#print(markets_df)
#markets_df.to_csv(r'C:\Users\Josep\OneDrive\Desktop\Coding\python.crypto-data\coin_mkt_details.csv')

#** token profile data
#print(cg.get_coin_by_id(id='bitcoin', localization='false'))
ticker_fields= ["base","target","last","volume","trust_score","bid_ask_spread_percentage","timestamp","last_traded_at"]
bitfinex_data = pd.json_normalize(cg.get_coin_by_id(id=input_id, localization='false'))['tickers'][0][0]
coinbase_data = pd.json_normalize(cg.get_coin_by_id(id=input_id, localization='false'))['tickers'][0][7] ## for bitcoin, coinbase BTC-USD is the 8th object
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
coin_df.to_csv(r'C:\Users\Josep\OneDrive\Desktop\Coding\python.crypto-data\coin_details_id.csv')


# Get Historical price by date
#print(cg.get_coin_history_by_id(id='bitcoin', date='30-01-2021', localization='false'))

#** Historical mkt data: Minutely data will be used for duration within 1 day, 
# Hourly data will be used for duration between 1 day and 90 days, 
# Daily data will be used for duration above 90 days.
# Returns as date in unix format, price
price_df = pd.DataFrame(cg.get_coin_market_chart_by_id(id=input_id, vs_currency='usd', days=365))
print(price_df)
# pull price data within a range
#print(cg.get_coin_market_chart_range_by_id(id='bitcoin', vs_currency='usd', from_timestamp='1392577232', to_timestamp='1422577232'))

## Token status updates
#print(cg.get_coin_status_updates_by_id(id='ethereum'))

#** Open High Low Close -- only works for single day, candles are 30 minutes for 1-2 day pulls
#print(cg.get_coin_ohlc_by_id(id='bitcoin',vs_currency='usd',days=1))


####################################
############## EXCHANGE DATA ##################
####################################

# Exchange lists and derivatives exchange lists, and the list of all exchange names and IDs
#print(cg.get_exchanges_list())
#print(cg.get_derivatives_exchanges_list())
#**print(cg.get_exchanges_id_name_list())  ## exchange volume in BTC abd tio 100 tickers only
#print(cg.get_exchanges_tickers_by_id(id='gdax')) # all tickers on the exchange, paginated w 100 per page
#**print(cg.get_exchanges_volume_chart_by_id(id='gdax', days=3)) $$ exchange volume for last X days

## Exchanges and their trust scores
#t_data = cg.get_exchanges_list()
#df =pd.DataFrame(t_data, columns=['name', 'trust_score','trust_score_rank'])

####################################
############## Derivatives DATA ##################
####################################
# All derivatives tickers and exchanges
#print(cg.get_derivatives())
#print(cg.get_derivatives_exchanges()) # all derivatives
#print(cg.get_derivatives_exchanges_list()) # derivatives name and ID

#** Derivative exchange data (24hr volume, open interest, # of pairs)
# print(cg.get_derivatives_exchanges_by_id(id='bitmex'))


####################################
############## OTHER DATA ##################
####################################

## Get status updates, can limit by ID, category
#** print(cg.get_status_updates())
#status = cg.get_coin_status_updates_by_id(id='litecoin')
#print(status)

## Get All events
#** print(cg.get_events())  #can limit by type, country, start and end date
#print(cg.get_events_countries())

## Trending coins (top 7 last 24 hours)
#** print(cg.get_search_trending())

## Crypto Industry Data (active cryptocurrencies, upcoming ICOs, total mkt cap)
#** print(cg.get_global())
# DeFi specific data(defi mkt cap, defi dominanc, defi:ETH ratio, trading volume 24h, top coin)
# print(cg.get_global_decentralized_finance_defi())




####################################
############## SAMPLE QUERIES ##################
####################################

## Vol of top 100 tickers 
data_binance=cg.get_exchanges_by_id('binance')
df_binance =pd.DataFrame(data_binance['tickers'], columns=['base','target','volume'])
#print(df_binance.head())

## Tickers for a specific exchange that are paginated
data_coinbase_pro=cg.get_exchanges_tickers_by_id(id='gdax')
df_coinbase_pro = pd.DataFrame(data_coinbase_pro['tickers'], columns=['base', 'target','volume'])
df_coinbase_pro.set_index('base',inplace=True)
#print(df_coinbase_pro)