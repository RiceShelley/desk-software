#!/usr/bin/python3
import socket
import time
import random
from PIL import Image

def set_color(r, g, b):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('192.168.1.28', 21))
    sock.recv(100).decode()
    sock.send((str(r) + "/" + str(g) + "/" + str(b) + "\0").encode());
    sock.close()

rgb = Image.open('rgb.jpg', 'r')
pix = list(rgb.getdata())

while (True):
    for j in range(0, 1282):
        i = j * 5
        set_color(pix[i][0], pix[i][1], pix[i][2])
        time.sleep(.5);
