import cbpro
import datetime
import pyodbc
from time import sleep
public_client = cbpro.PublicClient()
conn = pyodbc.connect('Driver={SQL Server};'
'Server=DESKTOP-UF36VE9\SQLEXPRESS;'
'Database=EthTr;'
'Trusted_Connection=yes;')

#'Server=localhost\SQLEXPRESS;'
#'Database=master;'
#'Trusted_Connection=True;'

cursor = conn.cursor()


def price_array_helper(array, product, granularity):
for x in array:
x[0:0] = [product, granularity]
return array
def print_historics(product='BTC-USD', end_date=datetime.datetime.now(), granularity=60):
"""
Ingest historical pricing and volume for a given crypto product from Coinbase and insert that into the SQL database
:param product: What product would you like to pull historical price info from Coinbase. Default is Bitcoin-USD pair
:param end_date: What is the most recent time period you would like to work backward from. Default is the current time, which then gets rounded to the nearest minute
:param granularity: What time period should Coinbase return the candles in. Default measure is 60 second candles, review Coinbase docs for potential options
:return: N/A
"""
# use 299 minutes given rate limit of 300 from Coinbase API and pulling candles of 1 minute
time_delta = datetime.timedelta(seconds=granularity*299)
# round down to nearest minute for consistency in database
end_date = end_date.replace(second=0, microsecond=0)
# add column headers from SQL database
product_historical_info_sql_headers = ['product', 'candle_dur_secs', 'time', 'low_price', 'high_price',
'open_price',
'close_price', 'volume']
product_historical_info = []
# Loop through historical info pulling data on given
for i in range(10000):
sleep(0.1)
print('Start date: ', end_date - time_delta)
print('End date: ', end_date)
product_historical_info.append(
public_client.get_product_historic_rates(product, start=(end_date - time_delta).isoformat(),
end=end_date.isoformat(),
granularity=granularity))
end_date = end_date - time_delta - datetime.timedelta(seconds=granularity)
print(product_historical_info)
product_historical_info_flat = [item for sublist in product_historical_info for item in sublist]
product_historical_info_flat = price_array_helper(product_historical_info_flat, product, granularity)
# Insert into SQL Table
columns = ','.join(product_historical_info_sql_headers) # String of column names
values = ','.join(['?'] * len(product_historical_info_sql_headers)) # Placeholders for values
# Bulk insert
query = "INSERT INTO dbo.Prices({0}) VALUES ({1})".format(columns, values)
cursor.executemany(query, product_historical_info_flat)
conn.commit() # save change

if __name__ == '__main__':
# setup()
# end_date = datetime.datetime.utcfromtimestamp(1465956840) #start here on the next round
# print_historics(end_date=end_date)
print_historics(product='ETH-USD')