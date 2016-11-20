# making own harrcascades https://www.youtube.com/watch?v=jG3bu0tjFbk
import cv2
cap = cv2.VideoCapture('./video-res/walkingpeople-1.mp4') # works
blue = (255, 0, 0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
i = 0
while(cap.isOpened()):
    rets, image = cap.read()
    orig = image.copy

    # work here
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # make it gray
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print faces
    for (x, y, w, h) in faces:
        print("x: %s, y: %s, w: %s, h: %s" % (x, y, w, h))
        cv2.rectangle(image, (x,y), (x + w, y + h), blue, 2)    # draw blue rectange
    cv2.rectangle(image, (0, 50), (40, 60), (0, 255, 0), 2)
    cv2.imshow('frame', image)
    key = cv2.waitKey(1)                     # key pressed
    if key & 0xFF == ord('q'):               # key pressed was q
        print("Killing ..")
        break

# keyboard binding function. Its argument is the time in milliseconds. The function waits for specified milliseconds for any keyboard event. If you press any key in that time, the program continues.
cap.release()
cv2.destroyAllWindows()