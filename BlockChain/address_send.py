import hashlib
import base58
import socket

from cryptography.hazmat.primitives.asymmetric import ec 
from cryptography.hazmat.primitives import serialization
def sha256(data):
    return hashlib.sha256(data).digest()
def ripemd160(data):
    return hashlib.new("ripemd160",data).digest()



# private_key_hex="0674904621abcfdaebad4325678914256378135275328902762896423425637"

private_key=ec.generate_private_key(ec.SECP256K1())

public_key=private_key.public_key()

public_key_bytes=public_key.public_bytes(
    encoding=serialization.Encoding.X962,
    format=serialization.PublicFormat.UncompressedPoint
)
sha2561=sha256(public_key_bytes)
ripemd1601=ripemd160(sha2561)


payload=b"\x00"+ripemd1601

cheksum=sha256(sha256(payload))[:4]

address= base58.b58encode(payload+cheksum).decode()


host="127.0.0.1"
port=5000

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((host,port))
client.send(address.encode())
client.close()

