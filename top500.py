import pandas as pd
import requests
from pandas import ExcelWriter

top250 = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1').json()
next250 = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=2').json()

top500 = []

for token in top250:
    top500.append(token)

for token in next250:
    top500.append(token)

dataset = pd.DataFrame(top500)

dataset.to_excel('top500.xlsx',sheet_name='top500',index=True)

print(dataset)