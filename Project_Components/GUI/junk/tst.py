import sys
from PyQt4 import QtCore, QtGui
from PyQt4 import *

app = QtGui.QApplication(sys.argv)

print 'img start'
label = QtGui.QLabel('text')
label.setGeometry(50,50,100,100)

myPixmap = QtGui.QPixmap("/Users/David/PycharmProjects/OpenCV-Project/Project_Components/Application/lib/bee2.png")
myScaledPixmap = myPixmap.scaled(label.size(), QtCore.Qt.KeepAspectRatio)
label.setPixmap(myScaledPixmap)

label.show()

print 'img end'

sys.exit(app.exec_())