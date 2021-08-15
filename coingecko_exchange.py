# https://github.com/man-c/pycoingecko
# https://www.coingecko.com/en/api/documentation?

from pycoingecko import CoinGeckoAPI
import pandas as pd
cg = CoinGeckoAPI()
input_id='bitcoin'

#df.to_csv(r'C:\Users\Josep\OneDrive\Desktop\Coding\python.crypto-data\new_file_name.csv')

####################################
############## EXCHANGE DATA ##################
####################################

##### Exchange lists and derivatives exchange lists, and the list of all exchange names and IDs (REFERENCE TABLE)
exchanges_df = pd.DataFrame(cg.get_exchanges_list())
#print(exchanges_df)

derivatives_exchanges_df = pd.DataFrame(cg.get_derivatives_exchanges_list())
#print(derivatives_exchanges_df)

#**print(cg.get_exchanges_id_name_list())  ## exchange volume in BTC abd tio 100 tickers only
#print(cg.get_exchanges_tickers_by_id(id='gdax')) # all tickers on the exchange, paginated w 100 per page
#**print(cg.get_exchanges_volume_chart_by_id(id='gdax', days=3)) $$ exchange volume for last X days

## Exchanges and their trust scores
#t_data = cg.get_exchanges_list()
#df =pd.DataFrame(t_data, columns=['name', 'trust_score','trust_score_rank'])