# https://codeplasma.com/2012/12/03/getting-webcam-images-with-python-and-opencv-2-for-real-this-time/
import cv2

camera_port = 0                             # default webcam port
webcam = cv2.VideoCapture(camera_port)      # init camera object w/ index of cam port

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
        cv2.imshow('frame window', frame)       # show frame

        # check if frame is blocking here


        print(frame)
        # wait 1 miliseond, & 0xFF to allow for 64 bit machines
        key = cv2.waitKey(1)                     # key pressed
        if key & 0xFF == ord('q'):               # key pressed was q
            print("Killing webcam")
            break

    else:
        print("Error: ret = " + str(ret))

"""
note: 0xFF
nding an integer with 0xFF leaves only the least significant byte. For example, to get the first byte in a short s,
you can write s & 0xFF. This is typically referred to as "masking". If byte1 is either a single byte type
(like uint8_t) or is already less than 256 (and as a result is all zeroes except for the least significant byte) there
is no need to mask out the higher bits, as they are already zero.
"""