
import sys
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




class Ui_Generic(QtGui.QMainWindow):
    # sets up the generic window
    def __init__(self):
        super(Ui_Generic, self).__init__()                      # super returns parent obj (QMainWindow obj)
        self.setGeometry(50,100,850,600)                        #           start x, y, w, h
        self.setWindowTitle("Bee Tracking Application")
    #    self.setWindowIcon(QtGui.QIcon("bee.jpg"))

        # menu items
        actionCapture = QtGui.QAction("&Capture", self)
        actionCapture.setShortcut("Shift+C")
        actionCapture.setStatusTip("Go to the Capture window")
        actionCapture.triggered.connect(self.holder)

        actionAnalyze = QtGui.QAction("&Analyze", self)
        actionAnalyze.setShortcut("Shift+A")
        actionAnalyze.setStatusTip("Go to the Analyze window")
        actionAnalyze.triggered.connect(self.holder)

        actionInformation = QtGui.QAction("&Information", self)
        actionInformation.setStatusTip("About the application")
        actionInformation.triggered.connect(self.holder)

        actionSuspendApp = QtGui.QAction("Suspend application", self)
        actionSuspendApp.setStatusTip("Exit application")
        actionSuspendApp.setShortcut("Ctrl+Q")
        actionSuspendApp.triggered.connect(self.holder)


        mainMenu = self.menuBar()
        applicationMenu = mainMenu.addMenu("&Application")
        # add actions to menu
        applicationMenu.addAction(actionAnalyze)
        applicationMenu.addAction(actionCapture)
        applicationMenu.addAction(actionSuspendApp)
        applicationMenu.addAction(actionInformation)
        # http://stackoverflow.com/questions/11702621/why-doesnt-menu-get-added rip 3 hours

        self.statusBar() # bottom left hand corner when hover over menu action

        # self.show() # dont need this because this is acting as an abstract class

    def holder(self):
        print 'holder'

class Ui_Capture(Ui_Generic):
    def __init__(self, Cap):
        super(Ui_Capture, self).__init__()

        #pb = QtGui.QPushButton("hi", self)
        #pb.move(100,10)

        #self.label = QtGui.QLabel("text", self)

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
        self.show()


    def retranslateUi(self, Cap):
        Cap.setWindowTitle( _translate("Cap", "MainWindow", None))
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

       # self.show()

def main():
    app = QtGui.QApplication(sys.argv)
#    gui = Ui_Capture(QtGui.QMainWindow())
    gui = Ui_Capture(QtGui.QMainWindow())
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()