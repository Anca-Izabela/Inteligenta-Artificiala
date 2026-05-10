from sklearn.datasets import load_iris

iris = load_iris()

print("Dimensiuni date (randuri, coloane):", iris.data.shape)
print("Atribute:", iris.feature_names)
print("Clase (specii):", iris.target_names)