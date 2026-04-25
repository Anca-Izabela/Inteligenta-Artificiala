import pandas as pd

df = pd.read_csv('data.csv')
rezultat = df[df['Contract Valid Until'] == 2021]

print(rezultat)