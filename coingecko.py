# https://github.com/man-c/pycoingecko
# https://www.coingecko.com/en/api/documentation?

from pycoingecko import CoinGeckoAPI
import pandas as pd
cg = CoinGeckoAPI()
token_id='bitcoin'
exchange_id = 'gdax'

#df.to_csv(r'C:\Users\Josep\OneDrive\Desktop\Coding\python.crypto-data\new_file_name.csv')

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


####################################
############## NOT AS USEFUL ##################
####################################
# Coin price using the coin ID
#print(cg.get_price(ids=['binancecoin','bitcoin'], vs_currencies='usd'))
# provides the price using contract addresses
#print(cg.get_token_price())
# Get Historical price by date
#print(cg.get_coin_history_by_id(id='bitcoin', date='30-01-2021', localization='false'))
#print(cg.get_exchanges_tickers_by_id(id='gdax')) ## Same pairs from the coin_by_id request