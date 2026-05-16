import numpy as np
import matplotlib.pyplot as plt
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

model = Sequential([
    Dense(128, input_shape=(784,), activation='relu'),
    Dense(10, activation='softmax')
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=3, batch_size=32, verbose=1)

index_imagine = 0
imagine_test = X_test[index_imagine]
eticheta_reala = y_test[index_imagine]

imagine_pentru_predictie = np.expand_dims(imagine_test, axis=0)
predictii_probabilitati = model.predict(imagine_pentru_predictie)
cifra_prezisa = np.argmax(predictii_probabilitati)

imagine_2d = imagine_test.reshape(28, 28)
plt.figure(figsize=(5, 5))
plt.imshow(imagine_2d, cmap='gray')
plt.title(f"Reala: {eticheta_reala} | Predictie: {cifra_prezisa}")
plt.axis('off')
plt.show()