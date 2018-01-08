#!/usr/bin/env python

import socket               
import ssl
import threading

HOST = socket.gethostname() 
PORT = 12346
BUFSIZE = 1024
ADDR = (HOST, PORT)

s = socket.socket()         
ssl_sock = ssl.wrap_socket(s, ca_certs = "cert.pem",
        cert_reqs = ssl.CERT_REQUIRED)
ssl_sock.connect(ADDR)

class Ftp_client(threading.Thread):
    def __init__(self, window):
        super(Client, self).__init__()
        self.window = window

    def run(self):
        self.do_something()

    def do_something(self):
        while True:  
            data = ssl_sock.recv(BUFSIZE)  
            if not data:  
                break  
            print data  
        ssl_sock.close()  

    if os.path.isfile(filepath):
        fileinfo_size=struct.calcsize('128sl') #定义打包规则
        #定义文件头信息，包含文件名和文件大小
        fhead = struct.pack('128sl',os.path.basename(filepath),os.stat(filepath).st_size)
        s.send(fhead) 
        print 'client filepath: ',filepath
        # with open(filepath,'rb') as fo: 这样发送文件有问题，发送完成后还会发一些东西过去
        fo = open(filepath,'rb')
        while True:
            filedata = fo.read(1024)
            if not filedata:
                break
            s.send(filedata)
        fo.close()
        print 'send over...'
