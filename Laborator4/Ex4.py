import pandas as pd

df = pd.read_csv('data.csv')

rezultat = df.sort_values(by='Skill Moves', ascending=False)

print(rezultat)