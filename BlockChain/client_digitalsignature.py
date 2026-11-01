import hashlib
from cryptography.hazmat.primitives.asymmetric import rsa,padding
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes,serialization
import socket
import json


messege=b"tyuio"
private_key=rsa.generate_private_key(public_exponent=65507, key_size=2048)
public_key=private_key.public_key()


public_key_b=public_key.public_bytes(
    encoding=serialization.Encoding,
    format=serialization.public_key_byte
).decode()
signature=private_key.sign(
    messege,
    padding.PKCS1v15,
    hashes.SHA256
).decode()

data={
    "message":messege.decode(),
    "signature":signature,
    "priavte_key":public_key_b
}

host="127.0.0.1"
port=5000

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))
client.sendall(json.dumps(data).encode())
client.close()

