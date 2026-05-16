import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

(X_train_raw, y_train), (X_test_raw, y_test) = tf.keras.datasets.fashion_mnist.load_data()

X_train = X_train_raw.reshape(X_train_raw.shape[0], 784) / 255.0
X_test = X_test_raw.reshape(X_test_raw.shape[0], 784) / 255.0

model_fashion = Sequential([
    Dense(128, input_shape=(784,), activation='relu'),
    Dense(10, activation='softmax')
])

model_fashion.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model_fashion.fit(X_train, y_train, epochs=5, batch_size=32)

test_loss, test_acc = model_fashion.evaluate(X_test, y_test, verbose=0)
print(f"Acuratete Fashion MNIST: {test_acc * 100:.2f}%")