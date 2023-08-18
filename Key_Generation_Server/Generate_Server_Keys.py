import rsa


def generate_server_keys():
    # Generate RSA key pair
    public_key, private_key = rsa.newkeys(2048)
    print(public_key)
    print(private_key)

    with open('public_Key_Server.pem', 'wb') as p:
        p.write(public_key.save_pkcs1('PEM'))

    with open('private_Key_Server.pem', 'wb') as p:
        p.write(private_key.save_pkcs1('PEM'))


generate_server_keys()
