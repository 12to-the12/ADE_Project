import socket
connection = socket.create_connection(('helloworldbook3.com', 80))
connection.sendall('GET /data/message.txt HTTP/1.0\r\n'.encode('utf-8'))
connection.sendall(b'Host: helloworldbook3.com\r\n\r\n')
response = bytes()
while True:
    new_data = connection.recv(4096)
    if not new_data:
        break
    response += new_data
print(response.decode('utf-8'))
