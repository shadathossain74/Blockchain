import hashlib
import base58
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
import socket



def hash256(data):
    return hashlib.sha256(data).digest()
def ripemd160(data):
    return hashlib.new("ripemd160",data).digest()


private_key_hex="0674904621abcfdaebad43256789142563781352753289027628964234256371"


private_key=ec.derive_private_key(int(private_key_hex,16),ec.SECP256K1())
public_key=private_key.public_key()


public_key_hex=public_key.public_bytes(
    encoding=serialization.Encoding.X962,
    format=serialization.PublicFormat.UncompressedPoint
)

sha_256=hash256(public_key_hex)

hashripemd16=ripemd160(sha_256)

payload =b"\x00"+hashripemd16


checksum =hash256(hash256(payload))[:4]

address=base58.b58encode(payload+checksum).decode()



host="127.0.0.1"
port=5000

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(1)

connection,address_info=server.accept()

receive_data=connection.recv(1024).decode()


# checkpart
payload=base58.b58decode(receive_data)

checksum=payload[-4:]
payload=payload[:-4]

checksum1=hash256(hash256(payload))[:4]

if checksum==checksum1:
    print("valid")
else:
    print("invalid")

connection.close()
server.close()




