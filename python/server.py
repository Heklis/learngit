#!/usr/bin/env python

import socket, ssl, time

HOST = socket.gethostname()
PORT = 12345
BUFSIZE = 1024
ADDR = (HOST, PORT)

s = socket.socket()
s.bind(ADDR)
s.listen(5)

def do_something(connstream, data):
    backdata = raw_input('>')
    return backdata

def deal_with_client(connstream):
    data = connstream.recv(BUFSIZE)
    print data
    
    while data:
        backdata = do_something(connstream, data)
        if not backdata:
            break
        connstream.send(backdata)
        data = connstream.recv(BUFSIZE)
        print data

while True:
    newsocket, fromaddr = s.accept()
    print "socket accept one client from ",fromaddr
    connstream = ssl.wrap_socket(newsocket, 
            "key.pem",
            "cert.pem",
            server_side = True,
            ssl_version = ssl.PROTOCOL_TLSv1)
    try:
        deal_with_client(connstream)
    finally:
        connstream.shutdown(socket.SHUT_RDWR)
        connstream.close()
