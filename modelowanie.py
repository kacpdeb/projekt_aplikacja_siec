import os
os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"


import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.datasets import mnist 
from keras import layers 
from keras import models 
from keras.utils import to_categorical
from matplotlib.image import imread
import numpy as np

(X_train, y_train), (X_test, y_test) = mnist.load_data()
train_images = X_train.reshape((60000, 28, 28, 1)) 
test_images = X_test.reshape((10000, 28, 28, 1)) 
train_images = train_images.astype('float32') / 255
test_images = test_images.astype('float32') / 255
train_labels = to_categorical(y_train) 
test_labels = to_categorical(y_test)
num_classes = test_labels.shape[1]
model = models.Sequential() 
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1))) 
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu')) 
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(num_classes, activation='softmax'))
model.summary()
checkpoint = ModelCheckpoint('weights.hdf5', monitor='loss', verbose=1, save_best_only=True, mode='min', period=1)
model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=15, batch_size=64 , callbacks = [checkpoint])
test_loss, test_acc = model.evaluate(test_images, test_labels) 
print(test_loss, test_acc)
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
model.save_weights("model.h5")
print("Saved model to disk")