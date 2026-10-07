# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 21:23:13 2026

@author: kec994
"""

import socket
from mir250ctrl import request_data

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 5000))

data = request_data(sock)

x = data["x"]
y = data["y"]

print("Number of points:", data["num_points"])
print("x:", x)
print("y:", y)

sock.close()