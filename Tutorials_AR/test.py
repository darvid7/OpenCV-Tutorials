# print all functions in OpenCV
import cv2
funcs = dir(cv2)
for f in funcs:
    print(f)


# use xfeatures2d to access opencv contrib??
image = cv2.imread("test_image.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
sift = cv2.xfeatures2d.SIFT_create()
(kps, descs) = sift.detectAndCompute(gray, None)
print("# kps: {}, descriptors: {}".format(len(kps), descs.shape))

# kps: 6955, descriptors: (6955, 128)