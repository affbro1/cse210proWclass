
import pandas as pd   
import plotly_express as px  
import tabulate as tb 

url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/mpg/mpg.csv"
mpg = pd.read_csv(url)


chart = px.scatter(mpg, x='displ', y='hwy', title = 'engine_size_to_fuel')

chart.show()

print(mpg
  .head(5)
  .filter(["manufacturer", "model","year", "hwy"])
  .to_markdown(index=False))