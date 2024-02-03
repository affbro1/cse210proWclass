#| label: libraries
#| include: false
import pandas as pd
import numpy as np
import plotly.express as px

from IPython.display import Markdown
from IPython.display import display

#| label: project data
#| code-summary: Read and format project data
# Include and execute your code here
url = "https://github.com/byuidatascience/data4names/raw/master/data-raw/names_year/names_year.csv"
df = pd.read_csv(url)

df.columns 
df.shape
df.size
df.head()

#%%
#The number of olivers in Utah across all the years in the dataframe df
df.query("name == 'Oliver'").filter(['UT']).sum()
#or as 
#(df
# .query
# .filter
# .sum)

#%%
df.query('name == "Felicia"').filter(["year"]).min

# %%
nm = "Maximus"

maximus = df.query("name == 'Maximus' ")

px.line(maximus,
    x = 'year',
    y = 'Total')



#brittany question? Example code from class
brittany_data = data_frame.query("name == 'Brittany' ")
brittany_data = name_Brittany 
brittany_data["Age"] = 2024 - brittany_data.year

px.scatter(brittany_data,
           x = "Age"
           y = "Total",
           title = "The relationship between name and age counts 
           .add_annotation(x= 34, y = 32562.5, test = "estimated age"))
           
           
           
           
           
           






