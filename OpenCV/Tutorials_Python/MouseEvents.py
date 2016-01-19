'''
create a simple application which draws a circle on an image wherever we double-click on it.


First we create a mouse callback function which is executed when a mouse event take place. Mouse event can be anything related to mouse like left-button down, left-button up, left-button double-click etc. It gives us the coordinates (x,y) for every mouse event. With this event and location, we can do whatever we like. To list all available events available, run the following code in Python terminal:

#>>> import cv2
#>>> events = [i for i in dir(cv2) if 'EVENT' in i]
#>>> print events

'''

import cv2
import numpy as np

# mouse callback function
def draw_circle(event,x,y,flags,param):
    #print('called')
    print('event: ', str(event))
   # print('LBDC: ', str(cv2.EVENT_LBUTTONDBLCLK))
  #  print('Move: ', str(cv2.EVENT_MOUSEMOVE))

    if event == cv2.EVENT_LBUTTONDOWN:
    # if event == cv2.EVENT_MOUSEMOVE: # works but not idea
    # if event == cv2.EVENT_LBUTTONDOWN: # works but not ideal
  #      print('event')
        cv2.circle(img,(x,y),100,(255,0,0),-1)

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('imagex')

#print('LBDC: ', str(cv2.EVENT_LBUTTONDBLCLK))
#print('LBD: ', str(cv2.EVENT_LBUTTONDOWN))
#print('Move: ', str(cv2.EVENT_MOUSEMOVE))

# http://docs.opencv.org/master/d7/dfc/group__highgui.html#gsc.tab=0

cv2.waitKey(0)
cv2.setMouseCallback('imagex',draw_circle)
'''
All you have do is to define a callback function in the OpenCV C++ code attaching to the OpenCV window.
That callback function will be called every time, mouse events occur.
That callback function will also give the coordinates of the mouse events. (e.g - (x, y) coordinate of a mouse click).
'''

while(1):
    cv2.imshow('imagex',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()

'''
seems double click wont work, it just comes up as 2 clicks. LDown will work :)
http://stackoverflow.com/questions/32210066/mouse-callback-event-flags-in-python-opencv-osx

*Additional note: actually, the event EVENT_LBUTTONDOWN is the only event that works. Similar to this post,
EVENT_RBUTTONDOWN and the double click events don't work. (A double click registers as two clicks
and appends two sets of coordinates). I've tried this both with the trackpad and with an external mouse.
'''

# cooler example

drawing = False # not drawing, if mouse pressed = drawing
mode = True # toggle using t
ix = -1
iy = -1

# mouse callback function
def draw(event, x, y, flags, param):
    global ix,iy,drawing,mode # declare so can edit, easier than passing in this case
    if event > 0:
        print(event)
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                #cv2.rectangle(imgCanvas, (ix,iy), (x,y), (100,255,100), 3)
                pass
            else:
                #cv2.circle(imgCanvas, (x,y), 5, (50,50,255), 3)
                pass

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode:
               cv2.rectangle(imgCanvas, (ix,iy), (x,y), (100,255,100), 3)
        else:
            cv2.circle(imgCanvas, (x,y), (abs(x-ix)+abs(y-iy))//2, (50,50,255), 3)

imgCanvas = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('Paint :P')
cv2.setMouseCallback('Paint :P', draw)

while(True):
    cv2.imshow('Paint :P', imgCanvas)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('t'):
        mode = not mode
    elif key == 27:
        break

cv2.destroyAllWindows()

# kinda slow but seems to work