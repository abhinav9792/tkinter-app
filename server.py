import json
import socket
import threading
import mysql.connector as mysql
import os


db = mysql.connect(
    host='localhost',
    user='root',
    password=os.environ.get("SQL_PASSWORD", ""),
    database='CST1510dbs'
)


IP = "localhost"
PORT = 5566
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"


class ClientRoutes:
    def login(self, *args, **kwargs):
        cur = db.cursor()
        cur.execute(
            'SELECT * FROM user WHERE email=%s and password=%s',
            (kwargs.get('email'), kwargs.get('password'))
        )
        data = cur.fetchone()
        if data:
            return json.dumps({'status': True})
        else:
            return json.dumps({'status': False})


client_routes = ClientRoutes()


def parse_client_data(json_string):
    """
    Parse the json string to the server specific request parameters
    :param json_string: string json
    :return: connected_status, route to be used, client data
    """
    client_data = json.loads(json_string)
    route = client_data.get('route')
    if route:
        route = client_routes.__getattribute__("login")
    data = client_data.get("data", {})
    return route, data


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    auth = False
    while connected:
        client_msg = conn.recv(SIZE).decode(FORMAT)
        route, data = parse_client_data(client_msg)
        response = route(**data)
        print(f"[{addr}] {data}")
        msg = str(response)
        conn.send(msg.encode(FORMAT))

    conn.close()


def main():
    print("Starting the server...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server is listening on {IP}:{PORT}")

    while True:
        conn, addr = server.accept()  # loop waits for the client request

        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


if __name__ == '__main__':
    main()
