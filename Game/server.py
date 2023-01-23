## library ##
import socket
import random
import time

PcName = socket.gethostname()
ip = socket.gethostbyname(PcName)
port = 8050
addr = (ip , port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind(addr)
client.listen()

number = random.randint(1, 100)
print(number)
while True:

    client_socket, client_address = client.accept()

    while True:

        data = client_socket.recv(1024)

        if not data:
            break
        time.sleep(3)

        guess = int(data.decode())

        if guess == number:
            client_socket.send("Correct!".encode())
            
            break
        elif guess < number:
            client_socket.send("Too low!".encode())
        else:
            client_socket.send("Too high!".encode())

client.close()