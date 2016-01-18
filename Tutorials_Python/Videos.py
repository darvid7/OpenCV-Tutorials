import numpy as np
import cv2

# to cap video need to create a VideoCapture object
# argument can be device index or name of video file
# device index is number to specify cam
# pass 0 for cam 1, 1 for second cam ...

videoCapObj = cv2.VideoCapture(0)

if videoCapObj.isOpened():
    print(videoCapObj.isOpened())
else:
    videoCapObj.open()

while(True):
    # capture frame by frame
    ret, frame = videoCapObj.read()
    '''
    "Frame" will get the next frame in the camera (via "cap").
    "Ret" will obtain return value from getting the camera frame,
    either true of false.
    '''
    # operations on the frame
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # display resulting frame
    cv2.imshow('frame window', grayframe)

    # wait 1 miliseond, & 0xFF to allow for 64 bit machines
    # if ord q then break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(videoCapObj.read())
        break
    # does same thing, easier for me to understand V
    '''
    k = cv2.waitKey(1)
    if k & 0xFF:
        if k == ord('q'):
            break
    '''



# release capture when it is done
videoCapObj.release()
cv2.destroyAllWindows()

print('Can capture vid')
# playing vid from file

cap = cv2.VideoCapture('Resources/beePol.mp4')

while(cap.isOpened()):
    rets, aframe = cap.read()

    gray = cv2.cvtColor(aframe,cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame window', gray)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
# keyboard binding function. Its argument is the time in milliseconds. The function waits for specified milliseconds for any keyboard event. If you press any key in that time, the program continues.
cap.release()
cv2.destroyAllWindows()

print('can load vid')
# works ! :D


# saving video

'''
create a VideoWriter object
specify
- output file name
- FourCC code, 4 byte code to specify video codec (platform dependent)
FourCC code is passed as cv2.VideoWriter_fourcc('M','J','P','G') or cv2.VideoWriter_fourcc(*'MJPG) for MJPG.
- fps
- frame size
- isColour flag, either colour if T else grayscale
'''

capture = cv2.VideoCapture(0)
height = capture.get(4)
width = capture.get(3)

'''
You can also access some of the features of this video using cap.get(propId) method where propId is a number from 0 to 18. Each number denotes a property of the video (if it is applicable to that video) and full details can be seen here: Property Identifier. Some of these values can be modified using cap.set(propId, value). Value is the new value you want.

For example, I can check the frame width and height by cap.get(3) and cap.get(4). It gives me 640x480 by default. But I want to modify it to 320x240. Just use ret = cap.set(3,320) and ret = cap.set(4,240).

'''
print('h x w')
print(height)
print(width)
fourCC = cv2.VideoWriter_fourcc('I','4','2','0')
#f4cc = int(capture.get(6))
fps = int(capture.get(5))               # -1 works here in windows
outputV = cv2.VideoWriter('outputvMAC.avi',fourCC, 20, (int(width), int(height)))

'''
on mac there are some issues with fourCC, I cant seem to play vids that are written from a mac
the following work on a windows machine and can be played via vlc player
fourcc.cv2.VideoWriter_fourcc('I','4','2','0')
-1 # allowing you to pick what format
'''

while(capture.isOpened()):
    ret, frame1 = capture.read()
    if ret == True:                 # captured something
        frame1 = cv2.flip(frame1, 0)  # flip the frame

        # write the flipped frame
        outputV.write(frame1)

        cv2.imshow('frame', frame1)
        if cv2.waitKey(1) & 0xFF == ord ('q'):
                break
    else:
        break   # not capturing
print('outside cap loop')
# release all
capture.release()
outputV.release()
cv2.destroyAllWindows()
print('can save vid')
# osx issues: http://stackoverflow.com/questions/4872383/how-to-write-a-video-file-with-opencv