from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_scaled, y_train)

y_pred = knn.predict(X_test_scaled)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=iris.target_names))

"""
INTERPRETARE REZULTATE (Ex 6.3):

1. Performanta Modelului:
   Modelul a obtinut o acuratete de 100% (1.00). In matricea de confuzie 
   se observa ca toate cele 30 de flori din setul de test (10 Setosa, 
   9 Versicolor, 11 Virginica) au fost clasificate corect.

2. Cea mai bine prezisa clasa: 
   Toate clasele au fost prezise perfect, dar 'Setosa' este de obicei 
   cea mai sigura clasa deoarece are caracteristici fizice foarte 
   diferite fata de celelalte doua specii.

3. Concluzie:
   Faptul ca avem 0 in afara diagonalei principale in matricea de confuzie
   ne spune ca nu a existat nicio confuzie intre Versicolor si Virginica
   pe acest set de date de test. Modelul KNN cu k=3 este ideal pentru 
   aceasta problema.
"""