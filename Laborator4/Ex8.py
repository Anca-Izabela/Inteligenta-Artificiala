import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

top_5 = df['Nationality'].value_counts().head(5)

plt.pie(top_5.values, labels=top_5.index, autopct='%1.1f%%')
plt.title('Top 5 Nationalitati')
plt.show()