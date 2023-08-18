# Use pip install rsa if you do to have rsa in your local pc.
import rsa


def generateKeys():
    (publicKey, privateKey) = rsa.newkeys(1024)
    with open('publicKey.pem', 'wb') as p:
        p.write(publicKey.save_pkcs1('PEM'))
    with open('privateKey.pem', 'wb') as p:
        p.write(privateKey.save_pkcs1('PEM'))


def loadKeys():
    with open('public_Key_Server.pem', 'rb') as p:
        publicKey = rsa.PublicKey.load_pkcs1(p.read())
    with open('private_Key_Server.pem', 'rb') as p:
        privateKey = rsa.PrivateKey.load_pkcs1(p.read())
    return privateKey, publicKey


def encrypt(message, key):
    return rsa.encrypt(message.encode('ascii'), key)


def decrypt(ciphertext, key):
    try:
        return rsa.decrypt(ciphertext, key).decode('ascii')
    except:
        return False


# print(loadKeys())
# privateKey, publicKey  = loadKeys()
# print(privateKey)
# print(publicKey)
# print(type(privateKey))
# print(type(publicKey))