import pandas as pd 

df = pd.read_csv('data.csv') 
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(df)