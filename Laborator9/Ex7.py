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

model_tanh = Sequential([
    Dense(128, input_shape=(784,), activation='tanh'),
    Dense(10, activation='softmax')
])

model_tanh.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model_tanh.fit(X_train, y_train, epochs=3, batch_size=32)

test_loss, test_acc = model_tanh.evaluate(X_test, y_test, verbose=0)
print(f"Acuratete cu tanh: {test_acc * 100:.2f}%")