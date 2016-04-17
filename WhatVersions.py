import cv2
import numpy
import matplotlib
import sys
import PIL

print'\nPython: ', str(sys.version)
print '\n\nNumpy: ', str(numpy.__version__)
print'Matplotlib: ', str(matplotlib.__version__)
print'OpenCV: ', str(cv2.__version__)
print 'PIL: ', str(PIL.VERSION)
print 'Pillow: ', str(PIL.PILLOW_VERSION)
# to get open cv v 2.x.x this works https://jjyap.wordpress.com/2014/05/24/installing-opencv-2-4-9-on-mac-osx-with-python-support/
# to get open cv v 3 pyimsearch works
# can do this on python 3 or 2 and open cv 3 or 2, which ever is easiest for me

print '\n~~PyQt4 things~~'
from PyQt4.QtCore import QT_VERSION_STR
from PyQt4.pyqtconfig import Configuration

print "Qt version:", QT_VERSION_STR
cfg = Configuration()
print "SIP version:", cfg.sip_version_str
print "PyQt version:", cfg.pyqt_version_str



