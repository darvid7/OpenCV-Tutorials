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


abc = np.zeros((4,4,3),np.uint8)
print abc
print '---'
print abc[2:3]

a = np.array([0,1,2,3,4,5,6,7,8,9])
print(a[1:7:1])
# a[start:stop:step[ returns from start < stop index
print '------'
b = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15], [16,17,18,19,20]])
print b
print '------'
print b[1:2, 4:5]