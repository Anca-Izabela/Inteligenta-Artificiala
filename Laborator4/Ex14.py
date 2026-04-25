import pandas as pd

df = pd.read_csv('data.csv')

df['ShortPassing'] = df['ShortPassing'].fillna(0)
df['SprintSpeed'] = df['SprintSpeed'].fillna(0)

df['Scor'] = (0.3 * df['Overall']) + (0.3 * df['Potential']) + (0.2 * df['SprintSpeed']) + (0.2 * df['ShortPassing'])

rezultat = df[['Name', 'Overall', 'Potential', 'Scor']].sort_values(by='Scor', ascending=False)

print(rezultat.head(10))