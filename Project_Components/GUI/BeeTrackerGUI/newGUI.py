import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
import time

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

        # editor
        openEditor = QtGui.QAction("&Editor", self)
        openEditor.setShortcut("Ctrl+E")
        openEditor.setStatusTip("Open Editor")
        openEditor.triggered.connect(self.editor)
        # new editor menu
        editorMenu = mainMenu.addMenu("&Editor")
        editorMenu.addAction(openEditor)

        openFile = QtGui.QAction("&Open File", self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip("Open File")
        openFile.triggered.connect(self.open_file)

        # add to the file menu
        fileMenu.addAction(openFile)

        saveFile = QtGui.QAction("&Save File", self)
        saveFile.setShortcut("Ctrl+S")
        saveFile.setStatusTip("Save File")
        saveFile.triggered.connect(self.save_file)

        fileMenu.addAction(saveFile)

        fileMenu.show()


        #####
           # menu items
        actionCapture = QtGui.QAction("&Capture", self)
        actionCapture.setShortcut("Shift+C")
        actionCapture.setStatusTip("Go to the Capture window")
        actionCapture.triggered.connect(self.holder)

        actionAnalyze = QtGui.QAction("&Analyze", self)
        actionAnalyze.setShortcut("Shift+A")
        actionAnalyze.setStatusTip("Go to the Analyze window")
        actionAnalyze.triggered.connect(self.holder)

        actionInfoMe = QtGui.QAction("&Info Application", self)
        actionInfoMe.setStatusTip("Info the application")
        actionInfoMe.triggered.connect(self.holder)

        sSuspendA = QtGui.QAction("&Suspend Application", self)
        sSuspendA.setStatusTip("Suspend application")
        sSuspendA.setShortcut("Ctrl+Q")
        sSuspendA.triggered.connect(self.holder)

        actionTest = QtGui.QAction("&Text", self)


        fileMenu.addAction(sSuspendA)
        fileMenu.addAction(actionInfoMe)
        fileMenu.addAction(actionAnalyze)
        fileMenu.addAction(actionCapture)
        fileMenu.addAction(actionTest)
        ####

        self.home()

        # sets up stuff on a particular window


    def home(self):
        bSuspend = QtGui.QPushButton("Suspend", self)
        bSuspend.clicked.connect(self.close_application)
                                # if self.close_application() <- when you load into mem it will close every time
        bSuspend.resize(bSuspend.sizeHint())
        bSuspend.move(740,50)

        # toolbar - page specific
                                                    # icon, hover text, self
        extractAction = QtGui.QAction(QtGui.QIcon('bee.jpg'), 'Track bee', self)
        extractAction.triggered.connect(self.holder)

        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)

        # check box
        checkBox = QtGui.QCheckBox("Enlarge Window ", self)
        checkBox.resize(checkBox.sizeHint())
        checkBox.move(200,50)
        checkBox.stateChanged.connect(self.enlarge_window)

        # progress bar
        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(200,80,250,20)

        self.btn = QtGui.QPushButton("PseudoDL", self)
        self.btn.move(400,240)
        self.btn.clicked.connect(self.download)

        # drop down button
        print (self.style().objectName()) # prints your default style
        self.styleChoice = QtGui.QLabel("macintosh", self)

        comboBox = QtGui.QComboBox(self) # drop down
        comboBox.addItem("motif")
        comboBox.addItem("Windows")
        comboBox.addItem("cde")
        comboBox.addItem("Plastique")
        comboBox.addItem("Cleanlooks")
        comboBox.addItem("aqua")
        comboBox.addItem("macintosh")


        comboBox.move(300,400)
        self.styleChoice.move(100,250)
        comboBox.activated[str].connect(self.style_choice) # show current value

        # fonts
        fontChoice = QtGui.QAction("Font", self)
        fontChoice.triggered.connect(self.font_choice)
        self.toolBar = self.addToolBar("Font") # new toolbar, remove this to make it part of old toolbar
        self.toolBar.addAction(fontChoice)

        # colours
        colour = QtGui.QColor(0,0,0) # starting  colour = black

        fontColour = QtGui.QAction("Font bg Colour", self)
        fontColour.triggered.connect(self.colour_picker)

        self.toolBar.addAction(fontColour)

        # calendar
        cal = QtGui.QCalendarWidget(self)
        cal.move(500,200)
        cal.resize(200,200)




        self.show()
        #time.sleep(5)
        #self.hide()
        self.test()

    def test(self):
        pb = QtGui.QPushButton("hi", self)
        pb.show()
        #self.hide()

    def colour_picker(self):
        colour = QtGui.QColorDialog.getColor()
        # style sheet allows customization of things in appliaction
        self.styleChoice.setStyleSheet("QWidget {background-color: %s}" % colour.name())

    def open_file(self):
        name = QtGui.QFileDialog.getOpenFileName(self, "Open File")
        file = open(name, 'rw') # open with read

        self.editor()

        with file:
            text = file.read()
            self.textEdit.setText(text)

    def save_file(self):
        try:
            name = QtGui.QFileDialog.getSaveFileName(self, "Save File")
            file = open(name, 'w') # write
    # note file not self as only want to ref in this method, not the whole class
            text = self.textEdit.toPlainText()
            file.write(text)
            file.close()
        except IOError:
            print 'file unsaved, try again'


    def style_choice(self, text):
    # remember from 1008 self.var is accessible from all methods i of a class i believe
    # var isnt
        self.styleChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))

    def editor(self):
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)

    def font_choice(self, font):
        font, valid = QtGui.QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)


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
        while self.completed < 100:
            #print 'h'
            self.completed += 0.0001
            self.progress.setValue(self.completed)
            # use this line to show the progress
            QtGui.QApplication.processEvents()
            #print self.completed
            # set the value of the progress bar to the completion


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
