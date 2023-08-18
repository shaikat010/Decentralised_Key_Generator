import socket
import rsa

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 12345))
server_socket.listen(5)

while True:
    print("Waiting for a connection...")
    connection, client_address = server_socket.accept()
    print("Connected to", client_address)

    # Receive the public key bytes
    public_key_bytes_received = connection.recv(4096)

    # Deserialize the public key
    received_public_key = rsa.PublicKey.load_pkcs1(public_key_bytes_received)

    print("Received Public Key:", received_public_key)
    print(type(received_public_key))

    with open('publicKey.pem', 'wb') as p:
        p.write(received_public_key.save_pkcs1('PEM'))