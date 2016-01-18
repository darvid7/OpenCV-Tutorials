import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourCC = cv2.VideoWriter_fourcc('I','Y','U','V')
fps = int(cap.get(5))
height = int(cap.get(4))
width = int(cap.get(3))
print(fourCC)
fourcc = cv2.VideoWriter_fourcc(*'MP42')
out = cv2.VideoWriter('output.avi',fourCC, fps,(width,height))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()