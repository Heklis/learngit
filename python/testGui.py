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
        self.initEvent()
    
    def startClient(self):
        self.clientThread = Client.Client(self)
        self.clientThread.setDaemon(True)
        self.clientThread.start()

    def initEvent(self):
        #self.pushButton.clicked.connect(self.clientThread.sendMessage)
        self.connect(self.pushButton, QtCore.SIGNAL("clicked()"),
                self.clientThread.sendMessage)
        #self.inputBox.returnPressed.connect(self.clientThread.sendMessage)
        self.connect(self.inputBox, QtCore.SIGNAL("returnPressed()"),
                self.clientThread.sendMessage)
        self.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"),
                self.sendFile)

    def keyPressEvent(self, e):
        print e.key()

    def sendFile(self):
        filename = QtGui.QFileDialog.getOpenFileName(self,
                "select file",
                "./")
        self.clientThread.sendFile(filename) 

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
