import pandas as pd

df = pd.read_csv('data.csv')

jucatori_peste_40 = df[df['Age'] > 40]
rezultat = jucatori_peste_40.head(10)

print(rezultat)