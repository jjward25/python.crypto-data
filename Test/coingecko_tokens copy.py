# https://github.com/man-c/pycoingecko
# https://www.coingecko.com/en/api/documentation?

from pycoingecko import CoinGeckoAPI
import pandas as pd
from pandas import ExcelWriter
import requests
from ratelimit import limits, sleep_and_retry

cg = CoinGeckoAPI()
input_id='bitcoin'
writer = ExcelWriter('C:/Users/Josep/OneDrive/Desktop/Coding/python.crypto-data/token_files/tokens2.xlsx')
#df.to_csv(r'C:\Users\Josep\OneDrive\Desktop\Coding\python.crypto-data\new_file_name.csv')



TIME_PERIOD = 60   # time period in seconds
url ='https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1'

@limits(calls=50, period=TIME_PERIOD)
def call_api(url):
    response = pd.DataFrame(requests.get(url,headers='Headers'))
    print(response)
    response.to_excel(writer,sheet_name='price_history')

    if response.status_code != 200:
        raise Exception('API response: {}'.format(response.status_code))
    return response




#coin_list_500 = []

#price_df = pd.DataFrame()

#for c in coin_list_500:
    
#    price_df = pd.DataFrame(cg.get_coin_market_chart_by_id(id=input_id, vs_currency='usd', days=365))

#price_df.to_excel(writer,sheet_name='price_history')
#print(price_df)
