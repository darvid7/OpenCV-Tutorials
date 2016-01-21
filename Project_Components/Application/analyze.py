# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analyze.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Analyze(object):
    def setupUi(self, Analyze):
        Analyze.setObjectName(_fromUtf8("Analyze"))
        Analyze.resize(800, 600)
        self.centralwidget = QtGui.QWidget(Analyze)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lbImage = QtGui.QLabel(self.centralwidget)
        self.lbImage.setGeometry(QtCore.QRect(40, 60, 441, 311))
        self.lbImage.setText(_fromUtf8(""))
        self.lbImage.setPixmap(QtGui.QPixmap(_fromUtf8("../PycharmProjects/OpenCV-Project/OpenCV/Tutorials_Python/Resources/bee.jpg")))
        self.lbImage.setWordWrap(False)
        self.lbImage.setObjectName(_fromUtf8("lbImage"))
        self.pbAvg = QtGui.QPushButton(self.centralwidget)
        self.pbAvg.setGeometry(QtCore.QRect(550, 190, 113, 32))
        self.pbAvg.setObjectName(_fromUtf8("pbAvg"))
        self.pbTrack = QtGui.QPushButton(self.centralwidget)
        self.pbTrack.setGeometry(QtCore.QRect(550, 230, 113, 32))
        self.pbTrack.setObjectName(_fromUtf8("pbTrack"))
        self.pbLoadImg = QtGui.QPushButton(self.centralwidget)
        self.pbLoadImg.setGeometry(QtCore.QRect(550, 150, 113, 32))
        self.pbLoadImg.setObjectName(_fromUtf8("pbLoadImg"))
        self.pbReport = QtGui.QPushButton(self.centralwidget)
        self.pbReport.setGeometry(QtCore.QRect(550, 270, 113, 32))
        self.pbReport.setObjectName(_fromUtf8("pbReport"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(50, 380, 431, 41))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.pbPrev = QtGui.QPushButton(self.centralwidget)
        self.pbPrev.setGeometry(QtCore.QRect(110, 420, 113, 32))
        self.pbPrev.setObjectName(_fromUtf8("pbPrev"))
        self.pbNext = QtGui.QPushButton(self.centralwidget)
        self.pbNext.setGeometry(QtCore.QRect(250, 420, 113, 32))
        self.pbNext.setObjectName(_fromUtf8("pbNext"))
        self.pbSelAlbum = QtGui.QPushButton(self.centralwidget)
        self.pbSelAlbum.setGeometry(QtCore.QRect(550, 120, 113, 32))
        self.pbSelAlbum.setObjectName(_fromUtf8("pbSelAlbum"))
        Analyze.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Analyze)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Analyze.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Analyze)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Analyze.setStatusBar(self.statusbar)

        self.retranslateUi(Analyze)
        QtCore.QMetaObject.connectSlotsByName(Analyze)

    def retranslateUi(self, Analyze):
        Analyze.setWindowTitle(_translate("Analyze", "MainWindow", None))
        self.lbImage.setStatusTip(_translate("Analyze", "Current Image", None))
        self.pbAvg.setStatusTip(_translate("Analyze", "Average background", None))
        self.pbAvg.setText(_translate("Analyze", "Average", None))
        self.pbTrack.setStatusTip(_translate("Analyze", "Start tracking iamges in album", None))
        self.pbTrack.setText(_translate("Analyze", "Track", None))
        self.pbLoadImg.setStatusTip(_translate("Analyze", "Load an image", None))
        self.pbLoadImg.setText(_translate("Analyze", "Load Image", None))
        self.pbReport.setStatusTip(_translate("Analyze", "Generate tracking report", None))
        self.pbReport.setText(_translate("Analyze", "Report", None))
        self.progressBar.setStatusTip(_translate("Analyze", "Tracking progress", None))
        self.pbPrev.setStatusTip(_translate("Analyze", "Previous Image", None))
        self.pbPrev.setText(_translate("Analyze", "Previous", None))
        self.pbNext.setStatusTip(_translate("Analyze", "Next Image", None))
        self.pbNext.setText(_translate("Analyze", "Next", None))
        self.pbSelAlbum.setStatusTip(_translate("Analyze", "Select album to work from", None))
        self.pbSelAlbum.setText(_translate("Analyze", "Select Album", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Analyze = QtGui.QMainWindow()
    ui = Ui_Analyze()
    ui.setupUi(Analyze)
    Analyze.show()
    sys.exit(app.exec_())

