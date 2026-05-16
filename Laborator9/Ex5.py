import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

mnist = fetch_openml('mnist_784', version=1, as_frame=False, parser='liac-arff')
X, y = mnist.data, mnist.target
y = y.astype(np.uint8)

X_normalized = X / 255.0
X_train, X_test, y_train, y_test = train_test_split(X_normalized, y, test_size=0.2, random_state=42)

model_nou = Sequential([
    Dense(512, input_shape=(784,), activation='relu'),
    Dense(10, activation='softmax')
])

model_nou.summary()
model_nou.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model_nou.fit(X_train, y_train, epochs=3, batch_size=32)

test_loss, test_acc = model_nou.evaluate(X_test, y_test, verbose=0)
print(f"Noua acuratete: {test_acc * 100:.2f}%")


'''
INTERPRETARE REZULTATE EXERCITIUL 5:
1. Cresterea complexitatii: Prin modificarea numarului de neuroni din stratul 
   ascuns de la 128 la 512, numarul total de parametri antrenabili (ponderi si biasuri) 
   a crescut semnificativ, ajungand de la ~101.000 la 407.050.

2. Impactul asupra performantei: Modelul a devenit mult mai capabil sa memoreze 
   si sa recunoasca detalii fine. Acuratetea pe setul de antrenare a crescut rapid 
   la fiecare epoca, atingand 98.35% in epoca 3, iar pe setul de test s-a obtinut 
   o acuratete finala excelenta de 97.54%.

3. Costul computational: Dezavantajul cresterii numarului de neuroni se vede in 
   timpul de calcul. Fiecare epoca a durat in jur de 30-40 de secunde deoarece 
   procesorul (CPU) a avut de efectuat de 4 ori mai multe operatii matematice.
'''