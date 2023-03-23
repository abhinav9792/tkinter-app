import json
import socket
# from mysql.connector import

IP = "localhost"
PORT = 5566
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = 'utf-8'


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")

    connected = True
    while connected:
        msg = input(">>> ")
        username = input("Username: ")
        password = input("Password: ")
        client.send(json.dumps({'route': "login", 'data': {
            'email': username, 'password': password
        }}).encode('utf-8'))

        if not msg:
            connected = False
        else:
            res = client.recv(SIZE).decode(FORMAT)
            print(res)
            res_json = json.loads(res)
            print(f"[SERVER] {res_json}")
            if res_json.get('status'):
                print("Logged ID!")
            else:
                print("Unable to login")


if __name__ == '__main__':
    main()
