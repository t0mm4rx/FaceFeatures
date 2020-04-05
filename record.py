import numpy as np
import cv2
import time
import random

cap = cv2.VideoCapture(0)

inputs = []
TARGET = 75

while(True):
    ret, frame = cap.read()

    source = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    input = cv2.resize(source, (int(720 * 0.20), int(480 * 0.20)))
    source = cv2.imshow('frame', source)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if (random.random() > .80):
        inputs.append(input)
        print("{:2f}%".format(len(inputs) / TARGET * 100))
        if (len(inputs) >= TARGET):
            break

cap.release()
cv2.destroyAllWindows()

for i, input in enumerate(inputs):
    cv2.imwrite('./inputs/{}.jpg'.format(i), input)
