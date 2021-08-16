# https://github.com/man-c/pycoingecko
# https://www.coingecko.com/en/api/documentation?

from pycoingecko import CoinGeckoAPI
import pandas as pd
cg = CoinGeckoAPI()
input_id='bitcoin'
exchange_id = 'gdax'


#df.to_csv(r'C:\Users\Josep\OneDrive\Desktop\Coding\python.crypto-data\new_file_name.csv')

####################################
############## EXCHANGE DATA ##################
####################################
## Notes: maybe details only from exchanges w certain trust scores

##### Exchange lists and derivatives exchange lists, and the list of all exchange names and IDs (REFERENCE TABLE)
#exchanges_df = pd.DataFrame(cg.get_exchanges_list())
#exchanges_df.to_csv(r'C:\Users\Josep\OneDrive\Desktop\Coding\python.crypto-data\exchange_files\exchanges.csv')
#print(exchanges_df)

#derivatives_exchanges_df = pd.DataFrame(cg.get_derivatives_exchanges_list())
#derivatives_exchanges_df.to_csv(r'C:\Users\Josep\OneDrive\Desktop\Coding\python.crypto-data\exchange_files\derivatives_exchanges.csv')
#print(derivatives_exchanges_df)

#exchange_id_list_df = pd.DataFrame(cg.get_exchanges_id_name_list())  ## reference table for exchange IDs and Names
#exchange_id_list_df.to_csv(r'C:\Users\Josep\OneDrive\Desktop\Coding\python.crypto-data\exchange_files\exchange_id_list.csv')
#print(exchange_id_list_df)

#exchange_volume_df = pd.DataFrame(cg.get_exchanges_volume_chart_by_id(id=exchange_id, days=3)) ## exchange volume for last X days
#exchange_volume_df.to_csv(r'C:\Users\Josep\OneDrive\Desktop\Coding\python.crypto-data\exchange_files\exchange_volume.csv')
#print(exchange_volume_df)