import sys
import os
libPath = os.path.join(os.path.curdir, 'lib')
sys.path.insert(0,libPath)

import ctypes
import numpy
from PIL import Image
import uuid
import pdb

try:
    try:
        import Leap
        from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
    except ImportError:
        sys.path.append('/Users/David/Library/Python/2.7/lib/python/site-packages/LeapMotion')
        #print(sys.path)
        import Leap
except ImportError:
    print'unable to locate path to Leap Motion SDK packages'

class SampleListener(Leap.Listener):
    #guid=""
    #leftPath=""
    #rightPath=""
    def __init__(self):
        super(SampleListener, self).__init__()

        #guid = (str(uuid.uuid1())).upper()
        #self.leftPath = os.path.join(os.path.curdir,'images',guid,'left')
        #self.rightPath = os.path.join(os.path.curdir,'images',guid,'right')
        #os.makedirs(self.leftPath)
        #os.makedirs(self.rightPath)

    def on_connect(self, controller):
        print "Connected"
        controller.set_policy(Leap.Controller.POLICY_IMAGES)
    def on_frame(self, controller):
        print "Frame available"
        frame = controller.frame()
        id=str(frame.id)
        image_list = frame.images
        if not image_list.is_empty:
                print '********* Got Images ***********'
        else: return
        image = image_list[0]
        #fileName= os.path.join(self.leftPath,id+".png")
        fileName = 'a.png'
        save_leap_image(image,fileName)

        image = image_list[1]
        #fileName= os.path.join(self.rightPath,id+".png")
        save_leap_image(image,fileName)

def save_leap_image(image,fileName):
    image_buffer_ptr = image.data_pointer
    ctype_array_def = ctypes.c_ubyte * image.width * image.height

    # as ctypes array
    as_ctype_array = ctype_array_def.from_address(int(image_buffer_ptr))
    # as numpy array
    as_numpy_array = numpy.ctypeslib.as_array(as_ctype_array)
    img = Image.fromarray(as_numpy_array)
    print img
    img.save(fileName)

def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()
    print 'listener:'
    print type(listener)
    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)

if __name__=="__main__":
    main()
