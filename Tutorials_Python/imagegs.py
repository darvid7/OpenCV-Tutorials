import numpy as np
import cv2
import sys
import os

print cv2.__version__
'''
currentPath = os.path.abspath(os.getcwd())
print currentPath

oneFolderUp = os.path.dirname(os.getcwd())
print oneFolderUp

newpath = oneFolderUp + '/Resources'
print newpath


bee1 = cv2.imread(newpath + '/bee.jpg')
cv2.namedWindow('window1')
cv2.imshow('window1',bee1)

bee2 = cv2.imread(newpath + '/bee.jpg')
cv2.namedWindow('window2')
cv2.imshow('window2', bee2)

cv2.waitKey(0)
'''