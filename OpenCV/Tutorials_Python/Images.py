# material from http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_image_display/py_image_display.html#py-display-image


import numpy as np
import cv2

# path to an image
path = 'Resources/bee.jpg'
# read image as: 1=colour, 0=grayscale, -1=unchanged
flag = 1
# read in image
image1 = cv2.imread(path,flag)  # or .imread('path',1)
print(image1) # prints how it is stored

cv2.namedWindow('window1')
cv2.imshow('window1',image1)
# show image
#cv2.imshow('image', image1)
# keyboard binding function that waits milliseconds
milliseconds = 0 # if 0 passed, waits indefinitely for key stroke
cv2.waitKey(milliseconds)
#cv2.destroyAllWindows() # destroy all windows created
# can use destroyWindow('name') for specific

# window_normal so can reszie later, default is window_autosize
cv2.namedWindow('Win name', cv2.WINDOW_NORMAL)
cv2.imshow('Win name', image1)
cv2.waitKey(0)
cv2.destroyWindow('Win name')
cv2.waitKey(0)
cv2.destroyAllWindows()
# works!

# save image, filname, image to save
cv2.imwrite('Images_filename.png', image1)


imageTimeTable = cv2.imread('Resources/timetable.png',0)
cv2.imshow('Window: Timetable', imageTimeTable)
key = cv2.waitKey(0)
if key == 27: # escape key
    cv2.destroyAllWindows()
elif key == ord('s'): # s key
    cv2.imwrite('timetableGrey.png',imageTimeTable)
    cv2.destroyAllWindows()
elif key == ord('n'):
    cv2.imshow('NewWindow', image1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#  If you are using a 64-bit machine, you will have to modify k = cv2.waitKey(0) line as follows : k = cv2.waitKey(0) & 0xFF

# with matplotlib

import matplotlib.pyplot as pyplot
# same as from matplotlib import pyplot
# import matplotlib then matplotlib.pyploy doesnt work though ?
# doesnt work :/


'''
Warning Color image loaded by OpenCV is in BGR mode. But Matplotlib displays in RGB mode. So color images will
not be displayed correctly in Matplotlib if image is read with OpenCV.
'''
pyplot.imshow(image1, cmap='gray', interpolation = 'bicubic') # image1 was read with OpenCV so it came out wrong
pyplot.xticks([])
pyplot.yticks([])
pyplot.show()
# correct colour :D
image2 = pyplot.imread('Resources/bee2.png')
pyplot.imshow(image2, cmap='gray', interpolation= 'bicubic')
pyplot.xticks([])
pyplot.yticks([])
pyplot.show()

# pyplot readings http://matplotlib.org/api/pyplot_api.html
# converting RGB to BGR http://stackoverflow.com/questions/15072736/extracting-a-region-from-an-image-using-slicing-in-python-opencv/15074748#15074748