import cv2

bee = cv2.imread('bee2.png')

if bee.empty():
    print 'empty'
cv2.namedWindow('text')
cv2.imshow('text', bee)

cv2.waitKey(0)