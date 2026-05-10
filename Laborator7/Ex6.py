import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes

diabetes_data = load_diabetes()
df = pd.DataFrame(diabetes_data.data, columns=diabetes_data.feature_names)
df['target'] = diabetes_data.target

plt.figure(figsize=(10, 6))
scatter = plt.scatter(df['age'], df['bmi'], c=df['target'], cmap='viridis', alpha=0.8)
plt.colorbar(scatter, label='Target')
plt.xlabel('Age')
plt.ylabel('BMI')
plt.title('Scatter Plot: Age vs BMI')
plt.show()