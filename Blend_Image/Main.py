"""
@author: David Lei
@since: 14/04/2016
@modified: 

Note: in open cv

0                       width max
height max




0
"""

def show_img(img):
    import cv2
    cv2.imshow("window", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)

def ipa1():
    import cv2

    # pic1_name = raw_input("Enter the name of the file for the first picture (building): ")
    pic1 = Picture("RMIT_Building.jpg")

    show_img(pic1.image)

    # pic2_name = raw_input("Enter the name of the file for the second picture (logo): ")
    pic2 = Picture("RMIT_Logo.jpg")

    show_img(pic2.image)

    pic1_center = pic1.get_center()
    pic2_center = pic2.get_center()
    # big - small
    difference_width = pic1_center[0] - pic2_center[0]
    difference_height = pic1_center[1] - pic2_center[1]

    print "pic 1 details"
    print "width: " + str(pic1.get_width())
    print "height: " + str(pic1.get_height())
    print "pic 2 details"
    print "width: " + str(pic2.get_width())
    print "height: " + str(pic2.get_height())

    for i in range(pic2.get_width()):
        for j in range(pic2.get_height()):
            # Picture.image[height_coord, width_coord]
            logo_pix = pic2.image[j, i]
            building_pix = pic1.image[j+difference_width, i+difference_height]
            new_logo_pix = [x/2 for x in logo_pix]
            new_building_pix = [x/2 for x in building_pix]
            blend_values = [new_logo_pix[k]+new_building_pix[k] for k in range(3)]

            pic1.image[j+difference_width, i+difference_height] = blend_values          # pix here * 0.5 + pix there * 0.5

    show_img(pic1.image)

    # draw border
    pic1_width = pic1.get_width()
    pic1_height = pic1.get_height()

    # img[y,x] --> don't use x,y to reference a pixel

    # bottom border
    for i in range(4):
        for k in range(pic1_width):
            pic1.image[pic1_height-1-i, k] =[0, 0, 0]     # black

    # top border
    for i in range(4):
        for k in range(pic1_width):
            pic1.image[i, k] =[0, 0, 0]                 # black

    # left side border
    for i in range(4):
        for k in range(pic1_height):
            pic1.image[k, i] =[0, 0, 0]                 # black

    # right side border
    for i in range(4):
        for k in range(pic1_height):
            pic1.image[k, pic1_width-1-i] =[0, 0, 0]      # black

    show_img(pic1.image)

    # save image
    cv2.imwrite("RMIT_photo_colour.jpg", pic1.image)

    # gray colour image
    gray_image = cv2.cvtColor(pic1.image, cv2.COLOR_BGR2GRAY)

    # save image
    cv2.imwrite("RMIT_photo_grayscale.jpg", gray_image)

    show_img(gray_image)



class Picture:
    def __init__(self, name):
        import cv2
        self.image = cv2.imread(name)
        self.name = name
        self.shape = self.image.shape
        self.no_rows = self.shape[0]
        self.no_cols = self.shape[1]

    def image(self):
        return self.image

    def get_center(self):
        width = self.no_cols
        height = self.no_rows
        return width/2, height/2

    def get_width(self):
        return self.no_cols

    def get_height(self):
        return self.no_rows


if __name__ == "__main__":
    ipa1()
    print "Done"
