import time
import socket
import sys
import os

s = socket.socket()
host = "127.0.0.1"
port = 8080
s.connect((host, port))
print("Conectado ao servidor")
command = s.recv(1024)
command = command.decode()
if command == "open":
    print("Comando é:", command)
    s.send("Comando recebido".encode())
    os.system('ls')