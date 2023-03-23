import json
from .routes import ClientRoutes


client_routes = ClientRoutes()

SIZE = 1024
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"


def parse_client_data(json_string):
    """
    Parse the json string to the server specific request parameters
    :param json_string: string json
    :return: connected_status, route to be used, client data
    """
    client_data = json.loads(json_string)
    route_name = client_data.get('route')
    if route_name:
        route = client_routes.__getattribute__(route_name)
    else:
        route = None
    data = client_data.get("data", {})
    return route, route_name, data


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    auth = False
    username = None
    password = None
    while connected:
        client_msg = conn.recv(SIZE).decode(FORMAT)
        route, route_name, data = parse_client_data(client_msg)
        if route_name == 'login':
            response, auth, username, password = route(**data)
        elif (not auth) or (not username) or (not password):
            response = json.dumps({'status': 401})  # login required to continue
        else:
            response = route(email=username, **data)
        print(f"[{addr}] {data}")
        msg = str(response)
        conn.send(msg.encode(FORMAT))

    conn.close()
