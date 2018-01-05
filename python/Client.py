#!/usr/bin/env python
import socket               
import ssl
import threading

HOST = socket.gethostname() 
PORT = 12345
BUFSIZE = 1024
ADDR = (HOST, PORT)

s = socket.socket()         
ssl_sock = ssl.wrap_socket(s, ca_certs = "cert.pem",
        cert_reqs = ssl.CERT_REQUIRED)
ssl_sock.connect(ADDR)

class Client(threading.Thread):
    def __init__(self, window):
        super(Client, self).__init__()
        self.window = window
        self.eevent()

    def run(self):
        self.do_something()

    def do_something(self):
        while True:  
            data = ssl_sock.recv(BUFSIZE)  
            if not data:  
                break  
            print data  
            self.window.displayBox.append(data)
        ssl_sock.close()  

    def sendMessage(self):
        data = self.window.inputBox.toPlainText()
        if not data:
            return
        ssl_sock.send(data)
        self.window.displayBox.palette().setColor(QPalette::Active,
                QPalette::Base, Qt::red)
        self.window.displayBox.append(data)
        self.window.inputBox.setText('')

    def eevent(self):
        self.window.pushButton.clicked.connect(self.sendMessage)
