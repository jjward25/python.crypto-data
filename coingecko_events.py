# https://github.com/man-c/pycoingecko
# https://www.coingecko.com/en/api/documentation?

from pycoingecko import CoinGeckoAPI
import pandas as pd
cg = CoinGeckoAPI()
token_id='bitcoin'
exchange_id = 'gdax'

#df.to_csv(r'C:\Users\Josep\OneDrive\Desktop\Coding\python.crypto-data\new_file_name.csv')

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