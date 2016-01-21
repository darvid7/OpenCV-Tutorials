
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




class Generic_UI(QtGui.QMainWindow):
    # sets up the generic window
    def __init__(self):
        super(Generic_UI, self).__init__()                      # super returns parent obj (QMainWindow obj)
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
        # control panel push button
        self.pbCtrlP = QtGui.QPushButton("Control Panel", self)
        self.pbCtrlP.setGeometry(QtCore.QRect(160, 110, 113, 32))
        # FPS spinbox
        self.spbFPS = QtGui.QSpinBox(self)
        self.spbFPS.setGeometry(QtCore.QRect(580, 210, 48, 24))
        self.spbFPS.setMinimum(1)
        self.spbFPS.setMaximum(200)
        self.spbFPS.setProperty("value", 100)

        self.statusBar()

        self.show()

class Analyze_UI(Generic_UI):
    def __init__(self):
        super(Capture_UI, self).__init__()
        self.window = 2

        # image label
        self.lbImage = QtGui.QLabel("",self)
        self.lbImage.setGeometry(QtCore.QRect(40, 60, 441, 311))
        self.lbImage.setPixmap(QtGui.QPixmap(_fromUtf8("../PycharmProjects/OpenCV-Project/OpenCV/Tutorials_Python/Resources/bee.jpg")))
        self.lbImage.setWordWrap(False)
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
        # 
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





def main():
    curWindow = 1

    app = QtGui.QApplication(sys.argv)
#    gui = Ui_Capture(QtGui.QMainWindow())
    captureWindow = Capture_UI()
    analyzeWindow = Analyze_UI()

    windows = [captureWindow, analyzeWindow]

    for i in windows:
        if i.window != curWindow:
            i.hide()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()