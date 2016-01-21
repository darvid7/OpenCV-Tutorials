
import sys
import os
from PyQt4 import QtCore, QtGui


class Generic_UI(QtGui.QMainWindow):
    # sets up the generic window
    def __init__(self):
        super(Generic_UI, self).__init__()                      # super returns parent obj (QMainWindow obj)
        self.setGeometry(50,100,850,600)                        #           start x, y, w, h
        self.setWindowTitle("Bee Tracking Application")

    # set new icon soon
    #    self.setWindowIcon(QtGui.QIcon("bee.jpg"))

        # menu items
        actionCapture = QtGui.QAction("&Capture", self)
        actionCapture.setShortcut("Shift+C")
        actionCapture.setStatusTip("Go to the Capture window")
        actionCapture.triggered.connect(self.on_capture)

        actionAnalyze = QtGui.QAction("&Analyze", self)
        actionAnalyze.setShortcut("Shift+A")
        actionAnalyze.setStatusTip("Go to the Analyze window")
        actionAnalyze.triggered.connect(self.on_analyze)

        actionInformation = QtGui.QAction("&Information", self)
        actionInformation.setStatusTip("About the application")
        actionInformation.triggered.connect(self.holder)

        actionSuspendApp = QtGui.QAction("Suspend application", self)
        actionSuspendApp.setStatusTip("Exit application")
        actionSuspendApp.setShortcut("Ctrl+Q")
        actionSuspendApp.triggered.connect(self.on_suspendApp)

        actionDefaultSize = QtGui.QAction("Revert to default size", self)
        actionDefaultSize.setStatusTip("Set window size to default")
        actionDefaultSize.setShortcut("Shift+S")
        actionDefaultSize.triggered.connect(self.on_defaultSize)


        mainMenu = self.menuBar()
        applicationMenu = mainMenu.addMenu("&Application")
        # add actions to menu
        applicationMenu.addAction(actionAnalyze)
        applicationMenu.addAction(actionCapture)
        applicationMenu.addAction(actionSuspendApp)
        applicationMenu.addAction(actionInformation)
        applicationMenu.addAction(actionDefaultSize)
        # http://stackoverflow.com/questions/11702621/why-doesnt-menu-get-added rip 3 hours

        self.statusBar() # bottom left hand corner when hover over menu action

        # self.show() # dont need this because this is acting as an abstract class


    def show_window(self):
        self.show()

    def on_defaultSize(self):
        self.setGeometry(50,100,850,600)
    def on_analyze(self):
        global curWindow
        curWindow = 2
        print 'on analyze'
        self.windowController()

    def on_capture(self):
        global curWindow
        curWindow = 1
        print 'on capture'
        self.windowController()

    def windowController(self):
        print '-------called------'
        settings = self.geometry()
        print "current window: " + str(curWindow)
        print settings
        global windows
        for i in windows:
            if i.window != curWindow:
                print i.window
                i.hide()
            else:
                print 'chosen'
                print i.window
                chosenWindow = i

        chosenWindow.setGeometry(settings)
        chosenWindow.show()

    def on_suspendApp(self):
        choice = QtGui.QMessageBox.question(self, 'You are leaving',
                                            "Are you sure?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No )
        if choice == QtGui.QMessageBox.Yes:                 # qt yes | <- means either/or qt no
            print 'Goodbye'
            sys.exit()
        else:
            pass

    def on_information(self):
        pass

    def holder(self):
        print 'holder function'

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


class Analyze_UI(Generic_UI):
    def __init__(self):
        super(Analyze_UI, self).__init__()
        self.window = 2

        # image label
        self.lbImage = QtGui.QLabel("",self)
        self.lbImage.setGeometry(QtCore.QRect(40, 60, 441, 311))

        # pyqt browse picker
        self.lbImage.setPixmap(QtGui.QPixmap("../PycharmProjects/OpenCV-Project/OpenCV/Tutorials_Python/Resources/bee.jpg"))
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

class GenericThread(QtCore.QThread):
    def __init__(self, function, *args, **kwargs):
        QtCore.QThread.__init__(self)
        self.function = function
        self.args = args
        self.kwargs = kwargs

    def __del__(self):
        self.wait()

    def run(self):
        self.function(*self.args,**self.kwargs)
        return

def main():

    global curWindow
    curWindow = 1

    app = QtGui.QApplication(sys.argv)
#    gui = Ui_Capture(QtGui.QMainWindow())
    captureWindow = Capture_UI()
    analyzeWindow = Analyze_UI()

    global windows
    windows = [captureWindow, analyzeWindow]

    captureWindow.show_window()

    print captureWindow.geometry()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()