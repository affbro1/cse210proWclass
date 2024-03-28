#%%
import pandas as pd 
import numpy as np
import sqlite3

con = sqlite3.connect('lahmansbaseballdb.sqlite')

df = pd.read_sql_query("SELECT * FROM batting LIMIT 2", con)
print(df.to_string())

# %%
