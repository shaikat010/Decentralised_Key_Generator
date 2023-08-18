import rsa
import socket
import RSA_encrypt_decrypt


# Connect to the server
server_ip = '127.0.0.1'
server_port = 12345
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_ip, server_port))

# Receive the public key bytes
public_key_bytes_received = sock.recv(4096)

# Deserialize the public key
received_public_key = rsa.PublicKey.load_pkcs1(public_key_bytes_received)

print("Received Public Key:", received_public_key)
print(type(received_public_key))

with open('public_Key_Server.pem', 'wb') as p:
    p.write(received_public_key.save_pkcs1('PEM'))

message = input("Enter the Secret Phrase: ")
message = str(message)

encrypted_data = RSA_encrypt_decrypt.encrypt(message,received_public_key)
print(encrypted_data)

sock.send(encrypted_data)

# Close the socket
sock.close()

