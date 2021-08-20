import pandas as pd
from pandas.core.frame import DataFrame
import requests
from pandas import ExcelWriter
import datetime

## START: Top 50 Tokens Daily Market Metrics: to edit the # pulled, change the per_page and page= values in the links
any50 = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50&page=1').json()  ## pulls first 250 by market cap (limited to 250 per page)

any50 = []
for token in any50:
    any50.append(token)
dataset = pd.DataFrame(any50)
#dataset.to_excel('top500.xlsx',sheet_name='top500',index=True)
## END: Top 50 Tokens Daily Market Metrics


## START: Token Historical Data
today = datetime.datetime.timestamp(datetime.datetime.now())
token_list = dataset['id'] ## List of token IDs to loop through pulled from the top500 code.  Eventually will need to break this out at set timers to run only 50 per minute
historicals = pd.DataFrame(columns=['id','price_date','prices','cap_date','market_caps','vol_date','total_volumes'])

for token in token_list:
    historical_request = requests.get(f'https://api.coingecko.com/api/v3/coins/{token}/market_chart/range?vs_currency=usd&from=1483254000&to=1629352800').json()
    prices = pd.DataFrame(historical_request['prices'], columns=['date','prices'])
    mkt_caps = pd.DataFrame(historical_request['market_caps'], columns=['date','market_caps'])
    volumes = pd.DataFrame(historical_request['total_volumes'], columns=['date','total_volumes'])

    append_df = pd.DataFrame(columns=['id'])
    append_df.insert(1,'price_date', datetime.fromtimestamp(prices['date']))
    append_df.insert(2,'prices', prices['prices'])
    append_df.insert(3,'cap_date', datetime.fromtimestamp(mkt_caps['date']))
    append_df.insert(4,'market_caps', mkt_caps['market_caps'])
    append_df.insert(5,'vol_date', datetime.fromtimestamp(volumes['date']))
    append_df.insert(6,'total_volumes', volumes['total_volumes'])
    append_df['id'].fillna(token.strip("'<>() ").replace('\'', '\"'),inplace=True)
    print(append_df)
    historicals=historicals.append(append_df)

print(historicals)
historicals.to_excel('historicals.xlsx',sheet_name='historicals',index=True)