# https://github.com/man-c/pycoingecko
# https://www.coingecko.com/en/api/documentation?

from pycoingecko import CoinGeckoAPI
import pandas as pd
cg = CoinGeckoAPI()
token_id='bitcoin'
exchange_id = 'gdax'

#df.to_csv(r'C:\Users\Josep\OneDrive\Desktop\Coding\python.crypto-data\new_file_name.csv')

####################################
############## Derivatives DATA ##################
####################################
# All derivatives tickers and exchanges
derivatives_df = pd.DataFrame(cg.get_derivatives())
#print(derivatives_df)

exchange_market_data_df = pd.DataFrame(cg.get_derivatives_exchanges()) # all derivatives
#print(exchange_market_data_df)


# Derivative exchange data (24hr volume, open interest, # of pairs)
#derivative_by_exhange_df = pd.DataFrame(cg.get_derivatives_exchanges_by_id(id='bitmex')) ##must be an exchange w derivatives, like bitmex
#print(derivative_by_exhange_df)
