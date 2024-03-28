#project 5 notes


#%%
import pandas as pd 
import numpy as np
import sqlite3

pd.options.display.max_columns = None
# %%
df = pd.read_csv("https://raw.githubusercontent.com/fivethirtyeight/data/master/star-wars-survey/StarWars.csv", encoding = 'Latin-1')
# %%
df = pd.read_csv("https://raw.githubusercontent.com/fivethirtyeight/data/master/star-wars-survey/StarWars.csv", encoding='ISO-8859-1')


# %%
dat_cols =(dat_cols.replace('Unnamed: \d{1,2}', np.nan, regex=True).replace('Response', "").assign(clean_variable = lambda x: x.variable.str.strip().replace('Which of the following Star Wars films have you seen? Please selectall that apply.','seen'),clean_value = lambda x: x.value.str.strip()).fillna(method = 'ffill').assign(column_name = lambda x: x.clean_variable.str.cat(x.clean_value, sep ="__")))

# %%
dat_cols.column_name# %%# we want to use this with the .replace() command that accepts a dictionary.variables_replace = {'Which of the following Star Wars films have you seen\\? Please select allthat apply\\.':'seen','Please rank the Star Wars films in order of preference with 1 being yourfavorite film in the franchise and 6 being your least favorite film.':'rank','Please state whether you view the following characters favorably,unfavorably, or are unfamiliar with him/her.':'view','Do you consider yourself to be a fan of the Star Trekfranchise\\?':'star_trek_fan','Do you consider yourself to be a fan of the ExpandedUniverse\\?\x8cæ':'expanded_fan','Are you familiar with the Expanded Universe\\?':'know_expanded','Have you seen any of the 6 films in the Star Wars franchise\\?':'seen_any','Do you consider yourself to be a fan of the Star Wars film
franchise\\?':'star_wars_fans','Which character shot first\\?':'shot_first','Unnamed: \d{1,2}':np.nan,' ':'_',}values_replace = {'Response':'','Star Wars: Episode ':'',' ':'_'}
# %%
