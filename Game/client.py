## library ##
import socket
import random

ip = '0.0.0.0' ## Server IP Here ##
port = 8050
addr = (ip , port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)

while True:

    guess = input("Enter a guess: ")

    client.send(guess.encode())

    data = client.recv(1024)

    if data.decode() == "Correct!":
        print("You guessed it!")
        break
    else:
        print(data.decode())

client.close()