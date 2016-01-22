'''
img : The image where you want to draw the shapes

color : Color of the shape. for BGR, pass it as a tuple, eg: (255,0,0) for blue. For grayscale, just pass the scalar value.

thickness : Thickness of the line or circle etc. If -1 is passed for closed figures like circles, it will fill the shape. default thickness = 1

lineType : Type of line, whether 8-connected, anti-aliased line etc. By default, it is 8-connected. cv2.LINE_AA gives anti-aliased line which looks great for curves.

note, need to show the image for things to be seen on screen (online tute left this bit out)

'''
import numpy as np
import cv2

# Create a black image to draw things on
imgDrawOn = np.zeros((512,512,3), np.uint8)
'''
                    # x value, y value, z value (i think)
                    # if just (512,512) then colour space = black & white
                    # since 3 values we have x,y,z axis and colour space = BGR

the canvas is like  0                   512,0





                    0,512               512,512
'''
# Draw line - specify 2 points
linePoint1 = (0,0) # x value
linePoint2 = (512,512) # y value
colour = (255,0,0) # Blue, Green, Red, in thise case just blue
thickness = 5
cv2.line(imgDrawOn,linePoint1, linePoint2, colour, thickness)

cv2.line(imgDrawOn,(0,512), (512,0), (0,255,0), thickness)
cv2.line(imgDrawOn, (0,500), (512, 500), (0,0,255),thickness)

# Draw a rectangle  - specify top left & bottom right corner
#                      pt1      pt2     colour  thickness
cv2.rectangle(imgDrawOn,(384,0),(510,128),(255,255,0),3)    # can mix colours
                    # top left corner, bottom right corner

# Draw circle - specify center & radius

# cv.Circle(img, center, radius, color, thickness=1, lineType=8, shift=0)
cv2.circle(imgDrawOn,(447,63), 63, (255,0,255),-1)
            # notice thickness = -1, means shade the drawing in

# Draw ellipse - specify center, axes lengths (major axis, minor axis)

# cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color[, thickness[, lineType[, shift]]])

#  angle  - in anticlockwise dir
# startAngle and endAngle denotes the starting and ending of ellipse arc measured in clockwise direction from major axis.
# 0 & 360 will give the full ellipse

center = (256,256)
major, minor = 100,50
axes = (major, minor)
angleOfEllipse = 45
startAngle = 0
endAngle = 180
colour = (200,255,255)
thickness = 9
cv2.ellipse(imgDrawOn, center, axes, angleOfEllipse, startAngle, endAngle, colour, thickness )
# note it doesn't draw the line connecting the arc

# Draw a polygon
'''
a plane figure with at least three straight sides and angles, and typically five or more.

To draw a polygon, first you need coordinates of vertices. Make those points into
an array of shape ROWSx1x2 where ROWS are number of vertices and it should be of type int32

cv2.polylines(img, pts, isClosed, color[, thickness[, lineType[, shift]]])
'''
setOfPoints = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)  # need to do
reshaped = setOfPoints.reshape((-1,1,2))                            # these

# myArr = [[10,5],[20,30],[70,20],[50,10]] # Wont work - TypeError: pts is not a numpy array, neither a scalar

cv2.polylines(imgDrawOn,[reshaped],True,(0,255,255),5) # notice [reshaped] will draw the lines connecting dots
cv2.polylines(imgDrawOn, reshaped, True, (255,0,255),6)  # will just draw dots


# add text
'''
specify:
- Text data that you want to write
- Position coordinates of where you want put it (i.e. bottom-left corner where data starts).
- Font type (Check cv2.putText() docs for supported fonts)
- Font Scale (specifies the size of font)
regular things like color, thickness, lineType etc.
For better look, lineType = cv2.LINE_AA is recommended.
..
CV_FONT_HERSHEY_SIMPLEX normal size sans-serif font
CV_FONT_HERSHEY_PLAIN small size sans-serif font
CV_FONT_HERSHEY_DUPLEX normal size sans-serif font (more complex than CV_FONT_HERSHEY_SIMPLEX )
CV_FONT_HERSHEY_COMPLEX normal size serif font
CV_FONT_HERSHEY_TRIPLEX normal size serif font (more complex than CV_FONT_HERSHEY_COMPLEX )
CV_FONT_HERSHEY_COMPLEX_SMALL smaller version of CV_FONT_HERSHEY_COMPLEX
CV_FONT_HERSHEY_SCRIPT_SIMPLEX hand-writing style font
CV_FONT_HERSHEY_SCRIPT_COMPLEX more complex variant of CV_FONT_HERSHEY_SCRIPT_SIMPLEX

cv.PutText(img, text, org, font, color)

    org Bottom-left corner of the text string in the image.
    font CvFont structure initialized using InitFont().
    fontFace Font type. One of FONT_HERSHEY_SIMPLEX, FONT_HERSHEY_PLAIN, FONT_HERSHEY_DUPLEX, FONT_HERSHEY_COMPLEX, FONT_HERSHEY_TRIPLEX, FONT_HERSHEY_COMPLEX_SMALL, FONT_HERSHEY_SCRIPT_SIMPLEX, or FONT_HERSHEY_SCRIPT_COMPLEX, where each of the font ID can be combined with FONT_ITALIC to get the slanted letters.
'''
font = cv2.FONT_HERSHEY_SIMPLEX
text = 'OpenCV'
colour = (255,255,255) # is white
thickness = 2
#lineType = cv2.LINE_AA
# print cv2.CV_AA for open cv2 the above wont work

cv2.putText(imgDrawOn,text,(10,500), font, 4, colour, thickness)
# cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA


# draw on a saved image
actualImage = cv2.imread('Images_filename.png')
cv2.circle(actualImage, (250,250), 50, (100,100,255),4)
cv2.putText(actualImage, 'IMA BEE', (20,500), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,255,255), 5)

# use the following to display the images with all the drawings
while (True):

    cv2.imshow('Window: drawing',imgDrawOn)
    cv2.imshow('Window: draw on image', actualImage)
   # cv2.imshow('a', testimg)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()

# can help http://docs.opencv.org/2.4/modules/core/doc/drawing_functions.html
