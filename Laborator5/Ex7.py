import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

iris = load_iris()

X = iris.data[:, 2:] 
y = iris.target

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_scaled, y)

plt.figure(figsize=(8, 6))
for i, color, label in zip([0, 1, 2], ['blue', 'orange', 'green'], iris.target_names):
    plt.scatter(X[y == i, 0], X[y == i, 1], c=color, label=label, edgecolors='k')

plt.xlabel('Lungime petala (cm)')
plt.ylabel('Latime petala (cm)')
plt.title('Vizualizare Iris: Lungime vs Latime Petala')
plt.legend()
plt.show()

print("\n--- Predictie Floare Noua ---")
try:
    l_petala = float(input("Introduceti lungimea petalei: "))
    w_petala = float(input("Introduceti latimea petalei: "))

    noua_floare = np.array([[l_petala, w_petala]])
    noua_floare_scaled = scaler.transform(noua_floare)

    predictie_index = knn.predict(noua_floare_scaled)[0]
    nume_specie = iris.target_names[predictie_index]

    print(f"\nRezultat: Modelul crede ca floarea ta este din specia: **{nume_specie.upper()}**")
except ValueError:
    print("Eroare: Te rog sa introduci doar numere (cu punct in loc de virgula).")