import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes

diabetes_data = load_diabetes()
df = pd.DataFrame(diabetes_data.data, columns=diabetes_data.feature_names)

plt.hist(df['bmi'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('BMI')
plt.ylabel('Frecventa')
plt.title('Distributia caracteristicii BMI')
plt.show()