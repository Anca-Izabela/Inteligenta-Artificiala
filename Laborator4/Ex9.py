import pandas as pd

df = pd.read_csv('data.csv')

rezultat = df.groupby('Nationality')[['SprintSpeed', 'Acceleration']].mean()

print(rezultat)