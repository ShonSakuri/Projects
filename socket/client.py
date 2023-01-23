## library ##
import socket

ip = socket.gethostname()
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(ip)
ADDR = (SERVER , PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!disconnect"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(message):
    msg = message.encode(FORMAT)
    msg_length = len(msg)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(msg)
    print(client.recv(2048).decode(FORMAT))
send("Hello World!")
input()
send("Hello Everyone!")
input()
send("Hello Shon!")

send(DISCONNECT_MESSAGE)