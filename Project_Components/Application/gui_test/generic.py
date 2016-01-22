
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
        actionCapture.triggered.connect(self.on_gen)

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

    def on_gen(self):
        global curWindow
        curWindow = 1
        print 'on gen'
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