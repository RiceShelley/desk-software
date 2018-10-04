#!/usr/bin/python3
import socket
import time

def set_color(r, g, b):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('192.168.1.28', 21))
    sock.recv(100).decode()
    sock.send((str(r) + "/" + str(g) + "/" + str(b) + "\0").encode());
    sock.close()

set_color(250, 250, 250)
