import socket

s= socket.socket()
print("socket created")
s.bind(("localhost",9999))

s.listen(3)
print("waiting for the connection")

while True:
    c,addr=  s.accept()
    name=c.recv(1024).decode()
    print("coonected with",addr,name)
    c.send(bytes("welcome to my server","utf8"))
    c.close()
