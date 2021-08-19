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

#####*** Get status updates, can limit by ID, category
#print(cg.get_status_updates())
#status_updates_df = pd.DataFrame(cg.get_status_updates())  ## can maybe use a range to pull last few updates, or use curl like in the API guide, use that to make categories or search by coin
#print(status_updates_df)
#coin_status_df = cg.get_coin_status_updates_by_id(id='litecoin')
##print(coin_status_df)

#####*** Get All events
#events_df = pd.json_normalize(cg.get_events()).data[0][0]  #can limit by type, country, start and end date
#event_fields = ["type","title","description"]
#print(events_df["description"])
#print(cg.get_events_countries())

#####*** Trending coins (top 7 last 24 hours)
#trending_df = cg.get_search_trending()
#print(trending_df)


###### Crypto Industry Data (active cryptocurrencies, upcoming ICOs, total mkt cap)
#global_news_df = pd.DataFrame(cg.get_global())
#print(global_news_df)