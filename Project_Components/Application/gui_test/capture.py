import sys
import os
from PyQt4 import QtCore, QtGui
from mai import Generic_UI, GenericThread

class Capture_UI(Generic_UI):
    def __init__(self):
        super(Capture_UI, self).__init__()
        self.window = 1
        # FPS label
        self.lbFPS = QtGui.QLabel("FPS:", self)
        self.lbFPS.setGeometry(QtCore.QRect(530, 210, 59, 16))
        # seconds spinbox
        self.spbSecs = QtGui.QSpinBox(self)
        self.spbSecs.setGeometry(QtCore.QRect(430, 210, 48, 24))
        self.spbSecs.setMinimum(1)
        self.spbSecs.setMaximum(300)
        self.spbSecs.setProperty("value", 30)
        # make default checkbox
        self.cbMkDefault = QtGui.QCheckBox(self)
        self.cbMkDefault.setGeometry(QtCore.QRect(660, 210, 111, 21))
        # seconds label
        self.lbSecs = QtGui.QLabel("Seconds:", self)
        self.lbSecs.setGeometry(QtCore.QRect(360, 210, 59, 16))
        # record push button
        self.pbRec = QtGui.QPushButton("Record", self)
        self.pbRec.setGeometry(QtCore.QRect(160, 210, 113, 32))
        self.pbRec.clicked.connect(self.recordSetUp)
        # control panel push button
        self.pbCtrlP = QtGui.QPushButton("Control Panel", self)
        self.pbCtrlP.setGeometry(QtCore.QRect(160, 110, 113, 32))
        # FPS spinbox
        self.spbFPS = QtGui.QSpinBox(self)
        self.spbFPS.setGeometry(QtCore.QRect(580, 210, 48, 24))
        self.spbFPS.setMinimum(1)
        self.spbFPS.setMaximum(200)
        self.spbFPS.setProperty("value", 100)

    def recordSetUp(self):
        self.genericThread = GenericThread(self.record)
        self.genericThread.start()
        # disable button after click
        self.pbRec.setEnabled(False)

    def record(self):
        print 'initiating leap_record.py'
        currentPath = os.curdir
        filePath = currentPath + '/lib/leap_record.py'
        os.system('python ' + filePath)
        print 'leap_record.py finished'
        # re enable button
        self.pbRec.setEnabled(True)





def main():

    global curWindow
    curWindow = 1
    app = QtGui.QApplication(sys.argv)
    captureWindow = Capture_UI()
    global windows
    windows = [captureWindow]
    captureWindow.show_window()
    print captureWindow.geometry()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


