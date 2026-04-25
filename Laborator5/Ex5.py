import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

k_values = range(1, 16)
acurateti = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)
    acurateti.append(knn.score(X_test_scaled, y_test))

plt.plot(k_values, acurateti, marker='o')
plt.xlabel('k')
plt.ylabel('Acuratete')
plt.show()

"""
Comentariu Ex 5.3:
Cea mai buna valoare pentru k pare sa fie in intervalul 3-7. 
O valoare mica (k=1) face modelul prea sensibil la zgomot (overfitting), 
in timp ce o valoare prea mare (k=15) poate simplifica prea mult granitele 
dintre specii (underfitting). Valorile impare sunt preferate pentru a 
evita egalitatea la votare.
"""