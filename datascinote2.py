# 1/30/24
#project 2 

import pandas as pd 
import plotly_express as px 
import json 

flights = pd.read_json('https://raw.githubusercontent.com/byuidatascience/data4missing/master/data-raw/flights_missing/flights_missing.json')

#%%
pd.set_option("display.max_columns", None)
#Shows all of the columns in the data set that might otherwise not show up

# %%
flights.isna().sum()
#shows what python agrees is a missing value 
# %%
flights.value_counts()
# %%
result = flights[flights['month']== 'n/a']
print(result)
# %%
