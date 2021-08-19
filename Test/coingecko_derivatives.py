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
#derivatives_df = pd.DataFrame(cg.get_derivatives())
#derivatives_df.to_csv(r'C:\Users\Josep\OneDrive\Desktop\Coding\python.crypto-data\derivatives_files\derivatives_list.csv')
#print(derivatives_df)

#exchange_market_data_df = pd.DataFrame(cg.get_derivatives_exchanges()) # all derivatives
#exchange_market_data_df.to_csv(r'C:\Users\Josep\OneDrive\Desktop\Coding\python.crypto-data\derivatives_files\derivatives_exchange_data.csv')
#print(exchange_market_data_df)

#derivatives_exchanges_df = pd.DataFrame(cg.get_derivatives_exchanges_list())
#derivatives_exchanges_df.to_csv(r'C:\Users\Josep\OneDrive\Desktop\Coding\python.crypto-data\derivatives_files\derivatives_exchanges.csv')
#print(derivatives_exchanges_df)