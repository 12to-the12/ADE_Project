import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 12123))

s.listen(1)
connection, from_address = s.accept()

connection.sendall(b"Hi there--oops, sorry, gotta go!\r\n")

connection.shutdown(socket.SHUT_WR)
connection.close()
s.close()


