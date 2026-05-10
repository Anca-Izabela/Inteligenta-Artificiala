import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

diabetes_data = load_diabetes()
df = pd.DataFrame(diabetes_data.data, columns=diabetes_data.feature_names)
df['target'] = diabetes_data.target

X = df[['bmi', 'bp']]
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model_multi = LinearRegression()
model_multi.fit(X_train, y_train)

y_pred = model_multi.predict(X_test)

print(f"Coef BMI: {model_multi.coef_[0]:.2f}")
print(f"Coef BP: {model_multi.coef_[1]:.2f}")

r2 = r2_score(y_test, y_pred)
print(f"Scor R2: {r2:.4f}")