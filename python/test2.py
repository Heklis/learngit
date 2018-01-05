#!/usr/bin/env python

import sys
from PyQt4 import QtCore, QtGui, uic
import threading
import Client

qtCreatorFile = "/home/heklis/chat.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.startClient()
    
    def startClient(self):
        t = Client.Client(self)
        t.start()

    

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
