import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

wine_data = load_wine()
X = pd.DataFrame(wine_data.data, columns=wine_data.feature_names)
y = wine_data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf_complet = DecisionTreeClassifier(max_depth=None, random_state=42)
clf_complet.fit(X_train, y_train)

y_pred = clf_complet.predict(X_test)

acuratete = accuracy_score(y_test, y_pred)
print(f"Acuratete: {acuratete * 100:.2f}%")