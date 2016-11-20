import numpy as np
import cv2
import imutils
from imutils import paths

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image_paths = list(paths.list_images("./frontalfaces"))
blue = (255, 0, 0)
for image_path in image_paths:

    image = cv2.imread(image_path)
    orig = image.copy

    # work here
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # make it gray
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print faces
    for (x, y, w, h) in faces:
        print("x: %s, y: %s, w: %s, h: %s" % (x, y, w, h))
        cv2.rectangle(image, (x,y), (x + w, y + h), blue, 2)    # draw blue rectange
    cv2.rectangle(image, (0, 50), (40, 60), (0, 255, 0), 2)
    cv2.imshow('frame', image)
    cv2.waitKey(0)
# https://codeplasma.com/2012/12/03/getting-webcam-images-with-python-and-opencv-2-for-real-this-time/

