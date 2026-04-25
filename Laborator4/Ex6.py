import pandas as pd

df = pd.read_csv('data.csv')

print("Dimensiuni (randuri, coloane):", df.shape)

print("Numar jucatori unici:", df['Name'].nunique())