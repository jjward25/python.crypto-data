import cbpro
import datetime
from time import sleep

public_client = cbpro.PublicClient()

#    Ingest historical pricing and volume for a given crypto product from Coinbase and insert that into the SQL database
#    :param product: What product would you like to pull historical price info from Coinbase. Default is Bitcoin-USD pair
#    :param end_date: What is the most recent time period you would like to work backward from. Default is the current time, which then gets rounded to the nearest minute
#    :param granularity: What time period should Coinbase return the candles in. Default measure is 60 second candles, review Coinbase docs for potential options
#    :return: N/A

def print_historics(product='BTC-USD', end_date=datetime.datetime.now(), granularity=60):
# use 299 minutes given rate limit of 300 from Coinbase API and pulling candles of 1 minute
    time_delta = datetime.timedelta(seconds=granularity*299)
# round down to nearest minute for consistency in database
    end_date = end_date.replace(second=0, microsecond=0)
# add column headers from SQL database
    product_historical_info = []
# Loop through historical info pulling data on given
    for i in range(10000):
        sleep(0.1)

        print('Start date: ', end_date - time_delta)
        print('End date: ', end_date)

        product_historical_info.append(
            public_client.get_product_historic_rates(product, start=(end_date - time_delta).isoformat(), end=end_date.isoformat(), granularity=granularity))
        
        #Reset end date to capture earlier periods
        end_date = end_date - time_delta - datetime.timedelta(seconds=granularity)
        #print(product_historical_info)
    print(product_historical_info)
        
if __name__ == '__main__':

    print_historics(product='ETH-USD')