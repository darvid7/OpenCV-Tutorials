from PyQt4 import QtCore, QtGui

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # set up stacked widget - only 1 seen @ a time
        self.central_widget = QtGui.QStackedWidget()
        self.setCentralWidget(self.central_widget)
        # create LoginWidget - shows login text
        login_widget = LoginWidget(self)
        # pressed call log in
        login_widget.button.clicked.connect(self.login)
        self.central_widget.addWidget(login_widget)

        self.dialogTextBrowser = MyDialog(self)



    # shows 1 widget
    def login(self):
        self.hide()
        self.dialogTextBrowser.exec_()

        print 'h'
        self.show()
        '''
        # set widget to Logged
        logged_in_widget = LoggedWidget(self)
        # adds logged widget
        self.central_widget.addWidget(logged_in_widget)
        # set it to be the one show in the stack
        self.central_widget.setCurrentWidget(logged_in_widget)
        '''

class MyDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)

        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)

        self.textBrowser = QtGui.QTextBrowser(self)
        self.textBrowser.append("This is a QTextBrowser!")

        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.addWidget(self.textBrowser)
        self.verticalLayout.addWidget(self.buttonBox)

        self.pushb = QtGui.QPushButton("pushb", self)
        self.pushb.clicked.connect(self.changewindow)

    def changewindow(self):
        self.hide()
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
        app.show()


                                #

class LoginWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        print 'login widget used'
        super(LoginWidget, self).__init__(parent)
        layout = QtGui.QHBoxLayout()
        self.button = QtGui.QPushButton('Login')
        layout.addWidget(self.button)
        self.setLayout(layout)
        # you might want to do self.button.click.connect(self.parent().login) here


class LoggedWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        print 'logged on widget used'
        super(LoggedWidget, self).__init__(parent)
        layout = QtGui.QHBoxLayout()
        self.label = QtGui.QLabel('logged in!')
        layout.addWidget(self.label)
        self.setLayout(layout)
     #   self.changewindow()


class guiwindow1(QtGui.QMainWindow):
    def __init__(self):
        super(guiwindow1, self).__init__()


        self.setGeometry(50,100,800,500)
        #           start x, y, h, w
        self.setWindowTitle("Bee Tracking Application")
        self.setWindowIcon(QtGui.QIcon("bee.jpg"))

        self.label = QtGui.QLabel('text')
       # self.show()



if __name__ == '__main__':
    app = QtGui.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()