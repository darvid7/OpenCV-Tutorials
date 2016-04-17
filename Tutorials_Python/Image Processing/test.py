import numpy as np
import cv2
import sys
import os



currentPath = os.path.abspath(os.getcwd())
print currentPath

oneFolderUp = os.path.dirname(os.getcwd())
print oneFolderUp

newpath = oneFolderUp + '/Resources'
print newpath

'''

bee1 = cv2.imread(newpath + '/beef1.jpg', 0)
cv2.namedWindow('window1')
cv2.imshow('window1',bee1)

bee2 = cv2.imread(newpath + '/beef2.jpg', 0)
cv2.namedWindow('window2')
cv2.imshow('window2', bee2)
'''

bee3 = cv2.imread(newpath + '/beef3.jpg', 1)
cv2.namedWindow('window3')
cv2.imshow('window3', bee3)

bee4 = cv2.imread(newpath + '/beef4.jpg', 0)
cv2.namedWindow('window4')
cv2.imshow('window4', bee4)

cpy = cv2.imread(newpath + '/cpy.jpg',1)

print cv2.__version__
cv2.waitKey(0)

print bee3.shape

for x in range (400): # x axis
    for  y in range(599): # y axis
        imgBlue = bee3[x,y,0]
        imgGreen = bee3[x,y,1]
        imgRed = bee3[x,y,2]

        if imgGreen > 50:
            imgGreen = 50

        bee3[x,y] = [imgBlue, imgGreen, imgRed]

cv2.namedWindow('edited Bee3')
cv2.imshow('edited Bee3', bee3)

cv2.waitKey(0)

yVal = 304
xVal = 316

print cpy[xVal, yVal]

boundBlue = 99
boundGreen = 120
boundRed = 131
var = 15

for x in range (448): # x axis
    for  y in range(600): # y axis
        found = False
        imgBlue = cpy[x,y,0]
        imgGreen = cpy[x,y,1]
        imgRed = cpy[x,y,2]

        if imgBlue <= boundBlue + var and imgBlue >= boundBlue - var:
            if imgGreen <= boundGreen + var and imgGreen >= boundGreen - var:
                if imgRed <= boundRed + var and imgRed >= boundRed - var:
                    found = True
        if found:
            pass
        else:
            cpy[x,y] = [0,0,0]
cv2.namedWindow('new window')
cv2.imshow('new window', cpy)

cv2.waitKey(0)