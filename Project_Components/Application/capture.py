# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cap.ui'
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

class Ui_Cap(object):
    def setupUi(self, Cap):
        Cap.setObjectName(_fromUtf8("Cap"))
        Cap.resize(800, 600)
        self.centralwidget = QtGui.QWidget(Cap)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lbFPS = QtGui.QLabel(self.centralwidget)
        self.lbFPS.setGeometry(QtCore.QRect(530, 210, 59, 16))
        self.lbFPS.setObjectName(_fromUtf8("lbFPS"))
        self.spbSecs = QtGui.QSpinBox(self.centralwidget)
        self.spbSecs.setGeometry(QtCore.QRect(430, 210, 48, 24))
        self.spbSecs.setMinimum(1)
        self.spbSecs.setMaximum(300)
        self.spbSecs.setProperty("value", 30)
        self.spbSecs.setObjectName(_fromUtf8("spbSecs"))
        self.cbMkDefault = QtGui.QCheckBox(self.centralwidget)
        self.cbMkDefault.setGeometry(QtCore.QRect(660, 210, 111, 21))
        self.cbMkDefault.setObjectName(_fromUtf8("cbMkDefault"))
        self.lbSecs = QtGui.QLabel(self.centralwidget)
        self.lbSecs.setGeometry(QtCore.QRect(360, 210, 59, 16))
        self.lbSecs.setObjectName(_fromUtf8("lbSecs"))
        self.pbRec = QtGui.QPushButton(self.centralwidget)
        self.pbRec.setGeometry(QtCore.QRect(160, 210, 113, 32))
        self.pbRec.setObjectName(_fromUtf8("pbRec"))
        self.pbCtrlP = QtGui.QPushButton(self.centralwidget)
        self.pbCtrlP.setGeometry(QtCore.QRect(160, 110, 113, 32))
        self.pbCtrlP.setObjectName(_fromUtf8("pbCtrlP"))
        self.spbFPS = QtGui.QSpinBox(self.centralwidget)
        self.spbFPS.setGeometry(QtCore.QRect(580, 210, 48, 24))
        self.spbFPS.setMinimum(1)
        self.spbFPS.setMaximum(200)
        self.spbFPS.setProperty("value", 100)
        self.spbFPS.setObjectName(_fromUtf8("spbFPS"))
        Cap.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Cap)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Cap.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Cap)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Cap.setStatusBar(self.statusbar)

        self.retranslateUi(Cap)
        QtCore.QMetaObject.connectSlotsByName(Cap)

    def retranslateUi(self, Cap):
        Cap.setWindowTitle(_translate("Cap", "MainWindow", None))
        self.lbFPS.setText(_translate("Cap", "FPS:", None))
        self.spbSecs.setStatusTip(_translate("Cap", "Seconds to record for", None))
        self.cbMkDefault.setStatusTip(_translate("Cap", "Make the current seconds & FPS settings the default", None))
        self.cbMkDefault.setText(_translate("Cap", "Make default", None))
        self.lbSecs.setText(_translate("Cap", "Seconds:", None))
        self.pbRec.setStatusTip(_translate("Cap", "Record from the Leap Motion", None))
        self.pbRec.setText(_translate("Cap", "Record", None))
        self.pbCtrlP.setStatusTip(_translate("Cap", "Go to Leap Motion Control Panel", None))
        self.pbCtrlP.setText(_translate("Cap", "Control Panel", None))
        self.spbFPS.setStatusTip(_translate("Cap", "Frames per second", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Cap = QtGui.QMainWindow()
    ui = Ui_Cap()
    ui.setupUi(Cap)
    Cap.show()
    sys.exit(app.exec_())

