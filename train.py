import tensorflow as tf
import cv2
from matplotlib import pyplot as plt
from tensorflow.keras import layers, models
import numpy as np
import random

TARGET = 75
outputs = open('./input.csv', 'r').readlines()

def get_sets():
    inputs_train = []
    outputs_train = []
    inputs_test = []
    outputs_test = []
    for i in range(TARGET):
        input = cv2.imread("./inputs/{}.jpg".format(i))
        input = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)
        input = input / 255.0
        input = input.reshape((96, 144, 1))
        output = outputs[1 + i][:-1].split(',')[1:]
        output = [float(i) for i in output]
        output = np.array(output)
        if (random.random() > 0.90):
            inputs_test.append(input)
            outputs_test.append(output)
        else:
            inputs_train.append(input)
            outputs_train.append(output)
    return (np.array(inputs_train), np.array(outputs_train), np.array(inputs_test), np.array(outputs_test))

inputs, outputs, inputs_test, outputs_test = get_sets()
print(inputs.shape)
print(outputs.shape)

model = models.Sequential()
model.add(layers.Conv2D(16, (3, 3), activation='relu', input_shape=(96, 144, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(32, (3, 3), activation='relu'))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Conv2D(64, (3, 3), activation='relu'))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Conv2D(128, (3, 3), activation='relu'))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Conv2D(256, (3, 3), activation='relu'))
# model.add(layers.Flatten())
# model.add(layers.Dense(1000, activation='relu'))
# model.add(layers.Dense(500, activation='relu'))
model.add(layers.Dense(100, activation='relu'))
model.add(layers.Dense(6, activation='relu'))
model.summary()

model.compile(optimizer='adam',
              loss=tf.keras.losses.MeanSquaredError())

history = model.fit(inputs, outputs, validation_data=(inputs_test, outputs_test), epochs=20)

model.save('model')

plt.figure()
plt.plot(history.history['loss'], color='red', label='Loss')
plt.plot(history.history['val_loss'], color='blue', label='Val Loss')
plt.legend()
plt.show()
