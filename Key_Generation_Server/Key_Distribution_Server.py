import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 12346))
server_socket.listen(5)

while True:
    print("Waiting for a connection...")
    connection, client_address = server_socket.accept()
    print("Connected to", client_address)

    print("Sending Key to Requesting Client")

    # Send the OTP to the requesting client
    connection.send("OTP VALUE".encode('ascii'))