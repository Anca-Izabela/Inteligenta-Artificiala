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

df_afacere = df[['Name', 'Wage', 'Value']].copy()

df_afacere['val_num'] = df_afacere['Value'].apply(convert_finante)
df_afacere['wage_num'] = df_afacere['Wage'].apply(convert_finante)

df_afacere['difference'] = df_afacere['val_num'] - df_afacere['wage_num']

df_afacere = df_afacere.sort_values(by='difference', ascending=False)

print(df_afacere[['Name', 'Wage', 'Value', 'difference']].head(10))