import tensorflow as tf
import cv2
import numpy as np

model = tf.keras.models.load_model('model')
model.summary()

cap = cv2.VideoCapture(0)

def predict(input):
    input = input.reshape((96, 144, 1))
    input = input / 255.0
    prediction = model.predict(np.array([input]))
    prediction = prediction[0].tolist()
    return prediction

while(True):
    ret, frame = cap.read()

    source = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    input = cv2.resize(source, (int(720 * 0.20), int(480 * 0.20)))
    values = predict(input)
    print(values)
    cv2.circle(source, (int(values[0] * 8.88888), int(values[1] * 7.5)), 5, (255, 0, 0), -1)
    cv2.circle(source, (int(values[2] * 8.88888), int(values[3] * 7.5)), 5, (0, 255, 0), -1)
    cv2.circle(source, (int(values[4] * 8.88888), int(values[5] * 7.5)), 5, (0, 0, 255), -1)
    cv2.imshow('frame', source)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
