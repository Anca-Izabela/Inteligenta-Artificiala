import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def convert_finante(valoare_text):
    if isinstance(valoare_text, str):
        valoare_text = valoare_text.replace('€', '')
        if 'M' in valoare_text:
            return float(valoare_text.replace('M', '')) * 1000000
        elif 'K' in valoare_text:
            return float(valoare_text.replace('K', '')) * 1000
    return 0.0

df = pd.read_csv('data.csv')

df_plot = df.head(200).copy()
df_plot['Wage_num'] = df_plot['Wage'].apply(convert_finante)
df_plot['Value_num'] = df_plot['Value'].apply(convert_finante)

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_plot, x='Wage_num', y='Value_num', hue='Overall')
plt.title('Scatterplot Salariu vs Valoare')
plt.show()