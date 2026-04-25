import pandas as pd

df = pd.read_csv('data.csv')

frecventa = df['Nationality'].value_counts()

print("Cea mai frecventa nationalitate:", frecventa.idxmax())
print("\nTop 5 nationalitati:")
print(frecventa.head(5))