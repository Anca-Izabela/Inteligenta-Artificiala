import pandas as pd

df = pd.read_csv('data.csv')

rezultat = df.groupby('Club')['Overall'].mean().sort_values(ascending=False)

print(rezultat.head(1))