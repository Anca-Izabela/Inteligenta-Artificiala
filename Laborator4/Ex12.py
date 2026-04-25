import pandas as pd

def convert_finante(valoare_text):
    if isinstance(valoare_text, str):
        valoare_text = valoare_text.replace('€', '')
        if 'M' in valoare_text:
            return float(valoare_text.replace('M', '')) * 1000000
        elif 'K' in valoare_text:
            return float(valoare_text.replace('K', '')) * 1000
    return 0.0

df = pd.read_csv('data.csv')

df['Value_Numeric'] = df['Value'].apply(convert_finante)
df['Wage_Numeric'] = df['Wage'].apply(convert_finante)

rezultat = df[df['Value_Numeric'] > df['Wage_Numeric']]

print(len(rezultat))