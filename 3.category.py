import pandas as pd
import requests
import openpyxl

category_request = requests.get('https://api.coingecko.com/api/v3/coins/categories').json() 
category_df = pd.DataFrame(category_request)

with pd.ExcelWriter('crypto_data.xlsx', engine='openpyxl') as writer:
    writer.book = openpyxl.load_workbook('crypto_data.xlsx')
    category_df.to_excel(writer, sheet_name='category_deets')