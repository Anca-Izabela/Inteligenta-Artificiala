import pandas as pd
from sklearn.datasets import load_diabetes

diabetes_data = load_diabetes()
df = pd.DataFrame(diabetes_data.data, columns=diabetes_data.feature_names)
df['target'] = diabetes_data.target

print(df.head())
print(df.info())