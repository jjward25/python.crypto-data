# https://github.com/man-c/pycoingecko
# https://www.coingecko.com/en/api/documentation?

from pycoingecko import CoinGeckoAPI
import pandas as pd
cg = CoinGeckoAPI()

# Check server status
#print(cg.ping())

####################################
############## TOKEN DATA ##################
####################################

# Coin price using the coin ID
#print(cg.get_price(ids=['binancecoin','bitcoin'], vs_currencies='usd'))

# provides the price using contract addresses
#print(cg.get_token_price())

#** list of all supported coins id, name and symbol
#print(pd.DataFrame(cg.get_coins_list()))

#** all supported coins price, market cap, volume and market related data
#print(pd.DataFrame(cg.get_coins_markets(vs_currency='usd')))

#** token profile data
#print(cg.get_coin_by_id(id='bitcoin'))

#** Get Historical price by date
#print(cg.get_coin_history_by_id(id='bitcoin', date='30-01-2021', localization='false'))
#** Historical mkt data: Minutely data will be used for duration within 1 day, 
# Hourly data will be used for duration between 1 day and 90 days, 
# Daily data will be used for duration above 90 days.
# Returns as date in unix format, price
#** print(cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=365))
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