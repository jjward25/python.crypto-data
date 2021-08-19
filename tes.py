import pandas as pd
import requests
from pandas import ExcelWriter

import datetime

today = datetime.datetime.now().total_seconds()
print(today)


for token in top250:
    top500.append(token)

for token in next250:
    top500.append(token)

dataset = pd.DataFrame(top500)

dataset.to_excel('top500.xlsx',sheet_name='top500',index=True)

print(dataset)