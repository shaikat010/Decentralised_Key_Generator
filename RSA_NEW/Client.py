import rsa
import socket

# Generate RSA key pair
public_key, private_key = rsa.newkeys(2048)
print(public_key)
print(private_key)

# Serialize the public key
public_key_bytes = public_key.save_pkcs1(format='PEM')

# Connect to the server
server_ip = '127.0.0.1'
server_port = 12345
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_ip, server_port))

print("Connection Made Successfully!")

# Send the public key bytes
sock.sendall(public_key_bytes)

# Close the socket
sock.close()