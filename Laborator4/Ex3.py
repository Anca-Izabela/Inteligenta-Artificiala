import pandas as pd

df = pd.read_csv('data.csv')

rezultat = df[(df['Overall'] >= 85) & (df['Age'] < 25)]

print(rezultat)