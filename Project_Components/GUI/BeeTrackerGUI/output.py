# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'capture.ui'
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

class Ui_Capture(object):
    def setupUi(self, Capture):
        Capture.setObjectName(_fromUtf8("Capture"))
        Capture.resize(663, 441)
        self.centralWidget = QtGui.QWidget(Capture)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.pbCtrlP = QtGui.QPushButton(self.centralWidget)
        self.pbCtrlP.setGeometry(QtCore.QRect(20, 40, 113, 32))
        self.pbCtrlP.setObjectName(_fromUtf8("pbCtrlP"))
        self.pbRec = QtGui.QPushButton(self.centralWidget)
        self.pbRec.setGeometry(QtCore.QRect(20, 140, 113, 32))
        self.pbRec.setObjectName(_fromUtf8("pbRec"))
        self.spbSecs = QtGui.QSpinBox(self.centralWidget)
        self.spbSecs.setGeometry(QtCore.QRect(290, 140, 48, 24))
        self.spbSecs.setMinimum(1)
        self.spbSecs.setMaximum(300)
        self.spbSecs.setProperty("value", 30)
        self.spbSecs.setObjectName(_fromUtf8("spbSecs"))
        self.lbSecs = QtGui.QLabel(self.centralWidget)
        self.lbSecs.setGeometry(QtCore.QRect(220, 140, 59, 16))
        self.lbSecs.setObjectName(_fromUtf8("lbSecs"))
        self.lbFPS = QtGui.QLabel(self.centralWidget)
        self.lbFPS.setGeometry(QtCore.QRect(390, 140, 59, 16))
        self.lbFPS.setObjectName(_fromUtf8("lbFPS"))
        self.spbFPS = QtGui.QSpinBox(self.centralWidget)
        self.spbFPS.setGeometry(QtCore.QRect(440, 140, 48, 24))
        self.spbFPS.setMinimum(1)
        self.spbFPS.setMaximum(200)
        self.spbFPS.setProperty("value", 100)
        self.spbFPS.setObjectName(_fromUtf8("spbFPS"))
        self.cbMkDefault = QtGui.QCheckBox(self.centralWidget)
        self.cbMkDefault.setGeometry(QtCore.QRect(520, 140, 111, 21))
        self.cbMkDefault.setObjectName(_fromUtf8("cbMkDefault"))
        Capture.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(Capture)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 663, 22))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuApplication = QtGui.QMenu(self.menuBar)
        self.menuApplication.setObjectName(_fromUtf8("menuApplication"))
        Capture.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(Capture)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        Capture.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(Capture)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        Capture.setStatusBar(self.statusBar)
        self.actionCapture = QtGui.QAction(Capture)
        self.actionCapture.setObjectName(_fromUtf8("actionCapture"))
        self.actionAnalyze = QtGui.QAction(Capture)
        self.actionAnalyze.setObjectName(_fromUtf8("actionAnalyze"))
        self.actionAboutsasda = QtGui.QAction(Capture)
        self.actionAboutsasda.setObjectName(_fromUtf8("actionAboutsasda"))
        self.actionExitasdsad = QtGui.QAction(Capture)
        self.actionExitasdsad.setCheckable(True)
        self.actionExitasdsad.setShortcut(_fromUtf8(""))
        self.actionExitasdsad.setObjectName(_fromUtf8("actionExitasdsad"))
        self.actionTesr = QtGui.QAction(Capture)
        self.actionTesr.setObjectName(_fromUtf8("actionTesr"))
        self.actionAbout = QtGui.QAction(Capture)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionExit = QtGui.QAction(Capture)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuApplication.addAction(self.actionCapture)
        self.menuApplication.addAction(self.actionAnalyze)
        self.menuApplication.addAction(self.actionAbout)
        self.menuApplication.addAction(self.actionExit)
        self.menuBar.addAction(self.menuApplication.menuAction())

        self.retranslateUi(Capture)
        QtCore.QMetaObject.connectSlotsByName(Capture)

    def retranslateUi(self, Capture):
        Capture.setWindowTitle(_translate("Capture", "Capture", None))
        self.pbCtrlP.setStatusTip(_translate("Capture", "Go to Leap Motion Control Panel", None))
        self.pbCtrlP.setText(_translate("Capture", "Control Panel", None))
        self.pbRec.setStatusTip(_translate("Capture", "Record from the Leap Motion", None))
        self.pbRec.setText(_translate("Capture", "Record", None))
        self.spbSecs.setStatusTip(_translate("Capture", "Seconds to record for", None))
        self.lbSecs.setText(_translate("Capture", "Seconds:", None))
        self.lbFPS.setText(_translate("Capture", "FPS:", None))
        self.spbFPS.setStatusTip(_translate("Capture", "Frames per second", None))
        self.cbMkDefault.setStatusTip(_translate("Capture", "Make the current seconds & FPS settings the default", None))
        self.cbMkDefault.setText(_translate("Capture", "Make default", None))
        self.menuApplication.setTitle(_translate("Capture", "Application", None))
        self.actionCapture.setText(_translate("Capture", "Capture", None))
        self.actionCapture.setStatusTip(_translate("Capture", "Go to Capture window", None))
        self.actionCapture.setShortcut(_translate("Capture", "Shift+C", None))
        self.actionAnalyze.setText(_translate("Capture", "Analyze", None))
        self.actionAnalyze.setStatusTip(_translate("Capture", "Go to Analyze window", None))
        self.actionAnalyze.setShortcut(_translate("Capture", "Shift+A", None))
        self.actionAboutsasda.setText(_translate("Capture", "About", None))
        self.actionAboutsasda.setStatusTip(_translate("Capture", "About the application", None))
        self.actionExitasdsad.setText(_translate("Capture", "Exit", None))
        self.actionExitasdsad.setStatusTip(_translate("Capture", "Exit application", None))
        self.actionTesr.setText(_translate("Capture", "tesr", None))
        self.actionAbout.setText(_translate("Capture", "About", None))
        self.actionExit.setText(_translate("Capture", "Exit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Capture = QtGui.QMainWindow()
    ui = Ui_Capture()
    ui.setupUi(Capture)
    Capture.show()
    sys.exit(app.exec_())

