import socket

c= socket.socket()
c.connect(("localhost",9999))

name=input("enter the name")
c.send(bytes(name,"utf8"))
print(c.recv(1024).decode())