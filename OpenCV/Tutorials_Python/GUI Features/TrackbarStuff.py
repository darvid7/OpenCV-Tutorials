#'''
#Here we will create a simple application which shows the color you specify.
#You have a window which shows the color and three trackbars to specify each of B,G,R colors.
#You slide the trackbar and correspondingly window color changes. By default, initial color will be set to Black.

#The callback function always has a default argument which is the trackbar position. In our case, function does nothing, so we simply pass.

#Another important application of trackbar is to use it as a button or switch.
# open CV doenst have button functionality
#So you can use trackbar to get such functionality.
#In our application, we have created one switch in which application works only if switch is ON,
#otherwise screen is always black.

#'''
import cv2
import numpy as np

def nothing(x):
    pass

canvasImage = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('Trackbar exercise')

# create trackbars
trackbarName = 'Red'
windowName = 'Trackbar exercise'
creationValue = 0
maxPosValue = 255
onChangeFunction = nothing
#cv2.createTrackbar(trackbarName, windowName, creationValue, maxPosValue, onChangeFunction)
cv2.createTrackbar('Red', 'Trackbar exercise', 0, 255, nothing)
cv2.createTrackbar('Green', 'Trackbar exercise', 0, 255, nothing)
cv2.createTrackbar('Blue', 'Trackbar exercise', 0, 255, nothing)
# create switch for on/off
switch = '0 : OFF - 1 :ON'
cv2.createTrackbar(switch, 'Trackbar exercise', 0, 1, nothing)

while(True):
    cv2.imshow('Trackbar exercise', canvasImage)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    else:
        print(key)

    # if not break does stuff here in da loop

    # get current positions of trackbars
    red = cv2.getTrackbarPos('Red', 'Trackbar exercise')
    green = cv2.getTrackbarPos('Green', 'Trackbar exercise')
    blue = cv2.getTrackbarPos('Blue', 'Trackbar exercise')
    switchVal = cv2.getTrackbarPos(switch, 'Trackbar exercise')
# cv2.getTrackbarPos() - specify: trackbar_name, window_name, default value, max_value, callbackfn-executed every time trackbar val changes

    if switchVal == 0:
        canvasImage[:] = 0
        print(canvasImage)
    else:
        canvasImage[:] = [blue, green, red]
        print(canvasImage)
'''
above explained:
canvasImage is a numpy construct
[:] = 0 makes it black
[:] = [b,g,r] takes the b,g,r values we get from track bar and make the canvasImage that colour
this is a numpy thing

the numpy construct looks like
     b   g   r   cols
 [[ 82 100 217]
  [ 82 100 217]
  [ 82 100 217]
so we use the value to specify the column value for each pixel or something on those lines
  ...,
  [ 82 100 217]
  [ 82 100 217]
  [ 82 100 217]]]
'''
cv2.destroyAllWindows()