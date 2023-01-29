## library ##
import socket
import threading

ip = socket.gethostname()
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(ip)
ADDR = (SERVER , PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!disconnect"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(connection,addr):
    print(f"[New Connection] {addr} connected.")
    
    connected = True
    while connected:
        msg_length = connection.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = connection.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            connection.send("Message received".encode(FORMAT))
    connection.close()

def start():
    server.listen()
    print(f"[Listening] server is listening on {SERVER}")
    while True:
        connection , addr = server.accept()
        thread = threading.Thread(target=handle_client,args=(connection,addr))
        thread.start()
        print(f"[Active Connections] {threading.active_count() - 1}")

print("[Starting] server is starting...")

start()