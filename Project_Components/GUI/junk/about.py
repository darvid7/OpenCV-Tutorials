# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ab.ui'
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

class Ui_ab(object):
    def setupUi(self, ab):
        ab.setObjectName(_fromUtf8("ab"))
        ab.resize(800, 600)
        self.centralwidget = QtGui.QWidget(ab)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(140, 60, 341, 201))
        self.textEdit.setReadOnly(True)
        self.textEdit.setTabStopWidth(80)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        ab.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(ab)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        ab.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(ab)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        ab.setStatusBar(self.statusbar)

        self.retranslateUi(ab)
        QtCore.QMetaObject.connectSlotsByName(ab)

    def retranslateUi(self, ab):
        ab.setWindowTitle(_translate("ab", "MainWindow", None))
        self.textEdit.setText(_translate("ab", "my text here", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ab = QtGui.QMainWindow()
    ui = Ui_ab()
    ui.setupUi(ab)
    ab.show()
    sys.exit(app.exec_())

