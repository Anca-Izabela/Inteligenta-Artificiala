import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier, plot_tree

wine_data = load_wine()
df = pd.DataFrame(wine_data.data, columns=wine_data.feature_names)
y = wine_data.target

X = df[['alcohol', 'flavanoids']]

clf = DecisionTreeClassifier(max_depth=2, random_state=42)
clf.fit(X, y)

plt.figure(figsize=(12, 8))
plot_tree(clf, feature_names=['alcohol', 'flavanoids'], class_names=wine_data.target_names, filled=True)
plt.show()


'''
INTERPRETARE NODURI:
1. Nodul radacina (primul nod): Verifica de obicei nivelul de 'flavanoids'. 
   Daca flavanoids <= 1.58, proba este trimisa spre ramura care prezice clasa_2 (vinuri cu structura chimica specifica).
   
2. Nodul de pe nivelul 1 (stanga sau dreapta): Daca flavanoidele sunt > 1.58, 
   se verifica 'alcohol'. Daca alcohol <= 12.72, modelul tinde sa prezica clasa_1, 
   iar daca este mai mare, prezice clasa_0.
'''