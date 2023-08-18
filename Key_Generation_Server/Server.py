import socket
import rsa
import Generate_Server_Keys
import RSA_encrypt_decrypt


collected_secret_phrases = []

private_key, public_key = RSA_encrypt_decrypt.loadKeys()

# Serialize the public key and private key
public_key_bytes = public_key.save_pkcs1(format='PEM')
private_key_bytes = private_key.save_pkcs1(format='PEM')

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 12345))
server_socket.listen(5)

while True:
    print("Waiting for a connection...")
    connection, client_address = server_socket.accept()
    print("Connected to", client_address)

    print("Connection Made Successfully!")

    # Send the public key bytes during the initial key exchange phase
    connection.sendall(public_key_bytes)

    received_encrypted_data = connection.recv(4096)
    print("This is the encrypted secret phrase from the : ")
    print(received_encrypted_data)

    decrypted_secret_phrase = RSA_encrypt_decrypt.decrypt(received_encrypted_data,private_key)

    print("This is the decrypted secret phrase from the : ")
    print(decrypted_secret_phrase)

    collected_secret_phrases.append(decrypted_secret_phrase)

    with open("key_store.txt",'a') as file:
        file.write(str(decrypted_secret_phrase) + "\n" )

    connection.close()


