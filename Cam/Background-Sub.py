import cv2
import imutils
from imutils import paths

fbgb = cv2.BackgroundSubtractorMOG2()
image_paths = list(paths.list_images("./top_images"))
for image_path in image_paths:
    image = cv2.imread(image_path)
    orig = image.copy
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # make it gray
    fgmask = fbgb.apply(gray)
    cv2.imshow('frame', fgmask)
    cv2.waitKey(0)
# https://codeplasma.com/2012/12/03/getting-webcam-images-with-python-and-opencv-2-for-real-this-time/

"""
# https://codeplasma.com/2012/12/03/getting-webcam-images-with-python-and-opencv-2-for-real-this-time/
import cv2

camera_port = 0                             # default webcam port
webcam = cv2.VideoCapture(camera_port)      # init camera object w/ index of cam port
fbgb = cv2.BackgroundSubtractorMOG2()

if webcam.isOpened():
    print("webcam open: " + str(webcam.isOpened()))
else:
    print("opening webcam")
    webcam.open()

while(True):
    '''
    "Frame" will get the next frame in the camera (via "cap").
    "Ret" will obtain return value from getting the camera frame, either true of false.
    '''
    ret, frame = webcam.read()
    if ret:
        image = frame

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # make it gray
        fgmask = fbgb.apply(gray)
        cv2.imshow('frame', image)
        # check if frame is blocking here


        print(frame)
        # wait 1 miliseond, & 0xFF to allow for 64 bit machines
        key = cv2.waitKey(1)                     # key pressed
        if key & 0xFF == ord('q'):               # key pressed was q
            print("Killing webcam")
            break

"""