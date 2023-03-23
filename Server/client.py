import json
import socket
# from mysql.connector import

IP = "localhost"
PORT = 5567
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = 'utf-8'


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")

    connected = True
    route = "login"
    while connected:
        msg = input(">>> ")
        username = input("Username: ")
        password = input("Password: ")
        cash = input("Cash: ")
        if route == "login":
            client.send(json.dumps({'route': route, 'data': {
                'email': username, 'password': password, 'cash': cash,
            }}).encode('utf-8'))
        else:
            client.send(json.dumps({'route': route, 'data': {}}).encode('utf-8'))

        if not msg:
            connected = False
        else:
            res = client.recv(SIZE).decode(FORMAT)
            res_json = json.loads(res)
            if route == 'login' and res_json.get('status', False):
                route = 'stock_price'
            print(f"[SERVER] {res_json}")
            if res_json.get('status'):
                print("Logged ID!")
            else:
                print("Unable to login")


if __name__ == '__main__':
    main()
