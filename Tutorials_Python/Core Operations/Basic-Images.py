'''
Almost all the operations in this section is mainly related to Numpy rather than
OpenCV. A good knowledge of Numpy is required to write better optimized code with
OpenCV.

'''

import cv2, os
import numpy as np

parentdir = os.path.dirname(os.getcwd())
respath = parentdir + '/Resources/'

img = cv2.imread(respath+'ky.jpg')

'''
You can access a pixel value by its row and column coordinates.
For BGR image, it returns an array of Blue, Green, Red values.
For grayscale image, just corresponding intensity is returned.
'''

# get pixel val
    # row ,  col
px = img[523,342]
print px

blue = img[100,100,0]   # 0th element in Z colour array = blue element/value
print blue

'''
opencvIMGrepby3Dnumpy[Xval4pixl, Yval4pixl, colour(B,G,R)]
An image in OpenCV is represented as a 3D numpy ndarray.
The first two axes (X and Y) represent the pixel matrix. The third axis (Z) contains the color channels (B,G,R).
What you are doing in this line, is selecting a pixel by x, y and z coordinates.
The third index (the 0) in img[100,100,0] is the 0'th element in the array of the pixel's color values [B,G,R],
thus your blue color channel.
'''

# modify pixel
img[523,342] = [255,0,0]
# make a section blue
for x in range(100,300):
    for y in range(100,300):
        img[x,y] = [255,0,0]
print img[412,123] # B,G,R breakdown for that pixel
'''
Numpy is a optimized library for fast array calculations. So simply accessing each and every pixel values and modifying it will be very slow and it is discouraged
Above mentioned method is normally used for selecting a region of array, say first 5 rows and last 3 columns like that.
For individual pixel access, Numpy array methods, array.item() and array.itemset() is considered to be better.
But it always returns a scalar. So if you want to access all B,G,R values, you need to call array.item() separately for all.
'''

# better method
# accessing red val
print str(img.item(523,342,2)) + ': pixel @ 523,342 red val'
# modifying pixel val
setval = 230
img.itemset((523,342,2), setval)
print str(img.item(523,342,2)) + ': modified pixel @ 523,342 red val'

# accessing image properties
print img.shape
# (rows, cols, 3 if colour)
#(864, 1536,3) is output

ims = np.zeros((512,231), np.uint8)
print str(ims.shape) + ': no colour img'
# grayscale - just 2 values get printed as no colour
print 'total below'
print img.size # total no of pixles

print img.dtype # img.dtype is very important while debugging because a large number of errors in OpenCV-Python code is caused by invalid datatype.

# ROI - region of images
#ROI is again obtained using Numpy indexing

partOfKylo = img[150:10, 300:400]
#img[500:
cv2.imshow('d',img)
cv2.waitKey(0)
