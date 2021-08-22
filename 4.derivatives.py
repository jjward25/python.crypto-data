import pandas as pd
import requests
from pycoingecko import CoinGeckoAPI
import openpyxl

cg = CoinGeckoAPI()

## Top 25 Exchanges by 24h Volume
top_derivative_exchanges_request = requests.get('https://api.coingecko.com/api/v3/derivatives/exchanges?order=trade_volume_24h_btc_desc&per_page=25&page=1').json()
derivative_exchange_df = pd.DataFrame(top_derivative_exchanges_request)
#derivative_exchange_df.to_excel('crypto_data.xlsx',sheet_name='top_deriv_exchanges')
print(derivative_exchange_df)

## All Tickers
derivatives_df = pd.DataFrame(cg.get_derivatives())
#derivatives_df.to_excel('crypto_data.xlsx',sheet_name='all__derivs_tickers')
print(derivatives_df)

with pd.ExcelWriter('crypto_data.xlsx', engine='openpyxl') as writer:
    writer.book = openpyxl.load_workbook('crypto_data.xlsx')
    derivative_exchange_df.to_excel(writer, sheet_name='top_ders_xc')
    derivatives_df.to_excel(writer, sheet_name='all_der_ticks')
