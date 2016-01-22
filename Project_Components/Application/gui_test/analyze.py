import sys
import os
from PyQt4 import QtCore, QtGui
from mai import Generic_UI, GenericThread

class Analyze_UI(Generic_UI):
    def __init__(self):
        super(Analyze_UI, self).__init__()
        self.window = 2

        # image label
        self.lbImage = QtGui.QLabel("Hello",self)
        self.lbImage.setGeometry(QtCore.QRect(40, 60, 500, 300))

        self.set_image()

        # average push button
        self.pbAvg = QtGui.QPushButton("Average", self)
        self.pbAvg.setGeometry(QtCore.QRect(550, 190, 113, 32))
        # track push button
        self.pbTrack = QtGui.QPushButton("Track", self)
        self.pbTrack.setGeometry(QtCore.QRect(550, 230, 113, 32))
        # load img push button
        self.pbLoadImg = QtGui.QPushButton("Load image", self)
        self.pbLoadImg.setGeometry(QtCore.QRect(550, 150, 113, 32))
        # report push button
        self.pbReport = QtGui.QPushButton("Report",self)
        self.pbReport.setGeometry(QtCore.QRect(550, 270, 113, 32))
        # progress bar for images processed
        self.progressBar = QtGui.QProgressBar(self)
        self.progressBar.setGeometry(QtCore.QRect(50, 380, 431, 41))
        self.progressBar.setProperty("value", 0)
        # prev push button
        self.pbPrev = QtGui.QPushButton("Previous", self)
        self.pbPrev.setGeometry(QtCore.QRect(110, 420, 113, 32))
        # next push button
        self.pbNext = QtGui.QPushButton("Next", self)
        self.pbNext.setGeometry(QtCore.QRect(250, 420, 113, 32))
        # Select album push button
        self.pbSelAlbum = QtGui.QPushButton("Select Album", self)
        self.pbSelAlbum.setGeometry(QtCore.QRect(550, 120, 113, 32))

    def set_image(self):
        # pyqt browse picker
        self.imgPath = "/Users/David/PycharmProjects/OpenCV-Project/Project_Components/Application/lib/blank.jpg"
        self.img = QtGui.QPixmap(self.imgPath)
        self.scaledImg = self.img.scaled(self.lbImage.size(), QtCore.Qt.KeepAspectRatio)
        self.lbImage.setPixmap((self.scaledImg))
        self.lbImage.show()


def main():

    global curWindow
    curWindow = 1
    app = QtGui.QApplication(sys.argv)
    analyzeWindow = Analyze_UI()
    global windows
    windows = [analyzeWindow]
    analyzeWindow.show_window()
    print analyzeWindow.geometry()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()