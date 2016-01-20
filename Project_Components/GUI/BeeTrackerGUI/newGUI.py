import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class Window(QtGui.QMainWindow):
    # sets up a window
    def __init__(self):
        super(Window, self).__init__()
        # super returns parent obj (QMainWindow obj)
        self.setGeometry(50,100,800,500)
        #           start x, y, h, w
        self.setWindowTitle("Bee Tracking Application")
        self.setWindowIcon(QtGui.QIcon("bee.jpg"))

        # menu item
        extractAction = QtGui.QAction("&Menu Item", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.holder)

        self.statusBar() # bottom left hand corner when hover over menu action

        # menu
        mainMenu = self.menuBar()

        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)


        self.home()

        # sets up stuff on a particular window

    def home(self):
        bExit = QtGui.QPushButton("Exit", self)
        bExit.clicked.connect(self.close_application)
                                # if self.close_application() <- when you load into mem it will close every time
        bExit.resize(bExit.sizeHint())
        bExit.move(740,50)

        # toolbar - page specific
                                                    # icon, hover text, self
        extractAction = QtGui.QAction(QtGui.QIcon('bee.jpg'), 'Track bee', self)
        extractAction.triggered.connect(self.holder)

        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)

        checkBox = QtGui.QCheckBox("Enlarge Window ", self)
        checkBox.resize(checkBox.sizeHint())
        checkBox.move(200,50)
        checkBox.stateChanged.connect(self.enlarge_window)

        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(200,80,250,20)

        self.btn = QtGui.QPushButton("PseudoDL", self)
        self.btn.move(400,240)
        self.btn.clicked.connect(self.download)

        self.show()


    def close_application(self):

        choice = QtGui.QMessageBox.question(self, 'You are leaving',
                                            "Are you sure?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No )
        if choice == QtGui.QMessageBox.Yes:                 # qt yes | <- means either/or qt no
            print 'Goodbye'
            sys.exit()
        else:
            pass

    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(0,-150,1400,900)
        else:
            self.setGeometry(50,50,800,500)


    def holder(self):
        print 'this is a holder'

    def download(self):
        self.completed = 0
        

'''
The difference is, that sys.argv parameters are given before the program is running (while starting it):

python testcode.py arg1 arg2 arg3 arg4 and

http://stackoverflow.com/questions/9455148/what-does-sys-argv-mean
https://docs.python.org/2/library/sys.html
'''
def main():
    app = QtGui.QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
