import socket
IP = "localhost"
PORT = 5567
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = 'utf-8'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


class User:
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password


user = User()
