import cv2
import numpy as np


canvasImage = np.zeros((300,512,3), np.uint8)
# cv2.getTrackbarPos() - specify: trackbar_name, window_name, default value, max_value, callbackfn-executed every time trackbar val changes
canvasI2 = np.zeros((300,512,3))
canvasI3 = np.zeros((300,500))
thing = np.zeros((200,100))
'''
>>> np.zeros((2, 1))
array([[ 0.],
       [ 0.]])

       specify row & cols
       2 rows, 1 col of 0s ^

'''
thing1 = np.zeros((100,100), np.uint8)

thing2 = np.zeros((300,200,3), np.uint8)

idk = np.zeros((562,178, 4), np.uint8,)

while(1):
    cv2.imshow('1', thing)
    cv2.imshow('2', thing1)
    cv2.imshow('3', thing2)
    cv2.imshow('4', canvasImage)
    cv2.imshow('5', canvasI2)
    cv2.imshow('6', canvasI3)

    cv2.imshow('7', idk)
    cv2.waitKey(0)
    break