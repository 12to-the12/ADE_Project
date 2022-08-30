import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 12123))
s.listen(1)
connection, from_address = s.accept()
connection.sendall(b"Hi there! Welcome to my server!\r\nWhat's your name? ")
name = bytes()
while True:
    next_character = connection.recv(1)
    if next_character in [b'', b'\r', b'\n']:
        break
    else:
        name += next_character
connection.sendall(b"Nice to meet you, " + name + b"! Goodbye for now!\r\n")
connection.shutdown(socket.SHUT_WR)
connection.close()
s.close()
